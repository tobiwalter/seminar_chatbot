from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from typing import Text, Dict, Any, List
from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted, Restarted
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk import ActionExecutionRejection
from helpers import matchingSeminar, dateComparison, period_check,date_check, location_check, nextLocation
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import dateparser
from time import strftime
import json

# =============================================================================
# Initialize Firebase database instance
# =============================================================================

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:\\Users\\Tobias\\Documents\\Uni Mannheim\\Team Project NLU\\service_account_key.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seminar-b9c58.firebaseio.com/'
})      

# Initialize references 
seminarRef = db.reference('seminars')
countRef = db.reference('counts')
employeesRef = db.reference('employees')
employees = employeesRef.get()
seminars = seminarRef.get()
counts = countRef.get()

# =============================================================================
# Rasa Code 
# =============================================================================

class ActionShowBookings(Action):
  """Retrieves user bookings depending on params given"""

  def name(self):
    """returns name of the action """
    return "action_show_bookings"

  def run(self, dispatcher, tracker, domain):
    """ retrieves slot values """

    matchingID = tracker.get_slot('employee_id')
    date_period = tracker.get_slot('date-period')
    userGivenDate = tracker.get_slot('date')
    time = tracker.get_slot('time')
    city = tracker.get_slot('location')
    bookingtype = tracker.get_slot('booking-type')
    display_option = tracker.get_slot('display-option')

  # Find booked seminars if a matching ID was extracted from user verification
  if matchingID is None:
      dispatcher.utter_template('utter_ask_name', tracker)
      return[FollowupAction('action_listen')]
  else:
      bookingRef = db.reference('bookings/' + str(matchingID))
      bookings = bookingRef.get()
      bookedSeminars = set([])

      if bookings:
        # Check for booking type and add seminars accordingly
        if bookingtype == 'past':
            bookedSeminars = ["{} in {} on {}".format(ele["seminar_title"], ele["location"], ele["date"]) 
                  for ele in bookings if not "cancellation" in ele if \
                  dateComparison(ele["date"], date.today()) == -1]

        elif bookingtype == 'upcoming':
            bookedSeminars = ["{} in {} on {}".format(ele["seminar_title"],ele["location"], ele["date"]) 
                  for ele in bookings if not "cancellation" in ele if \
                  dateComparison(ele["date"], date.today()) == 1]

        else:
            bookedSeminars = ["{} in {} on {}".format(ele["seminar_title"],ele["location"], ele["date"]) 
                  for ele in bookings if not "cancellation" in ele]

        # return bookings depending on params given     
        if len(bookedSeminars) != 0:
          if display_option == "next":
            res = "This is your next seminar: " + self.showNextBooking(bookings)
          elif userGivenDate:
            res = self.showBookingsOnGivenDate(time,userGivenDate,matchingID, bookings)
          elif date_period:
            res = self.showBookingsWithinPeriod(date_period,time,matchingID, bookings)
          elif city:
            res = self.showBoookingsAtLocation(city,matchingID, bookings)
          else:
            res = "These are your booked seminars: \n" + '\n '.join(sorted(bookedSeminars))

          dispatcher.utter_message(res)
          return [SlotSet("date", None),SlotSet("location",None), SlotSet("date-period",None), 
                  SlotSet("time",None), SlotSet('display-option',None),
                  SlotSet('booking-type',None) ]

      dispatcher.utter_message("There are no recorded bookings for you.")
      return []


  def showNextBooking(self,bookings):
    # Only consider future bookings and sort them 
    bookings = [ele for ele in bookings if not 'cancellation' in ele if 
      dateComparison(ele["date"], date.today()) == 1]
    bookings = sorted(bookings, key = lambda i: datetime.strptime(i['date'],"%d/%m/%y"))
    return "{} on {} in {}.".format(bookings[0]["seminar_title"],bookings[0]["date"],
      bookings[0]["location"])


  def showBookingsOnGivenDate(self, time, seminar_date, matchingID, bookings):
    # If nothing was extracted by Duckling, check if custom date entity could be extracted 
    if not time:
      userGivenDate = dateparser.parse(seminar_date,settings={'DATE_ORDER': 'DMY'}).date()
    else: 
      userGivenDate = dateparser.parse(time).date()

    matchedSeminars = ["{} in {}".format(ele["seminar_title"],ele["location"]) 
    for ele in bookings 
    if not 'cancellation' in ele if dateComparison(ele["date"], userGivenDate) == 0]

    if len(matchedSeminars) != 0:
      return "Your booked seminars on {} : {}.".format(userGivenDate.strftime("%d.%m.%y"),
            ', '.join(matchedSeminars))
    else:
      return "There are no recorded bookings for you on {}.".format(userGivenDate.strftime("%d.%m.%y"))


  def showBookingsWithinPeriod(self,date_period, time, matchingID, bookings):
    # Check if temporal expression extracted by duckling is an interval
    if isinstance(time, dict):
      start = dateparser.parse(time["from"]).date()
      end = dateparser.parse(time["to"]).date()  
    #   If bookings between start and end, add them to the list of matched seminars
      matchedSeminars = ["{} at {} in {}".format(ele["seminar_title"],ele["date"],ele["location"]) 
      for ele in bookings if not 'cancellation' in ele
      if start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end]

    # If duckling extracted a day value, set this day as start and try to infer 
    # the lenght of the interval by the value of the date period entity
    elif "week" in date_period.lower() or  "month" in date_period.lower() or "year" in date_period.lower():
      start = dateparser.parse(time).date()
      if "week" in date_period.lower():
        end = start + relativedelta(days = 7)
      elif "month" in date_period.lower():
        end = start + relativedelta(day=31)
      elif "year" in date_period.lower():
        end = start + relativedelta(day=365)

    # If bookings between start and end, add them to the list of matched seminars
      matchedSeminars = ["{} at {} in {}".format(ele["seminar_title"],ele["date"],ele["location"]) 
      for ele in bookings if not 'cancellation' in ele
      if start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end]

    # If date-period is a month or season and duckling only extracted a date value (e.g. "Show bookings in April")
    else:
      matchedSeminars = ["{} at {} in {}".format(ele["seminar_title"],ele["date"],ele["location"])
      for ele in bookings if not "cancellation" in ele 
                          if period_check(date_period, ele["date"])]
          

    if len(matchedSeminars) != 0:
      return "Your booked seminars for {}: \n{}".format(date_period.capitalize(),@@q@ "\n".join(matchedSeminars))
    else:
      return "There are no recorded bookings for you within the specified period."


  def showBoookingsAtLocation(self,city, matchingID, bookings):
    matchedSeminars = ["{} on {}".format(ele["seminar_title"],ele["date"]) for ele in bookings
        if not "cancellation" in ele if ele["location"].lower() == city.lower()]

    if len(matchedSeminars) != 0:
      return "Your booked seminars in {} : {}".format(city.capitalize(),', '.join(matchedSeminars))
    else:
      return "There are no recorded bookings for you in {}".format(city)


class ActionBookSeminar(Action):
"""Stores new seminar bookings in database"""

  def name(self):
    return "action_book_seminar"

  def run(self, dispatcher, tracker, domain):
    
    """ retrieves slot values """
    matchingID = tracker.get_slot('employee_id')
    course = tracker.get_slot('course')
    city = tracker.get_slot('location')
    booking_confirmed = tracker.get_slot('booking_confirmed')

    if matchingID is None:
      dispatcher.utter_template('utter_ask_name', tracker)
      return[FollowupAction('action_listen')]

    if not course:
      res = 'You need to specify a course for your request'
      dispatcher.utter_message(res)
      return [FollowupAction('action_course_offering')]
    else:
      #retrieve data snapshots
      countRef = db.reference('counts/booking_count')
      counts = countRef.child(str(matchingID)).get()
      bookingRef = db.reference('bookings/' + str(matchingID))
      bookings = bookingRef.get()
      seminarRef = db.reference('seminars')
      seminars = seminarRef.get()

      #matching seminar ID
      seminar_id = matchingSeminar(seminars,course)

      if seminar_id is None:
        res = "The seminar you requested is not being offered."
        dispatcher.utter_message(res)
        return [SlotSet("booking_confirmed",False)]

      #  In case necessary slots are not filled, ask user to fill them
      if not city:
        dispatcher.utter_template('utter_ask_location', tracker)
        return [SlotSet("booking_confirmed",False), FollowupAction('action_location_buttons')]
      else:  
        # Check if course is offered at user-given location
        seminar = seminars[seminar_id]
        if not city.capitalize() in seminar["locations"]:
          res = "The seminar {} is not offered in {}.".format(seminar["title"],city.capitalize())
          next_loc = nextLocation(city,seminar)
          if next_loc:
            res += " But there is a seminar in {}.".format(next_loc)

            buttons=[{'title': 'Yes', 'payload': "/affirm}"},{'title': 'No', 'payload': '/negative'}]
            dispatcher.utter_message(res)
            dispatcher.utter_button_message("Do you agree with this location?", buttons)
            return [SlotSet("booking_confirmed",False),SlotSet("location", next_loc), SlotSet("date", None),
            SlotSet("time", None), SlotSet("date-period", None), FollowupAction('utter_do_something_else')]
          else:
            dispatcher.utter_message(res)
            return [SlotSet("booking_confirmed",False),SlotSet("location", None), SlotSet("date", None),
            SlotSet("time", None), SlotSet("date-period", None), FollowupAction('utter_do_something_else')]

      # the entity representing the date can be one of two entities, 
      # 1) custom entity date or 2) built-in entity time from duckling
      userGivenDate = tracker.get_slot("date")
      if not userGivenDate:
        userGivenDate = tracker.get_slot("time")
      if not userGivenDate:
        dispatcher.utter_template('utter_ask_date', tracker)
        return [SlotSet("booking_confirmed",False), FollowupAction('action_date_buttons')]
      else: 
        dateMatch = None
        seminarDates = seminar["locations"][city.capitalize()]
        for ele in seminarDates:
          if userGivenDate is not None:
            if dateComparison(userGivenDate, ele["date"]) == 0: 
              dateMatch = ele
              userGivenDate = str(semdate)
              break
          elif time is not None:
            if dateComparison(time, ele["date"]) == 0: 
              dateMatch = ele
              userGivenDate = str(semdate)
              break

      if not dateMatch:
        dispatcher.utter_message("The seminar {} is not offered on the specified date".format(seminar["title"]))
        return [SlotSet("booking_confirmed", False),SlotSet("date", None), SlotSet("time", None),
        FollowupAction('utter_do_something_else')]

      #If date and location check successful, check if spot still available at given date and location      
      if seminar["capacity"] == dateMatch["occupancy"]:
        dispatcher.utter_message("All seminars about {} are booked out.".format(course))
        return [SlotSet("booking_confirmed",False),SlotSet("date", None), SlotSet("time", None),
                SlotSet("location",None), SlotSet('date-period', None), FollowupAction('utter_do_something_else')]

      # If not booked, perform booking from here on: First, update occupancy on matched date 
      occupancy = dateMatch["occupancy"]
      occupancy += 1  
      occupancyRef = seminarRef.child("{}/locations/{}/{}".format(str(seminar_id), city.capitalize(),
        str(seminarDates.index(dateMatch)))).update({"occupancy": occupancy})

      try:
        # Update booking count of matching employee
        countRef.update({str(matchingID): counts+1})
      except:
        print('Occupancy update failed!')

      #Write to DB
      booking_count = len(bookings) + 1 if bookings is not None else 1
      
      try:
        bookingRef.update({
          str(booking_count -1): {
          'date': userGivenDate ,
          'location': city.capitalize(),
          'seminar_id' : seminar_id,
          'seminar_title': seminar["title"]
          }})
      except:
        print('Booking could not be stored successfully.')

      res = "Your booking request for the seminar {} in {} on {} has been forwarded.\n You will receive a confirmation via email.\n".format(
        course.capitalize(),city.capitalize(),userGivenDate)
      
      # Check for date clashes: loop through bookings and check if there is another booking on the requested date (breaker1 = false)
      # or if there is a booking for the same requested course with a future date (breaker2 = false).
      breaker1 = True
      breaker2 = True
      res1 = []
      res2 = []
      if bookings:
          for ele in bookings:
            if not "cancellation" in ele:
              if ele["date"] == userGivenDate : 
                res1.append("{} in {} on {}".format(ele["seminar_title"],ele["location"],ele["date"]))
                breaker1 = False
              if ele["seminar_id"] == seminar_id and dateComparison(ele["date"], date.today()) == 1:
                res2.append("in {} on {}".format(ele["location"],ele["date"]))
                breaker2 = False

          # If a date clash was found (breaker1 or/and breaker2 is set false), ask if user wants to cancel one of the seminars
          # otherwise only return booking confirmation message.
          if not breaker2:
            res += "\nYou have already booked the seminar {}: ".format(course.capitalize())
            res += ',\t'.join(res2)

            buttons=[{'title': 'Yes', 'payload': '/cancel_seminar'},{'title': 'No', 'payload': '/negative'}]
            dispatcher.utter_message(res)
            dispatcher.utter_button_message("Do you want to cancel one seminar?", buttons)
          elif not breaker1:
            res += "\nYou have another seminar on the same day: {}".format(',\t'.join(res1))

            buttons=[{'title': 'Yes', 'payload': '/cancel_seminar'},{'title': 'No', 'payload': '/negative'}]
            dispatcher.utter_message(res)
            dispatcher.utter_button_message("Do you want to cancel one seminar?", buttons)
          else:
            dispatcher.utter_message(res)
      else:
          dispatcher.utter_message(res)

      return [SlotSet("booking_confirmed",True),SlotSet("date", None), SlotSet("time", None),
              SlotSet('date-period',None), SlotSet("location",None), SlotSet("course",None), 
              FollowupAction('action_listen')]


class ActionCancelSeminar(Action):
  """Deletes seminar bookings from database"""

  def name(self):
    return "action_cancel_seminar"

  def run(self, dispatcher, tracker, domain):
    matchingID = tracker.get_slot('employee_id')
    course = tracker.get_slot('course')
    city = tracker.get_slot('location')
    userGivenDate = tracker.get_slot('date')
    date_period = tracker.get_slot('date-period')
    time = tracker.get_slot('time')

    if matchingID is None:
      dispatcher.utter_template('utter_ask_name', tracker)
      return[FollowupAction('action_listen'), SlotSet('cancellation_confirmed', False)]
    else:
      bookingRef = db.reference('bookings/' + str(matchingID))
      bookings = bookingRef.get()

      # If no course given, show user bookings and ask which course to cancel
      if not course:
          dispatcher.utter_template('utter_ask_course_cancel', tracker)
          return [FollowupAction('action_show_bookings')]
      else: 
        seminar_id = matchingSeminar(seminars,course)
        
        if seminar_id is None:
          dispatcher.utter_message("There is no seminar matching your request.")
          return [SlotSet("cancellation_confirmed",False), SlotSet("course",None),
           SlotSet("location",None), SlotSet("date",None), SlotSet("time", None),
            FollowupAction('utter_suggest_help')]

        #Search for corresponding booking
        if not bookings:
          dispatcher.utter_message("We do not have bookings for you in our database.")
          return  [SlotSet("cancellation_confirmed",False), SlotSet("course",None), SlotSet("time", None),
                 SlotSet("location",None), SlotSet("date",None), FollowupAction('utter_suggest_help')]
        else:
          for ele in bookings:
            # ignore cancelled bookings
            if not "cancellation" in ele:
              if ele["seminar_id"] == seminar_id and dateComparison(ele["date"], date.today()) == 1:

                #Check date (period) and location match in case specified by user when cancelling 

                dateEqual = True
                locEqual  = True
                
                if userGivenDate:
                  dateEqual = (dateComparison(userGivenDate, ele["date"]) == 0)

                elif date_period:
                  # Check if temporal expression extracted by duckling is an interval, i.e. has a "from" and "two" value
                  if isinstance(time, dict):
                    start = dateparser.parse(time["from"]).date()
                    end = dateparser.parse(time["to"]).date()  

                    dateEqual = (start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end)

                  elif "week" in date_period.lower() or "month" in date_period.lower() or "year" in date_period.lower():
                    start = dateparser.parse(time,settings={'DATE_ORDER': 'DMY'}).date()
                    if "week" in date_period.lower():
                      end = start + relativedelta(days = 7)
                    elif "month" in date_period.lower():
                      end = start + relativedelta(day=31)
                    elif "year" in date_period.lower():
                      end = start + relativedelta(day=365)

                    dateEqual = (start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end)

                  else:
                    dateEqual = period_check(date_period, ele["date"])
                
                #check location in case user defined location
                if city:
                  locEqual = city.lower() == ele["location"].lower() 

                if dateEqual and locEqual:
                  #cancel booking by deleting entries
                  seminar_date = ele["date"]
                  city = ele["location"]
                  cancellation = "cancelled on " + str(date.today())
                  try: 
                    bookingRef.update({str(bookings.index(ele)): {'cancellation': cancellation}})
                  except:
                    print('Booking could not be deleted from database.')

                #Update occupancy 
                  try:
                    seminarDates = seminars[seminar_id]["locations"][city.capitalize()]
                    for ele in seminarDates:
                      semdate = ele["date"]
                      if dateComparison(seminar_date, semdate) == 0:
                        dateMatch = ele
                        occupancy = ele["occupancy"]
                        occupancy -= 1 if occupancy > 0 else 0
                        occupancyRef = seminarRef.child("{}/locations/{}/{}".format(str(seminar_id),
                        city.capitalize(),str(seminarDates.index(dateMatch)))).update({"occupancy": occupancy})
                        break
                  except:
                    print('Seminar date is not in the database. No occupancy update!')
                
                  res = "Your seminar booking for {} on {} in {} has been cancelled.\n \
                  You will receive a cancellation confirmation by mail.".format(
                    course.capitalize(), seminar_date, city.capitalize())

                  dispatcher.utter_message(res)
                  return [SlotSet("cancellation_confirmed",True), SlotSet("course",None),
                   SlotSet("location",None), SlotSet("date",None), SlotSet("time", None),
                   FollowupAction('action_listen')]


class ActionProvideDescription(Action):

  def name(self):
    return "action_provide_description"

  def run(self, dispatcher, tracker, domain):
    course = tracker.get_slot("course")

    if course is not None:
      seminar_id = matchingSeminar(seminars,course)
    else: 
      res = 'You need to specify a course for your request'
      dispatcher.utter_message(res)
      return [FollowupAction('action_course_offering')]

    if seminar_id != None:
      seminar = seminars[seminar_id]
      attachment = json.dumps([{
          "fallback": seminar['text'], #only if client doesn't show formatted text
          "color": "good",
          "pretext": "You may be interested in this seminar ",
          "title": seminar['title'],
          "title_link": seminar['url'],
          "text": seminar['text']}])
      dispatcher.utter_attachment(attachment)
      return []
    else:
      res = "We don't offer seminars that match your request."
      dispatcher.utter_message(res)
      return []


class ActionDisplaySeminar(Action):
  """Display dates and locations of a given seminar or seminars that are available in given location/time period"""

  def name(self):
    return "action_display_seminar"

  def run(self, dispatcher, tracker, domain):
    """ retrieves slot values """
    course = tracker.get_slot('course')
    city = tracker.get_slot('location')
    date_period = tracker.get_slot('date-period')
    time = tracker.get_slot('time')

    # First priority: If course entity could be extracted, check if corresponding seminar can be matched
    if course:
      seminar_id = matchingSeminar(seminars,course)

      # If seminar could be matched, display seminar dates and locations of only this seminar
      if seminar_id is not None:
        seminarRef = db.reference('seminars/' + str(seminar_id))
        seminar = seminarRef.get()

        locs = sorted(seminar["locations"])
        dates = {}

        for loc in locs:
          # Check if date-period was given by user
          if not date_period:
            # If no date-period, add all seminar dates that are not booked out yet
            dates[loc] = [ele["date"] for ele in seminar["locations"][loc] 
            if ele["occupancy"] < seminar["capacity"]]

          # If date-period was given by user, only display dates in requested period
          else:
            
            # Check if temporal expression extracted by duckling is a time interval
            if isinstance(time, dict):
              start = dateparser.parse(time["from"]).date()
              end = dateparser.parse(time["to"]).date()  

              dates[loc] = [ele["date"] for ele in seminar["locations"][loc] 
              if ele["occupancy"] < seminar["capacity"] 
              if start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end]

            # If duckling extracted a day value, set this day as start and try to infer
            # the lenght of the interval by the value of the date period entity
            elif "week" in date_period.lower() or  "month" in date_period.lower() or "year" in date_period.lower():
              start = dateparser.parse(time).date()
              if "week" in date_period.lower():
                end = start + relativedelta(days = 7)
              elif "month" in date_period.lower():
                end = start + relativedelta(day=31)
              elif "year" in date_period.lower():
                end = start + relativedelta(day=365)              

              dates[loc] = [ele["date"] for ele in seminar["locations"][loc]
              if ele["occupancy"] < seminar["capacity"] 
              if start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end]    

            # If date-period is a month or season and duckling only extracted a date value
            else:
              dates[loc] = [ele["date"] for ele in seminar["locations"][loc] 
              if ele["occupancy"] < seminar["capacity"] 
              if period_check(date_period, ele["date"])]

          # sort extracted dates for each location      
          if len(dates[loc]) > 0:
            dates[loc] = sorted(dates[loc], key=lambda x: datetime.strptime(x, '%d/%m/%y'))

        #do not display locations that are fully booked for all dates
        dates = dict( [(k,v) for k,v in dates.items() if len(v)>0])

        if dates:
          res = "The seminar {} is offered at the following locations and dates:\n\n".format(seminar["title"])
          res += '\n'.join(["*{:5}*: \t{:<5}".format(key, ',\t'.join(value)) for key, value in dates.items()])
          attachment = json.dumps([{
          "text": res}])
          dispatcher.utter_attachment(attachment)
          return [SlotSet("locations", locs),SlotSet("title", seminar["title"]),SlotSet("seminar_id", seminar_id), SlotSet('time', None)]

        else:
          res = "There are no booking dates available for {} in the given period".format(seminar["title"])
          dispatcher.utter_message(res)
          return[SlotSet('date-period', None), SlotSet('time', None), FollowupAction('utter_do_something_else')]

      # If course, but no matching seminar id could be found
      else:
        res = "We don't offer {} seminars.".format(course)
        dispatcher.utter_message(res)
        return [FollowupAction('utter_do_something_else'), SlotSet('course', None), SlotSet('location', None),
        SlotSet('time', None), SlotSet('date', None), SlotSet('date-period', None)]

    #Second priority: If no course, but location could be extracted, find seminars at that location
    elif city:
      available_seminars = [ele["category"] for ele in seminars if city.capitalize() in ele["locations"]]
          
      if len(available_seminars) != 0:
        res = "We offer the following seminars in {} :\n{}".format(city.capitalize(), ', '.join(available_seminars))
        dispatcher.utter_message(res)
        return [SlotSet('categories', available_seminars),SlotSet('date-period', None), SlotSet('time', None)]

      else: 
        dispatcher.utter_message("There are no seminars offered in {}".format(city))
        return [SlotSet('location', None), FollowupAction('utter_do_something_else')]

    # Third priority: If no course and loc, but date period could be extracted, find seminars within this period
    elif date_period:
      available_seminars = []

      if isinstance(time, dict):
        start = dateparser.parse(time["from"]).date()
        end = dateparser.parse(time["to"]).date()  

        for sem in seminars:
          cities = []
          for loc in sem["locations"]:
            for ele in sem["locations"][loc]:
              if start <= dateparser.parse(ele["date"],settings={'DATE_ORDER': 'DMY'}).date() <= end:
                cities.append(loc)
                break
          # Add seminar and cities where it can be booked
          if cities:
            seminar = "{} in {}".format(sem["category"],", ".join(cities))
            available_seminars.append(seminar)

      elif "week" in date_period.lower() or  "month" in date_period.lower() or "year" in date_period.lower():
        start = dateparser.parse(time).date()
        if "week" in date_period.lower():
          end = start + relativedelta(days = 7)
        elif "month" in date_period.lower():
          end = start + relativedelta(day=31)
        elif "year" in date_period.lower():
          end = start + relativedelta(day=365)

        for sem in seminars:
          cities = [] 
          for loc in sem["locations"]:
            for ele in sem["locations"][loc]:
              if start <= dateparser.parse(ele["date"],settings={'DATE_ORDER': 'DMY'}).date() <= end:
                cities.append(loc)
                break

          # Add seminar and cities where it can be booked
          if cities:
            seminar = sem["category"] + " in {}".format(", ".join(cities))
            available_seminars.append(seminar)

      else:
        for sem in seminars:
          cities = []
          for loc in sem["locations"]:
            for ele in sem["locations"][loc]:
              if period_check(date_period, ele["date"]):
                cities.append(loc)
                break

          # Add seminar and cities where it can be booked
          if cities:
            seminar = sem["category"] + " in {}".format(", ".join(cities))
            available_seminars.append(seminar)

      # Display all available seminars with locations in the specified period
      if len(available_seminars) != 0:
        res = "We offer the following seminars in the specified period:\n{}".format(
          '\n'.join(available_seminars))
        dispatcher.utter_message(res)
        return [SlotSet('categories', available_seminars),SlotSet('date-period', None), SlotSet('time', None)]
      else: 
        dispatcher.utter_message("There are no seminars offered in the given period.")
        return[SlotSet('date-period', None), SlotSet('time', None), FollowupAction('utter_do_something_else')]

    # Show the course offering if no course entity or anything else could be extracted 
    else: 
      dispatcher.utter_message("You need to specify a course for your request.")
      return [FollowupAction('action_course_offering'), SlotSet('location', None), SlotSet('time', None), SlotSet('date', None), SlotSet('date-period', None)]


class ActionCourseOffering(Action):
"""Display seminar offering or seminars offered in a specific city depending on the user intent""" 

  def name(self):
    return "action_course_offering"

  def run(self, dispatcher, tracker, domain):
    intent = tracker.latest_message['intent'].get('name')

    # If user wants to know what courses are offered  
    if intent != 'get_location':
      cats = {ele["category"] for ele in seminars}
      res = "We offer the following seminars: \n\n" + ", ".join(cats)
      dispatcher.utter_message(res)
      return []

    # If user wants to know in which cities courses are offered
    elif intent == 'get_location':
      cities = {loc for sem in seminars for loc in sem["locations"]}
      res = "We offer seminars in the following cities: \n\n" + ", ".join(cities)
      dispatcher.utter_message(res)
      return [] 


class ActionQueryDate(Action):
"""Display dates of a given seminar in a given city"""

    def name(self):
        return "action_query_date"

    def run(self, dispatcher, tracker, domain):
        course = tracker.get_slot("course")
        city = tracker.get_slot("location")

        # If wrong prediction made by dialogue management
        if not city:
          return[FollowupAction('action_display_seminar')]

        if course:
          seminar_id = matchingSeminar(seminars,course)
        else: 
          res = 'You need to specify a course for your request'
          dispatcher.utter_message(res)
          return [FollowupAction('action_course_offering')]

        if seminar_id is not None:
            seminarRef = db.reference('seminars/' + str(seminar_id))
            seminar = seminarRef.get()

        # Collect dates of seminar in the corresponding city
            if city.capitalize() in seminar["locations"] and location_check(seminar, city):
              dates = [ele["date"] for ele in seminar["locations"][city] if date_check(seminar, city, ele["date"])]

              dates = sorted(dates, key=lambda x: datetime.strptime(x, '%d/%m/%y'))
              res = "In {} the seminar takes place on those dates: \n{}".format(city, ", \t".join(dates))
              dispatcher.utter_message(res)
              return [SlotSet("dates", ', '.join(dates)), SlotSet("title", seminar["title"],
                SlotSet('time', None))]

            # Suggest closest seminar location if seminar not held in specified city 
            else:
                res = "The seminar {} is not offered in {}.".format(seminar["title"],city)
                next_loc = nextLocation(city.capitalize(),seminar)
                if next_loc:
                    res += " But there is a seminar in {}.".format(next_loc)

                    buttons=[{'title': 'Yes', 'payload': "/affirm}"},{'title': 'No', 'payload': '/negative'}]
                    dispatcher.utter_message(res)
                    dispatcher.utter_button_message("Do you agree with this location?", buttons)
                    return [SlotSet("location",next_loc)]
                else:
                    dispatcher.utter_message(res)
                    return []
        else: 
            res = "We don't offer {} seminars.".format(course)
            dispatcher.utter_message(res)
            return []


class ActionProvidePrerequisites(Action):

  def name(self):
    return "action_provide_prerequisites"

  def run(self, dispatcher, tracker, domain):
    course = tracker.get_slot('course')

    if course:
      seminar_id = matchingSeminar(seminars,course)
    else: 
      res = 'You need to specify a course for your request'
      dispatcher.utter_message(res)
      return[FollowupAction('action_course_offering')]

    if seminar_id != None:
      prqs = seminars[seminar_id]["prerequisites"]
        
      if prqs == "none":
            dispatcher.utter_message("There are no prerequisites.")
            return []
      else:
            dispatcher.utter_message("The prerequisites are {}.".format(" & ".join(prqs)))
            return []
    else: 
        res = "We don't offer {} seminars.".format(course)
        dispatcher.utter_message(res)
        return []
  

class ActionQueryLevel(Action):

  def name(self):
    return "action_query_level"

  def run(self, dispatcher, tracker, domain):
    course = tracker.get_slot('course')

    if course:
      seminar_id = matchingSeminar(seminars,course)
    else: 
      res = 'You need to specify a course for your request'
      dispatcher.utter_message(res)
      return[FollowupAction('action_course_offering')]

    if seminar_id != None:
        level = seminars[seminar_id]["level"]
        dispatcher.utter_message("This is the level of the course: {}".format(level))
        return []
    else: 
        res = "We don't offer {} seminars.".format(course)
        dispatcher.utter_message(res)
        return []


class ActionQueryDuration(Action):

  def name(self):
    """returns name of the action """
    return "action_query_duration"

  def run(self, dispatcher, tracker, domain):
    course = tracker.get_slot('course')

    if course:
      seminar_id = matchingSeminar(seminars,course)
    else: 
      res = 'You need to specify a course for your request'
      dispatcher.utter_message(res)
      return[FollowupAction('action_course_offering')]

    if seminar_id is not None:
        duration = seminars[seminar_id]["duration (days)"]
        if duration == 1:
          res = "The seminar is scheduled over one day from 9 am to 5 pm.".format(duration)
        elif duration > 1:
          res = "The seminar is scheduled over {} days from 9 am to 5 pm.".format(duration)
        dispatcher.utter_message(res)
        return []
    else:
      res = "We don't offer {} seminars.".format(course)
      dispatcher.utter_message(res)
      return []


  class VerifyUser(Action):

    def name(self):
      return "action_verify_user"

    def run(self, dispatcher, tracker, domain):
      firstname = tracker.get_slot('given-name')
      lastname = tracker.get_slot('last-name')
      verification = tracker.get_slot('user_verified')

      # Find matching employee identifier
      if firstname and lastname:
        for e in employees:
          if e["First_name"].lower() == firstname.lower():
            if e["Last_name"].lower() == lastname.lower():
              dispatcher.utter_message("Hello {}.".format(firstname.capitalize()))
              return [SlotSet("user_verified",True), SlotSet("employee_id",e["employee_id"])]

      ## if slot set already, that means bot ask for the 2nd time,
      ## so if verification fails again, suggest_help
      if verification is False:
        dispatcher.utter_message("You are not in our database. Please contact HR.")
        return [SlotSet('user_verified', False), FollowupAction('utter_suggest_help')]
      else:
        # Prompt user to input name again in case verification fails for 1st time
        dispatcher.utter_template('utter_try_again', tracker)
        return [SlotSet('user_verified', False), FollowupAction('action_listen')]


class SeminarForm(FormAction):
  """ Asks user for location and date slots that are needed in order to perform a booking"""

  RANDOMIZE = False

  def name(self):
    return "seminar_form"

  @staticmethod
  def required_slots(tracker):
     
    if tracker.get_slot('time') and not isinstance(tracker.get_slot('time'),dict):
      return ["location"]
    else:
      return ["location", "date"]

  def slot_mappings(self):
    return {"date": [self.from_entity(entity="date", intent=["inform","book_seminar"]),
        self.from_entity(entity="time", intent=["inform","book_seminar"])],
        "location": self.from_entity(entity="location", intent= ["book_seminar","inform"])}
   
  @staticmethod 
  def date_in_database(val,tracker):
    course = tracker.get_slot('course')
    city = tracker.get_slot('location')
    seminar_id = matchingSeminar(seminars,course)
    seminar = seminars[seminar_id]

    isDate = False
    for ele in seminar["locations"][city]:
      if dateComparison(val, ele["date"]) == 0:
        isDate = True
        break
    return isDate
       
  @staticmethod         
  def loc_in_database(val,tracker):
    course = tracker.get_slot('course')
    seminar_id = matchingSeminar(seminars,course)
    seminar = seminars[seminar_id]
    if val.capitalize() in seminar["locations"]:
      return True
    else:
      return False 

  def validate(self, dispatcher, tracker, domain):
    """Validate extracted requested slot
      else reject the execution of the form action
    """
    # extract other slots that were not requested
    # but set by corresponding entity
    slot_values = self.extract_other_slots(dispatcher, tracker, domain)

    # extract requested slot
    slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
    if slot_to_fill:
      for slot, value in self.extract_requested_slot(dispatcher,
                               tracker,
                               domain).items():
        validate_func = getattr(self, "validate_{}".format(slot),
                    lambda *x: value)
        slot_values[slot] = validate_func(value, dispatcher, tracker,domain)

      if not slot_values:
        # reject form action execution
        # if some slot was requested but nothing was extracted
        # it will allow other policies to predict another action
        raise ActionExecutionRejection(self.name(),
                       "Failed to validate slot {0} "
                       "with action {1}"
                       "".format(slot_to_fill,
                             self.name()))
    # we'll check when validation failed in order
    # to add appropriate utterances
    for slot, value in slot_values.items():
      if slot == "date" or slot == "time":
        if not self.date_in_database(value,tracker):
          dispatcher.utter_template("utter_wrong_date", tracker)
          # validation failed, set slot to None
          slot_values[slot] = None

      elif slot == "location":
        if not self.loc_in_database(value,tracker):
          dispatcher.utter_template("utter_wrong_location", tracker)
          slot_values[slot] = None
           # validation failed, set slot to None

    # validation succeed, set the slots values to the extracted values
    return [SlotSet(slot, value) for slot, value in slot_values.items()]

  def request_next_slot(self, dispatcher, tracker, domain):
    for slot in self.required_slots(tracker):
      if self._should_request_slot(tracker, slot):
        dispatcher.utter_template("utter_ask_{}".format(slot), tracker)
        if slot == "location":
          ActionLocationButtons().run(dispatcher, tracker, domain)
          return [SlotSet(REQUESTED_SLOT, slot)]
        elif slot == "date":
          ActionDateButtons().run(dispatcher, tracker, domain)
          return [SlotSet(REQUESTED_SLOT, slot)]
    return None

  def submit(self, dispatcher, tracker, domain):
    dispatcher.utter_template('utter_submit', tracker)
    return [FollowupAction('action_book_seminar')]


class ActionLocationButtons(Action):

  def name(self):
      return "action_location_buttons"

  def run(self, dispatcher, tracker, domain):
      course = tracker.get_slot('course')

      if course: 
        seminars = db.reference('seminars').get()
        seminar_id = matchingSeminar(seminars,course)
      else:
        res = 'You need to specify a course for your request'
        dispatcher.utter_message(res)
        return[FollowupAction('action_course_offering')]

      if seminar_id is not None:
        seminar = seminars[seminar_id]
        locations = seminar.get("locations")  
        loc_occupancy = {}
        buttons = []

        # Get working location of employee to give closer locations higher priority
        employee_id = tracker.get_slot("employee_id")

        if employee_id is None:
          return FollowupAction('action_verify_user')
        home_city = employees[employee_id]["location"]

        for loc in locations:

          # Primarily, display locations with occupancy < 70% and sort by distance
          # Secondarily, display locations with occupancy > 70 % and sort by average occupancy
          occ = 0
          count = 0
          for ele in seminar["locations"][loc]:
            occ += ele["occupancy"]
            count += 1
        #do not display locations that are fully booked
          if occ < count*seminar["capacity"]:
            loc_occupancy[loc] = []
            loc_occupancy[loc].append(round(occ/count,2))
            if round(occ/count,2) > 0.7:
                loc_occupancy[loc].append(float('inf'))
            else:
                loc_distance = self.locDistance(home_city, loc)
                loc_occupancy[loc].append(loc_distance)

        sort_by_dis = {}
        sort_by_occ = {}

        for l in list(loc_occupancy):
            if loc_occupancy[l][1] < float('inf'):
               sort_by_dis[l] = loc_occupancy[l][1]
            else:
               sort_by_occ[l] = loc_occupancy[l][1]

        loc_buttons = sorted(sort_by_dis.items(), key=lambda x: x[1])
        # add buttons for locations with > 70 % occupancy 
        loc_buttons += sorted(sort_by_occ.items(), key=lambda x: x[1])

        #displaying top 3 locations
        for x in list(loc_buttons)[0:3]:
          buttons.append({'title': x[0], 'payload': '/inform{"location": \"' + x[0].capitalize() + '\"}'})

        # if not satisfied with one of 3 suggested locations, user can ask for other locations  
        buttons.append({"title": "other location", 'payload': "/other_loc_date{\"other_location\":\"True\"}"})
        dispatcher.utter_button_message("Please select a button:", buttons)
        return [FollowupAction, ('action_listen')]
      else:
        dispatcher.utter_template('utter_ask_course_book',tracker)

  def locDistance(self, homecity, destination):
      # Install Module geopy
    from geopy.geocoders import Nominatim
    from geopy import distance

    geolocator = Nominatim(user_agent='myapplication')

    try:
        location = geolocator.geocode(homecity)
        sem_city = geolocator.geocode(destination)
        dis = distance.distance((sem_city.latitude, sem_city.longitude),
          (location.latitude,location.longitude)).km

    except:
        print(destination, "not found.")
        dis = float('inf')
    return dis


class ActionDateButtons(Action):

  def name(self):
    return "action_date_buttons"

  def run(self, dispatcher, tracker, domain):
    city = tracker.get_slot("location").capitalize()
    course = tracker.get_slot("course")

    if course:
      seminars = db.reference('seminars').get()
      seminar_id = matchingSeminar(seminars,course)
    else: 
      res = 'You need to specify a course for your request'
      dispatcher.utter_message(res)
      return[FollowupAction('action_course_offering')]

    if seminar_id is not None:
      seminar = seminars[seminar_id]
      if city in seminar["locations"]:

        #displaying top 2 dates with the fewest participant number
        date_occupancy = {}
        buttons = []

        for ele in seminar["locations"][city]:
          #do not display dates that are fully booked
          if date_check(seminar, city, ele["date"]):
            date_occupancy[ele["date"]] = ele["occupancy"]
        date_occupancy = sorted(date_occupancy.items(), key=lambda x: x[1])

        for x in list(date_occupancy)[0:2]: 
          buttons.append({"title": x[0], 'payload': '/inform{\"date\": \"' + x[0] + '\"}'})

        # if not satisfied with one of 2 suggested dates, user can ask for other dates
        buttons.append({'title': "other date", 'payload': '/other_loc_date{\"other_date\":\"True\"}'})
        dispatcher.utter_button_message("Please select a button:", buttons)
        return [FollowupAction, ('action_listen')]

      # If no location could be extracted, suggest next location
      else:
          res = "We do not offer {} seminars in {}.".format(course,city)
          next_loc = nextLocation(city,seminar)
          if next_loc:
            res += " But there is a seminar in {}.".format(next_loc)
            buttons=[{'title': 'Yes', 'payload': "/affirm}"},{'title': 'No', 'payload': '/negative'}]
            dispatcher.utter_message(res)
            dispatcher.utter_button_message("Do you agree with this location?", buttons)
            return [SlotSet("location",next_loc), FollowupAction('action_listen')]
          dispatcher.utter_message(res)


class ActionQueryOccupancy(Action):
  """Retrieves the number of slots available for a seminar"""

  def name(self):
      return "action_query_occupancy"

  def run(self, dispatcher, tracker, domain):

      course = tracker.get_slot('course')
      seminars = db.reference('seminars').get()
      city = tracker.get_slot('location')
      userGivenDate = tracker.get_slot('date')

      if course:
        seminar_id = matchingSeminar(seminars,course)
        seminar = seminars[seminar_id]
      else: 
        res = 'You need to specify a course for your request.'
        dispatcher.utter_message(res)
        return[FollowupAction('action_course_offering')]

      if seminar_id is not None:
        locs = sorted(seminar["locations"])
        occ_at_dates = {}
        capacity = seminar["capacity"]

        if city in locs:
          if userGivenDate:
            # If city and date given, only query occupancy at specified date
            for ele in seminar["locations"][city]:
              if dateComparison(ele["date"],userGivenDate) == 0:
                occupancy = capacity - ele["occupancy"]
                res = "{} slot(s) are left for grabs in {} on {}".format(occupancy, city, ele["date"]) 
          else:
            # If city but no date given, query occupancy at all dates 
            occ_at_dates = [(str(capacity - ele["occupancy"]) + " on " + ele["date"])
              for ele in seminar["locations"][city]]
            occ_at_dates = sorted(occ_at_dates, key=lambda x: datetime.strptime(x[-8:], '%d/%m/%y'))
            res = "This is how many slots are left for {} in {}:\n\n".format(course,city,)
            res += '\n'.join(occ_at_dates)
        else:
          for loc in locs:    
              occ_at_dates[loc] = [(capacity - ele["occupancy"])
                for ele in seminar["locations"][loc]]
          availableLocs = {k : sum(v) for (k,v) in occ_at_dates.items() if sum(v) > 0}
          res = "There are free slots left for {} in {}.".format(course,', '.join(k for k in availableLocs))

        dispatcher.utter_message(res)
        return []  
      else:
        res = "We don't offer {} seminars.".format(course)
        dispatcher.utter_message(res)
        return []        


class ActionDefaultAskAffirmation(Action):
  """ Prompts user affirmation when confidence score under certain threshold"""
  
  def name(self):
      return "action_default_ask_affirmation"

  def __init__(self):
      import pandas as pd

      self.intent_mappings = pd.read_csv("data/intent_description_mapping.csv", sep=';')
      self.intent_mappings.fillna("", inplace=True)
      self.intent_mappings.entities = self.intent_mappings.entities.map(
        lambda entities: {e.strip() for e in entities.split(',')})

      col_name = self.intent_mappings.columns[0]
      self.intent_mappings = self.intent_mappings.rename(columns = {col_name:'intent'})
      col_name = self.intent_mappings.columns[1]
      self.intent_mappings = self.intent_mappings.rename(columns = {col_name:'button'})
      col_name = self.intent_mappings.columns[2]
      self.intent_mappings = self.intent_mappings.rename(columns = {col_name:'entities'})

  def run(self, dispatcher, tracker, domain):
        # get the most likely intent
        last_intent_name = tracker.latest_message['intent']['name']
        
        if last_intent_name == None or last_intent_name == "None" or last_intent_name == "":
          res = "Oh! Its seems like I didn’t get that. Let’s try again or you can call at our Help desk +49621 66566."
          dispatcher.utter_message(res)
        else:
          intent_ranking = tracker.latest_message.get('intent_ranking', [])

        #display top 3 intents
          intent_ranking = intent_ranking[:3]
          first_intent_names = [intent.get('name', '')
                               for intent in intent_ranking
                               if intent.get('name', '') != 'out_of_scope']    
    
          message = ("Sorry, I'm not sure I've understood you correctly. Do you mean ... ")

          entities = tracker.latest_message.get("entities", [])
          entities = {e["entity"]: e["value"] for e in entities}

          entities_json = json.dumps(entities)

          buttons = []
          for intent in first_intent_names:
            buttons.append({'title': self.get_button_title(intent, entities),
                          'payload': '/{}{}'.format(intent, entities_json)})

          buttons.append({'title': 'Something else',
                        'payload': '/out_of_scope'})
          
          dispatcher.utter_button_message(message, buttons = buttons)

        return []

  def get_button_title(self, intent: Text, entities: Dict[Text, Text]
                         ) -> Text:
      default_utterance_query = self.intent_mappings.intent == intent
      utterance_query = (
                      (self.intent_mappings.entities == entities.keys()) &
                      default_utterance_query)

      utterances = self.intent_mappings[utterance_query].button.tolist()

      if len(utterances) > 0:
          button_title = utterances[0]
      else:
          utterances = (
              self.intent_mappings[default_utterance_query] 
                  .button.tolist())
          button_title = utterances[0] if len(utterances) > 0 else intent

      return button_title.format(**entities)


class ActionDefaultFallback(Action):  

  def name(self):
      return "action_default_fallback"

  def run(self,
          dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]
          ) -> List['Event']:

      # Fallback caused by TwoStageFallbackPolicy
      if (len(tracker.events) >= 4 and
              tracker.events[-4].get('name') ==
              'action_default_ask_affirmation'):

          dispatcher.utter_template('utter_restart_with_button', tracker)

          return []

      # Fallback caused by Core
      else:
          dispatcher.utter_template('utter_default', tracker)
          return [UserUtteranceReverted()]


class ActionShowAllButtons(Action):

  def name(self):
    return "action_show_all_buttons"

  def run(self, dispatcher, tracker, domain):

    course = tracker.get_slot('course')
    city = tracker.get_slot('location')
    otherLoc = tracker.get_slot('other_location')
    otherDate = tracker.get_slot('other_date')
    seminars = db.reference('seminars').get()

    if tracker.latest_message['intent'].get('name') == 'other_loc_date':
      seminar_id = matchingSeminar(seminars,course)
      seminar = seminars[seminar_id]
      buttons = []
      if seminar_id is not None:
        if otherLoc is not None:
          locs = sorted(seminar["locations"]) 
        # If user clicked on other locations, display all available locations 
          for loc in locs:
            if location_check(seminar, loc):
              buttons.append({'title': loc, 'payload': '/inform{"location": \"' + loc + '\"}'})
          if buttons:
            dispatcher.utter_button_message("These are all available locations.\
              Please select a button or type stop if none of these fits:", buttons)

        elif otherDate is not None:
          if city is not None:
            if city in seminar["locations"]:
            # If user clicked on other dates, display all dates
              for ele in seminar["locations"][city]:
                if date_check(seminar,city,ele["date"]):
                  buttons.append({'title': ele["date"], 'payload': '/inform{"date": \"' + ele["date"] + '\"}'})
            if buttons:  
              dispatcher.utter_button_message("These are all available dates.\
               Please select a button or type stop if none of these fits:", buttons)
      else:
        dispatcher.utter_template("utter_ask_course_book", tracker)

    return [FollowupAction('action_listen'),SlotSet("other_date", None),SlotSet("other_location",None)]
