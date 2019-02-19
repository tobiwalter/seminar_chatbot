# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:07:50 2019

@author: Tobias
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import firebase_admin
import datetime
from firebase_admin import credentials
from firebase_admin import db
#from flask import Flask, request, make_response, jsonify
from datetime import date
import dateparser
import pytz

# =============================================================================
# Initialize Firebase database instance 
# =============================================================================

cred = credentials.Certificate('C:\\Users\\Tobias\\Documents\\Uni Mannheim\\Team Project NLU\\service_account_key_thao.json')
# Fetch the service account key JSON file contents

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seminar-b9c58.firebaseio.com/'
})

# =============================================================================
# Define fixed values
# =============================================================================

firstname = "Teresa"
lastname = "Williams"
course = "machine learning"
city = "Munich"
seminar_date = ""
bookingtype = ""
display_option = ""
matchingID = "10"

employeesRef = db.reference('employees')
employees = employeesRef.get()
seminarRef = db.reference('seminars')
seminars = seminarRef.get()
bookingRef = db.reference('bookings')
bookings = bookingRef.get()
countRef = db.reference('counts')
counts = countRef.get()

# =============================================================================
# Test cancel seminar
# =============================================================================

def TestCancelSeminar():
#matching employer's name with their ID
    matchingID = 2
    course = "Excel"
    city = ""
    seminar_date = ""
    
    if not matchingID:
        res = "You are not in the database. Please contact HR."
        return res

    #matching seminar ID
    for j in range(len(seminars)):
        breaker = False
        for k in range(len(seminars[j]["description"])):
            if seminars[j]["description"][k].lower() == course.lower():
                seminar_id = seminars[j]["seminar_id"]
                print(seminar_id)
                breaker = True
                break
        if breaker:
            break
    
    if not 'seminar_id' in locals():
    #     dispatcher.utter_message("You don't have bookings according to your request.")
    #     return []
        return("No bookings according to your request.")
        
    #search for corresponding booking
    breaker = False
    for j in range(len(bookings)):
        if not "cancellation" in bookings[j]:
            print (bookings[j]["employee_id"] == matchingID and bookings[j]["seminar_id"]== seminar_id and datetime.datetime.strptime(bookings[j]["date"], '%d/%m/%y').date() > date.today())
            if bookings[j]["employee_id"] == matchingID and bookings[j]["seminar_id"]== seminar_id and datetime.datetime.strptime(bookings[j]["date"], '%d/%m/%y').date() > date.today():
#            if bookings[j]["employee_id"] == matchingID and bookings[j]["seminar_id"]== seminar_id and dateparser.parse(bookings[j]["date"]).date() > date.today():
                breaker_1 = True
                breaker_2 = True
                #check date in case user defined date
                if seminar_date != "":
                    breaker_1 = (dateparser.parse(seminar_date).date() == dateparser.parse(bookings[j]["date"]).date())
    
                #check location in case user defined location
                if city != "":
                    breaker_2 = city.lower() == bookings[j]["location"].lower()
                print (breaker)
                breaker = breaker_1 and breaker_2
    
            if breaker:
                #cancel booking by deleting entries
                seminar_date = bookings[j]["date"]
                cancellation = "cancelled on " + str(date.today())
                bookingRef.update({
                            str(j): {
                				'cancellation': cancellation
                            }})
                return ("Your seminar booking for " + course + " on " + seminar_date + " in " + city + " has been cancelled. You will receive a cancellation confirmation.")
    #            dispatcher.utter_message(res)
    #            return [SlotSet("cancellation_confirmed","True")]
            
    return ("Okay cool, okay cool.")
    #            dispatcher.utter_message("You don't have bookings according to your request.")
    #            return []
            
# =============================================================================
# Test show bookings 
# =============================================================================

def testShowBooking():
    # Find matching employee ID
        
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
                res = "This is your next seminar: " + showNextBooking(bookedSeminars)
            elif seminar_date:
                res = showBookingsOnGivenDate(seminar_date,bookedSeminars,matchingID)
        #                elif date_period:
        #                    dateStart = date_period["startDate"]
        #                    dateEnd = date_period["endDate"]
        #                    res = self.showBookingsWithinPeriod(dateStart, dateEnd, bookedSeminars, matchingID)
            elif city:
                res = showBoookingsAtLocation(city,bookedSeminars,matchingID)
            else:
                bookedSeminars = ', '.join(bookedSeminars)
                res = "These are your booked seminars: " + bookedSeminars
                
        #            dispatcher.utter_message(res)
        #            return []
            
        else:
            res = "There are no recorded bookings for you."
    #        dispatcher.utter_message(res)
    #        return [] 
    else:
    #    dispatcher.utter_message(res)
    #    return [SlotSet('user_verified', 'False')]  
        res = "You are not verified."
        
    return res
         
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
    given_date = dateparser.parse(seminar_date).date()

    bookings = bookingRef.get()
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

                sem = bookings[i]["seminar_title"] + " on " + bookings[i]["date"]
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
            bookings[i]["location"].lower() == city.lower() and
            bookings[i]["employee_id"] == matchingID):

                sem = bookings[i]["seminar_title"] + " on " + bookings[i]["date"]
                matchedSeminars.add(sem)

    if len(matchedSeminars) != 0:
        return "Your booked seminars in " + city + ": " + ', '.join(matchedSeminars)
    else:
        return "There are no recorded bookings for you in " + city
    
# =============================================================================
#     Test BookSeminar
# =============================================================================
def testBookSeminar():

    seminar_date = "02/04/19"
    for i in range(len(employees)):
            if employees[i]["First_name"].lower() == firstname.lower():
                if employees[i]["Last_name"].lower() == lastname.lower():
                    employee_id = employees[i]["employee_id"]
                    break
    
        
    if not "employee_id" in locals():
#        dispatcher.utter_message(resp)
#        return [SlotSet("user_verified","False")]
        return("Not verified")
    #check availability
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
        return ("The seminar you requested is not being offered.")

        #check location
    seminar = seminars[seminar_id]
    if not city.lower() in (sem.lower() for sem in seminar["locations"]):
#            dispatcher.utter_message("The seminar {} is not offered in {}".format(seminar["title"],city))
        return ("The seminar {} is not offered in {}".format(seminar["title"],city))
        
    if not dateparser.parse(seminar_date).date() in (dateparser.parse(d).date() for d in seminar["dates"]):
        print(dateparser.parse(seminar_date).date() in (dateparser.parse(d).date() for d in seminar["dates"]))
#            dispatcher.utter_message("The seminar {} is not offered on {}".format(seminar["title"],seminar_date))
        return ("The seminar {} is not offered on {}".format(seminar["title"],seminar_date))
    
    for l in range(len(seminar["locations"])):
        breaker = False
        if seminar["locations"][l].lower() == city.lower():
            return ("All seminars about " + course + " are booked out. You will be informed if new dates are available.") #this is the standard answer which will be changed if a seminar matches 
#            break
            #check occupancy
            if seminar["capacity"] > seminar["occupancy"]:
                occupancy = seminar["occupancy"]
                #check if already booked
                i = 0
                while i < len(bookings):
                    if not "cancellation" in bookings[i]:
                        if bookings[i]["employee_id"] == employee_id and bookings[i]["location"].lower() == city.lower() and bookings[i]["seminar_id"] == seminar_id:
                            return ("You have already booked the seminar " + course + " in "+city+" on " + bookings[i]["date"] + ".")
#                                breaker = True
#                                break
#                        i+=1

#                    if breaker:
#                        break
##                        dispatcher.utter_message(res)
##                        return [SlotSet("booking_confirmed","False")] 
                        else:
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
                                    return("Your booking request for the seminar " + course + " in "+city+" on " + seminar_date + " has been forwarded. You will receive a confirmation via email.")
                                
#                                dispatcher.utter_message(resp)
#                                return [SlotSet("booking_confirmed","True")]
#                            else:
#                                dispatcher.utter_message("The next date for the seminar is not known yet.")
#                                return [SlotSet("booking_confirmed","False")]