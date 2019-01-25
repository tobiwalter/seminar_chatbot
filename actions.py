# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:40:25 2019

@author: Tobias
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction
#import requests
#import json
#from random import randint
import datetime
#import os
#import yaml
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
#from flask import Flask, request, make_response, jsonify
from datetime import date
import dateparser
import pytz

# =============================================================================
# Initialize Firebase database instance 
# =============================================================================

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:\\Users\\Tobias\\Documents\\Uni Mannheim\\Team Project NLU\\service_account_key_thao.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seminar-b9c58.firebaseio.com/'
})

employees = db.reference('employees').get()
bookings = db.reference('bookings').get()
seminars = db.reference('seminars').get()
counts = db.reference('counts').get()        

class ActionShowBookings(Action):
    

    def name(self):
        """returns name of the action """
        return "action_show_bookings"
    
    def run(self, dispatcher, tracker, domain):
        """ retrieves slot values """
        
        res = "Your are not in our database. Please contact HR."
        firstname = tracker.get_slot('given-name')
        lastname = tracker.get_slot('last-name')
#        date_period = tracker.get_slot('date-period')
        seminar_date = tracker.get_slot('date')
        city = tracker.get_slot('location')
        bookingtype = tracker.get_slot('booking-type')
        display_option = tracker.get_slot('display-option')
        
        # Find matching employee ID
        for i in range(len(employees)):
            if employees[i]["First_name"].lower() == firstname.lower():
                if employees[i]["Last_name"].lower() == lastname.lower():
                    matchingID = employees[i]["employee_id"]
                    break
                
    #    Find booked seminars depending on params given
        if 'matchingID' in locals():
            bookingRef = db.reference('bookings')
            bookings = bookingRef.get()
            bookedSeminars = set([])
            
    #   Check for booking type and add seminars accordingly
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
                    res = "This is your next seminar: " + self.showNextBooking(bookedSeminars)
                elif seminar_date:
                    res = self.showBookingsOnGivenDate(seminar_date,bookedSeminars,matchingID)
#                elif date_period:
#                    dateStart = date_period["startDate"]
#                    dateEnd = date_period["endDate"]
#                    res = self.showBookingsWithinPeriod(dateStart, dateEnd, bookedSeminars, matchingID)
                elif city:
                    res = self.showBoookingsAtLocation(city,bookedSeminars,matchingID)
                else:
                    bookedSeminars = ', '.join(bookedSeminars)
                    res = "These are your booked seminars: " + bookedSeminars
                    
                dispatcher.utter_message(res)
                return []
                 
            else:
                res = "There are no recorded bookings for you."
                dispatcher.utter_message(res)
                return [] 
        else:
            dispatcher.utter_message(res)
            return [SlotSet('user_verified', 'False')]  
             
    def showNextBooking(self,bookedSeminars):
    
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
    
    
    def showBookingsOnGivenDate(self,seminar_date,bookedSeminars,matchingID):
    
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
    
    def showBookingsWithinPeriod(self,dateStart,dateEnd,bookedSeminars, matchingID):
        start = dateparser.parse(dateStart)
        end = dateparser.parse(dateEnd)
    
    #   If bookings between start and end, add them to the list of matched seminars
    
        matchedSeminars = set([])
        for i in range(len(bookings)):
            if not "cancellation" in bookings[i]:
                if (bookings[i]["seminar_title"] in bookedSeminars and
                start <= pytz.utc.localize(dateparser.parse(bookings[i]["date"])) <= end and
                bookings[i]["employee_id"] == matchingID):
    
                    sem = bookings[i]["seminar_title"] + " on " + bookings[i]["date"]
                    matchedSeminars.add(sem)
    
        if len(matchedSeminars) != 0:
            return "Your booked seminars between " + start.strftime("%d.%m.%y") + " and " + end.strftime("%d.%m.%Y") + ": " + ', '.join(matchedSeminars)
        else:
            return "There are no recorded bookings for you within the specified period."
    
    def showBoookingsAtLocation(self,city, bookedSeminars, matchingID):
    
        matchedSeminars = set([])
        for i in range(len(bookings)):
            if not "cancellation" in bookings[i]:
                if (bookings[i]["seminar_title"] in bookedSeminars and
                bookings[i]["location"].lower() == city.lower() and
                bookings[i]["employee_id"] == matchingID):
    
                    sem = bookings[i]["seminar_title"] + " on " + bookings[i]["date"]
                    matchedSeminars.add(sem)
    
        if len(matchedSeminars) != 0:
            return "Your booked seminars in " + city + ": " + ', '.join(matchedSeminars)
        else:
            return "There are no recorded bookings for you in " + city
            
        
class ActionBookSeminar(Action):
    def name(self):
        """returns name of the action """
        return "action_book_seminar"
    
    def run(self, dispatcher, tracker, domain):
        """ retrieves slot values """
        
        res = "You are not in our database. Please try to input your name again."
        
        firstname = tracker.get_slot('given-name')
        lastname = tracker.get_slot('last-name')
        course = tracker.get_slot('course')
        city = tracker.get_slot('location')

        #matching employee's name with their ID
        for i in range(len(employees)):
            if employees[i]["First_name"].lower() == firstname.lower():
                if employees[i]["Last_name"].lower() == lastname.lower():
                    employee_id = employees[i]["employee_id"]
                    break
    
        
        if not "employee_id" in locals():
            dispatcher.utter_message(res)
            return [SlotSet("user_verified","False")]
        
        #check availability
        res = "The seminar you requested is not being offered."
        for j in range(len(seminars)):
            breaker = False
            for k in range(len(seminars[j]["description"])):
                if seminars[j]["description"][k].lower() == course.lower():
                    seminar_id = seminars[j]["seminar_id"]
                    breaker = True
                    break
            if breaker== True:
                break
            
        if not "seminar_id" in locals():
            dispatcher.utter_message(res)
            return [SlotSet("booking_confirmed","False")] 
    
    
        #check location
        seminar = seminars[seminar_id]
        if not city.lower() in (sem.lower() for sem in seminar["locations"]):
            dispatcher.utter_message("The seminar {} is not offered in {}".format(seminar["title"],city))
            return []
        
        for l in range(len(seminar["locations"])):     ## use seminar[locations][city] if possible 
            if seminar["locations"][l].lower() == city.lower():
                res = "All seminars about " + course + " are booked out. You will be informed if new dates are available." #this is the standard answer which will be changed if a seminar matches 
#                    break
                #check occupancy
                if seminar["capacity"] > seminar["occupancy"]:
                    occupancy = seminar["occupancy"]
                    #check if already booked
                    for i in range(len(bookings)):
                        if not "cancellation" in bookings[i]:
                            if bookings[i]["employee_id"] == employee_id and bookings[i]["location"].lower() == city.lower() and bookings[i]["seminar_id"] == seminar_id:
                                res = "You have already booked the seminar " + course + " in "+city+" on " + bookings[i]["date"] + "."
                                dispatcher.utter_message(res)
                                return [SlotSet("booking_confirmed","False")] 

                                #check next date
                    for m in range(len(seminar["dates"])):
                        if dateparser.parse(seminar["dates"][m]).date() > date.today():
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
                                    'location': city,
                                    'seminar_id': seminar_id,
                                    'seminar_title': seminar["title"]
                                }})
                            res = "Your booking request for the seminar " + course + " in "+city+" on " + seminar_date + " has been forwarded. You will receive a confirmation via email."
                            
                            dispatcher.utter_message(res)
                            return [SlotSet("booking_confirmed","True")]
                        if m == len(seminar["dates"]): 
                            dispatcher.utter_message("A date for the seminar has not yet been fixed. We will notify you as soon we have a fixed date.")
                            return [SlotSet("booking_confirmed","False")]    

            #TO BE DONE: date suggestion, location alternative, capacity check

class ActionCancelSeminar(Action):
    def name(self):
        """returns name of the action """
        return "action_cancel_seminar"

    def run(self, dispatcher, tracker, domain):
        """ retrieves slot values """
        firstname = tracker.get_slot('given-name')
        lastname = tracker.get_slot('last-name')
        course = tracker.get_slot('course')
        city = tracker.get_slot('location')
        seminar_date = tracker.get_slot('date')
    
#matching employer's name with their ID
        for i in range(len(employees)):
            if employees[i]["First_name"].lower() == firstname.lower():
                if employees[i]["Last_name"].lower() == lastname.lower():
                    employee_id = employees[i]["employee_id"]
                    break

        if not 'employee_id' in locals():
            dispatcher.utter_message("You are not in the database. Please contact HR.")
            return []

#matching seminar ID
        for j in range(len(seminars)):
            breaker = False
            for k in range(len(seminars[j]["description"])):
                if seminars[j]["description"][k].lower() == course.lower():
                    seminar_id = seminars[j]["seminar_id"]
                    breaker = True
                    break
            if breaker:
                break
        
        if not 'seminar_id' in locals():
             dispatcher.utter_message("You don't have bookings according to your request.")
             return []
           
            
        #search for corresponding booking
        breaker = False
        for j in range(len(bookings)):
            if not "cancellation" in bookings[j]:
                if bookings[j]["employee_id"] == employee_id and bookings[j]["seminar_id"]== seminar_id and datetime.datetime.strptime(bookings[j]["date"], '%d/%m/%y').date() > date.today():
                    breaker_1 = True
                    breaker_2 = True
                    
                    #check date in case user defined date
                    if seminar_date != "":
                        breaker_1 = (dateparser.parse(seminar_date).date() == dateparser.parse(bookings[j]["date"]).date())
        
                    #check location in case user defined location
                    if city != "":
                        breaker_2 = city.lower() == bookings[j]["location"].lower()
        
                    breaker = breaker_1 and breaker_2
        
                if breaker:
                    #cancel booking by deleting entries
                    seminar_date = bookings[j]["date"]
                    cancellation = "cancelled on " + str(date.today())
                    bookingRef.update({
                                str(j): {
                    				'cancellation': cancellation
                                }})
                    res = "Your seminar booking for " + course + " on " + seminar_date + " in " + city + " has been cancelled. You will receive a cancellation confirmation."
                    dispatcher.utter_message(res)
                    return [SlotSet("cancellation_confirmed","True")]
                else:
                    res = "Okay cool, okay cool."
                    dispatcher.utter_message("You don't have bookings according to your request.")
                    return []

class ActionProvideDescription(Action):
    def name(self):
        """returns name of the action """
        return "action_provide_description"

    def run(self, dispatcher, tracker, domain):
        """ retrieves slot values """
            
        course = tracker.get_slot('course')
        course = tracker.get_slot('user-level')
    
        for j in range(len(seminars)):
            breaker = False
            for k in range(len(seminars[j]["description"])):
                if seminars[j]["description"][k].lower() == course.lower():
                    seminar_id = seminars[j]["seminar_id"]
                    breaker = True
                    break
            if breaker == True:
                break
    
        if "seminar_id" in locals():
            seminar = seminars[seminar_id]
            res = "The seminar {} is described as follows: \n \
            {}".format(seminar["title"],seminar["text"])
            dispatcher.utter_message(res)
            return []
            
        else:
            res = "We don't offer seminars that match your request."
            dispatcher.utter_message(res)
            return []
    
class ActionDisplaySeminar(Action):
    def name(self):
        """returns name of the action """
        return "action_display_seminar"

    def run(self, dispatcher, tracker, domain):
        """ retrieves slot values """
        
        course = tracker.get_slot('course')
        
        for j in range(len(seminars)):
            breaker = False
            for k in range(len(seminars[j]["description"])):
                if seminars[j]["description"][k].lower() == course.lower():
                    seminar_id = seminars[j]["seminar_id"]
                    breaker = True
                    break
            if breaker == True:
                break
            
        if "seminar_id" in locals():
            seminar = seminars[seminar_id]
            locations = ", ".join(seminar["locations"])
            dates = ", ".join(seminar["dates"])
            res = "The seminar {} is offered at the following locations and dates: \n \
            Locations: {} \n \
            Dates: {}".format(seminar["title"], locations, dates)
            
            dispatcher.utter_message(res)
            return [SlotSet("locations",locations), SlotSet("dates",dates), SlotSet("title",seminar["title"])]
            
        else:
            res = "We don't offer seminars that match your request."
            dispatcher.utter_message(res)
            return []
    
class ActionCourseOffering(Action):
    
    def name(self):
        """returns name of the action """
        return "action_course_offering"
    
    def run(self, dispatcher, tracker, domain):
        """ retrieves slot values """
        cats = set()
        for j in range(len(seminars)):
            cats.add(seminars[j]["category"])
            
        res = "We offer seminars in the following categories: \n\n" + ", ".join(cats)
        dispatcher.utter_message(res)
        return []
    
class ActionSelectDate(Action):
    
    def name(self):
        """returns name of the action """
        return "action_select_date"
    
    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot("location")
        dates = tracker.get_slot("dates")
        course = tracker.get_slot("course")
        
#        if sem_category: 
        if dates:
            if city:
                res = "On which date do you want to take the seminar in {}: \n \
                        {}.".format(city, ", ".join(dates))
            else:
                res = "On which date do you want to take the seminar: \n {}".format(", ".join(dates))
        else:    
            seminarRef = db.reference('seminars')
            seminars = seminarRef.get()
            for j in range(len(seminars)):
                breaker = False
                for k in range(len(seminars[j]["description"])):
                    if seminars[j]["description"][k].lower() == course.lower():
                        dates = seminars[j]["dates"]
                        breaker = True
                        break
                if breaker == True:
                    break
        
            if city:
                res = "On which date do you want to take the seminar in {}: \n \
                    {}.".format(city, ", ".join(dates))
            else: 
                res = "On which date do you want to take the seminar: \n {}".format(", ".join(dates))
                
        dispatcher.utter_message(res)
        return []

class ActionProvidePrerequisites(Action):
    def name(self):
        """returns name of the action """
        return "action_provide_prerequisites"

    def run(self, dispatcher, tracker, domain):
        """ retrieves slot values """
            
        course = tracker.get_slot('course')    
        prqs = []
        for j in range(len(seminars)):
            breaker = False
            if course.lower() in seminars[j]["description"]:
                for k in range(len(seminars[j]["prerequisites"])):
                    prqs.append(seminars[j]["prerequisites"][k])
                    breaker = True
            if breaker == True:
                break
            
        dispatcher.utter_message(", ".join(prqs))
        return []

class ActionProvideDatesWithLocation(Action):
 
    def name(self):
        """returns name of the action """
        return "action_provide_datesWithLocation"

    def run(self, dispatcher, tracker, domain):
        """ retrieves slot values """
        
        course = tracker.get_slot('course')
        results = ([],[])
        for j in range(len(seminars)):
            if course in seminars[j]["description"]:
                for k in range(len(seminars[j]["dates"])):
                    results[0].append(seminars[j]["dates"][k])
                    results[1].append(seminars[j]["locations"][k])
                
        resp = "The seminar takes place at the following dates and cities:\
        \n \n dates: {} \n cities: {} ".format(", ".join(results[0]),", ".join(results[1]))
        
        dispatcher.utter_message(resp)
        return [SlotSet("dates",results[0]), SlotSet("location", results[1])]

class VerifyUser(Action):
    def name(self):
        """returns name of the action """
        return "action_verify_user"

    def run(self, dispatcher, tracker, domain):
        """ retrieves slot values """
        
        firstname = tracker.get_slot('given-name')
        lastname = tracker.get_slot('last-name')
        
        # Find matching employee ID
        for i in range(len(employees)):
            if employees[i]["First_name"].lower() == firstname.lower():
                if employees[i]["Last_name"].lower() == lastname.lower():
                    return [SlotSet("user_verified","True"), SlotSet("employee_id",employees[i]["employee_id"])]
                
        dispatcher.utter_message("You are not in our database. Please try to input your name again")
        return [SlotSet("user_verified","False")]
    
class SeminarForm(FormAction):
   """Example of a custom form action"""

   def name(self):
       """Unique identifier of the form"""

       return "seminar_form"

   @staticmethod
   def required_slots(tracker):
       """A list of required slots that the form has to fill"""

       return ["course", "location", "date"]

   def submit(self, dispatcher, tracker, domain):
       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
       """Define what the form has to do after all required slots are filled"""

       # utter submit template
       dispatcher.utter_template('utter_submit', tracker)
       return []
                
                
                
        
    
            
            