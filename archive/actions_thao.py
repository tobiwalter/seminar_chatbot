from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from flask import Flask, request, make_response, jsonify
from datetime import date, datetime
import dateparser
import pytz

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/Users/thaonguyen/Documents/Studium/Data Science/Teamprojekt/Seminar-b253e5498290.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
	'databaseURL': 'https://seminar-b9c58.firebaseio.com/'
})

class Showbookings(Action):
	def name(self):
		return 'showbookings'

	def showNextBooking(bookedSeminars):
		bookingRef = db.reference('bookings')
		bookings = bookingRef.get()
		
		# Initialise date of next booking with first date in the list and iterate through all dates
		for i in range(len(bookings)):
			if not "cancellation" in bookings[i]:
				if bookings[i]["seminar_title"] in bookedSeminars:           
					temp = bookings[i]["date"]
					dateNext = dateparser.parse(temp).date() 
					break
					 
		for i in range(1,len(bookings)):
			if not "cancellation" in bookings[i]:
				if bookings[i]["seminar_title"] in bookedSeminars:      
					temp = bookings[i]["date"] 
					if dateparser.parse(temp).date() <= dateNext:
						dateNext = dateparser.parse(temp).date() 
						num = i 

		return bookings[num]["seminar_title"]

	def showBookingsOnGivenDate(seminar_date,bookedSeminars,matchingID):
			
		bookingRef = db.reference('bookings')
		bookings = bookingRef.get()    
		given_date = dateparser.parse(seminar_date).date() 
		
		matchedSeminars = set([])
						
		for i in range(len(bookings)):
			if not "cancellation" in bookings[i]:
				if (bookings[i]["seminar_title"] in bookedSeminars and
				dateparser.parse(bookings[i]["date"]).date() == given_date and
				bookings[i]["employee_id"] == matchingID):
					
					sem = bookings[i]["seminar_title"]
					matchedSeminars.add(sem)
					
		if len(matchedSeminars) != 0:
			return "Your booked seminars on " + given_date.strftime("%d.%m.%y") + ": " + ', '.join(matchedSeminars)
		else:
			return "There are no recorded bookings for you on the specified date."    
		
	def showBookingsWithinPeriod(dateStart,dateEnd,bookedSeminars, matchingID):
		bookingRef = db.reference('bookings')
		bookings = bookingRef.get()
		start = dateparser.parse(dateStart)
		end = dateparser.parse(dateEnd)
		
	#   If bookings between start and end, add them to the list of matched seminars

		matchedSeminars = set([])                    
		for i in range(len(bookings)):
			if not "cancellation" in bookings[i]:
				if (bookings[i]["seminar_title"] in bookedSeminars and
				start <= pytz.utc.localize(dateparser.parse(bookings[i]["date"])) <= end and
				bookings[i]["employee_id"] == matchingID):
					
					sem = bookings[i]["seminar_title"]
					matchedSeminars.add(sem)
					
		if len(matchedSeminars) != 0:
			return "Your booked seminars between " + start.strftime("%d.%m.%y") + " and " + end.strftime("%d.%m.%Y") + ": " + ', '.join(matchedSeminars)
		else:
			return "There are no recorded bookings for you within the specified period."            
		
	def showBoookingsAtLocation(city, bookedSeminars, matchingID):
		bookingRef = db.reference('bookings')
		bookings = bookingRef.get()

		matchedSeminars = set([])                    
		for i in range(len(bookings)):    
			if not "cancellation" in bookings[i]:
				if (bookings[i]["seminar_title"] in bookedSeminars and
				bookings[i]["location"].lower() == city and
				bookings[i]["employee_id"] == matchingID):
					
					sem = bookings[i]["seminar_title"]
					matchedSeminars.add(sem)
					
		if len(matchedSeminars) != 0:
			return "Your booked seminars in " + city + ": " + ', '.join(matchedSeminars)
		else:
			return "There are no recorded bookings for you in " + city

	def run(self, dispatcher, tracker, domain):
		# Initialise result as empty    
		resp = "Your are not in our database. Please contact HR."
		
		# fetch parameters from json
		display_option = tracker.get_slot('display-option').lower()
		seminar_date = tracker.get_slot('date')
		firstname = tracker.get_slot('given-name').lower()
		lastname = tracker.get_slot('last-name').lower()
		date_period = tracker.get_slot('date-period')
		bookingtype = tracker.get_slot('booking-type').lower()
		city = tracker.get_slot('city').lower()
		
		employeesRef = db.reference('employees')
		employees = employeesRef.get()
	   
		for i in range(len(employees)):
			if employees[i]["First_name"].lower() == firstname:
				if employees[i]["Last_name"].lower() == lastname:
					matchingID = employees[i]["employee_id"]
					break
					
		if 'matchingID' in locals():
			bookingRef = db.reference('bookings')
			bookings = bookingRef.get()
			bookedSeminars = set([])

			if bookingtype == 'past':
				for i in range(len(bookings)):
					if not "cancellation" in bookings[i]:
						if dateparser.parse(bookings[i]["date"]).date() < date.today():
							if  bookings[i]["employee_id"] == matchingID:
								sem = bookings[i]["seminar_title"] + " on " + bookings[i]["date"] + " in " + bookings[i]["location"]
								bookedSeminars.add(sem)
			elif bookingtype == 'upcoming':
				for i in range(len(bookings)):
					if not "cancellation" in bookings[i]:
						if dateparser.parse(bookings[i]["date"]).date() >= date.today():
							if  bookings[i]["employee_id"] == matchingID:
								sem = bookings[i]["seminar_title"] + " on " + bookings[i]["date"] + " in " + bookings[i]["location"]
								bookedSeminars.add(sem)
			else:
				for i in range(len(bookings)):
					if not "cancellation" in bookings[i]:
						if  bookings[i]["employee_id"] == matchingID:
							sem = bookings[i]["seminar_title"]
							bookedSeminars.add(sem)
			
			if len(bookedSeminars) != 0:
				if display_option == "next" or display_option == "upcoming":
					resp = "This is your next seminar: " + showNextBooking(bookedSeminars)
				elif seminar_date:
					resp = showBookingsOnGivenDate(seminar_date,bookedSeminars,matchingID)
				elif date_period:
					dateStart = date_period["startDate"]
					dateEnd = date_period["endDate"]
					resp = showBookingsWithinPeriod(dateStart, dateEnd, bookedSeminars, matchingID)
				elif city:
					resp = showBoookingsAtLocation(city, bookedSeminars, matchingID)
				else:
					bookedSeminars = ', '.join(bookedSeminars)   
					resp = "These are your booked seminars: " + bookedSeminars
			else:
				resp = "There are no recorded bookings for you."

		dispatcher.utter_message(resp)

class BookSeminar(Action):
	def name(self):
		return 'bookseminar'

	def run(self, dispatcher, tracker, domain):
		res = "You are not in our database. Please contact HR."
		
		firstname = tracker.get_slot('given-name').lower()
		lastname = tracker.get_slot('last-name').lower()
		course = tracker.get_slot('course').lower()
		city = tracker.get_slot('city').lower()

		employeesRef = db.reference('employees')
		employees = employeesRef.get()
		seminarRef = db.reference('seminars')
		seminars = seminarRef.get()
		bookingRef = db.reference('bookings')
		bookings = bookingRef.get()
		countRef = db.reference('counts')
		counts = countRef.get()

		#matching employer's name with their ID
		for i in range(len(employees)):
			if employees[i]["First_name"].lower() == firstname:
				if employees[i]["Last_name"].lower() == lastname:
					employee_id = employees[i]["employee_id"]
					break

		#check if given key word by the user matches any of the seminar key words in description
		if "employee_id" in locals():
			res = "The seminar you requested is not being offered in " + city.title() + "."

			for j in range(len(seminars)):
				breaker = False
				for k in range(len(seminars[j]["description"])):
					if seminars[j]["description"][k].lower() == course:
						seminar_id = seminars[j]["seminar_id"]
						breaker = True
						break
				if breaker== True:
					break
			
			if "seminar_id" in locals():
				seminar = seminars[seminar_id]

				#check location
				for l in range(len(seminar["locations"])):
					breaker = False
					if seminar["locations"][l].lower()==city:
						res = "All seminars about " + course.title() + " are booked out. You will be informed if new dates are available."
						
						#check occupancy
						if seminar["capacity"] > seminar["occupancy"]:
							occupancy = seminar["occupancy"]
							res = "Unfortunately, you missed our last seminar about " + course.title() + ". You will be informed if new dated are available."
						
							#check if already booked
							i = 0
							while i < len(bookings):
								if not "cancellation" in bookings[i]:
									if bookings[i]["employee_id"] == employee_id and bookings[i]["location"].lower() == city and bookings[i]["seminar_id"] == seminar_id:
										res = "You have already booked the seminar " + course.title() + " in "+city.title()+" on " + bookings[i]["date"]+"."
										breaker = True
										break
								i+=1

							if breaker:
								break
							else:
								#check next date
								for m in range(len(seminar["dates"])):
									if datetime.strptime(seminar["dates"][m], '%d/%m/%y').date()> date.today(): 
										seminar_date = str(seminar["dates"][m])

										#Update occupancy
										seminarRef.child(str(seminar_id)).update({"occupancy": occupancy + 1})

										#Update bookingcount
										booking_count = counts['booking_count'] + 1
										countRef.update({"booking_count": booking_count})

										#Write to DB
										bookingRef.update({
											str(booking_count): {
												'date': seminar_date,
												'employee_id': employee_id,
												'location': city.title(),
												'seminar_id': seminar_id,
												'seminar_title': seminar["title"]
											}})
										res = "Your booking request for the seminar " + course.title() + " in "+city.title()+" on " + seminar_date + " has been forwarded. You will receive a confirmation via email."
										breaker = True
										break
							if breaker:
								break

		#TO BE DONE: date suggestion, location alternative, capacity check
		dispatcher.utter_message(res)

class SeminarInfo(Action):
	def name(self):
		return 'seminarinfo'

	def run(self, dispatcher, tracker, domain):
		course = tracker.get_slot('course').lower()
		userlevel = tracker.get_slot('user-level').lower()

		seminarRef = db.reference('seminars')
		seminars = seminarRef.get()

		for j in range(len(seminars)):
			breaker = False
			for k in range(len(seminars[j]["description"])):
				if seminars[j]["description"][k].lower() == course:
					seminar_id = seminars[j]["seminar_id"]
					breaker = True
					break
			if breaker == True:
				break

		if "seminar_id" in locals():
			seminar = seminars[seminar_id]
			res = "We are offering the seminar " + seminar["title"] + " which is described as followed: \n"
			res = res + seminar["text"]
		else:
			res = "We don't have seminars that matches your request."
		dispatcher.utter_message(res)

class CancelSeminar(Action):
	def name(self):
		return 'cancelseminar'

	def run(self, dispatcher, tracker, domain):
		firstname = tracker.get_slot('given-name').lower()
		lastname = tracker.get_slot('last-name').lower()
		course = tracker.get_slot('course').lower()
		city = tracker.get_slot('city').lower()
		seminar_date = tracker.get_slot('date')

		employeesRef = db.reference('employees')
		employees = employeesRef.get()
		seminarRef = db.reference('seminars')
		seminars = seminarRef.get()
		bookingRef = db.reference('bookings')
		bookings = bookingRef.get()
		countRef = db.reference('counts')
		counts = countRef.get()

		res = "You are not in the database. Please contact HR."
		#matching employer's name with their ID
		for i in range(len(employees)):
			if employees[i]["First_name"].lower() == firstname:
				if employees[i]["Last_name"].lower() == lastname:
					employee_id = employees[i]["employee_id"]-1
					break

		#matching seminar ID
		for j in range(len(seminars)):
			breaker = False
			for k in range(len(seminars[j]["description"])):
				if seminars[j]["description"][k].lower() == course:
					seminar_id = seminars[j]["seminar_id"]-1
					res = "You don't have bookings according your request."
					breaker = True
					break
			if breaker:
				break
		
		breaker = False
		if 'employee_id' in locals() and 'seminar_id' in locals():
			#search for corresponding booking
			for j in range(len(bookings)):
				if not "cancellation" in bookings[j]:
					if bookings[j]["employee_id"] == employee_id and bookings[j]["seminar_id"]== seminar_id and datetime.strptime(bookings[j]["date"], '%d/%m/%y').date() > date.today():
						breaker_1 = True
						breaker_2 = True
		
						#check date in case user defined date
						if seminar_date != "":
							breaker_1 = (dateparser.parse(seminar_date).date() == dateparser.parse(bookings[j]["date"]).date())
		
						#check location in case user defined date
						if city != "":
							breaker_2 = (city == bookings[j]["location"].lower())
		
						breaker = breaker_1 and breaker_2
		
					if breaker:
						#cancel booking by deleting entries
						seminar_date = bookings[j]["date"]
						cancellation = "cancelled on " + str(date.today())
						bookingRef.update({
									str(j): {
										'cancellation': cancellation
									}})
						res = "Your seminar booking for " + course.title() + " on " + seminar_date + " in " + city.title() + " has been cancelled. You will receive a cancellation confirmation."
						break
		dispatcher.utter_message(res)