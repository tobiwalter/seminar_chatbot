from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, FollowupAction
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk import ActionExecutionRejection
from helpers import matchingSeminar, dateComparison, period_check
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
cred = credentials.Certificate('C:\\Users\\Tobias\\Documents\\Uni Mannheim\\Team Project NLU\\service_account_key_thao.json')
# cred = credentials.Certificate('/Users/thaonguyen/Documents/Studium/Data Science/Teamprojekt/Seminar-b253e5498290.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seminar-b9c58.firebaseio.com/'
})      

seminarRef = db.reference('seminars')
countRef = db.reference('counts')
employeesRef = db.reference('employees')
employees = employeesRef.get()
seminars = seminarRef.get()
counts = countRef.get()

class ActionShowBookings(Action):

  def name(self):
    """returns name of the action """
    return "action_show_bookings"

  def run(self, dispatcher, tracker, domain):
    """ retrieves slot values """

    matchingID = tracker.get_slot('employee_id')
    date_period = tracker.get_slot('date-period')
    seminar_date = tracker.get_slot('date')
    time = tracker.get_slot('time')
    city = tracker.get_slot('location')
    bookingtype = tracker.get_slot('booking-type')
    display_option = tracker.get_slot('display-option')

  # Find booked seminars depending on params given
    if matchingID is not None:
      bookingRef = db.reference('bookings/' + str(matchingID))
      bookings = bookingRef.get()
      bookedSeminars = set([])
      semWithLocDate = set([])

      if bookings is not None:

        # Check for booking type and add seminars accordingly
        if bookingtype == 'past':
            bookedSeminars = ["{} in {} on {}".format(ele["seminar_title"],ele["location"], ele["date"]) 
                  for ele in bookings if not "cancellation" in ele if \
                  dateComparison(ele["date"],strftime("%c")) == -1]

        elif bookingtype == 'upcoming':
            bookedSeminars = ["{} in {} on {}".format(ele["seminar_title"],ele["location"], ele["date"]) 
                  for ele in bookings if not "cancellation" in ele if \
                  dateComparison(ele["date"],strftime("%c")) == 1]

        else:
            semWithLocDate = ["{} in {} on {}".format(ele["seminar_title"],ele["location"], ele["date"]) 
                  for ele in bookings if not "cancellation" in ele]
            bookedSeminars = [ele["seminar_title"] for ele in bookings if not "cancellation" in ele]

        if len(bookedSeminars) != 0:
          if display_option == "next" or display_option == "upcoming":
            res = "This is your next seminar: " + self.showNextBooking(bookings)
          elif seminar_date:
            res = self.showBookingsOnGivenDate(seminar_date,matchingID, bookings)
          elif date_period:
            res = self.showBookingsWithinPeriod(date_period,time,matchingID, bookings)
          elif city:
            res = self.showBoookingsAtLocation(city,matchingID, bookings)
          else:
            bookedSeminars = '\n '.join(sorted(semWithLocDate))
            res = "These are your booked seminars: \n" + bookedSeminars

          dispatcher.utter_message(res)
          return [SlotSet("date", None),SlotSet("location",None), SlotSet("date-period",None), SlotSet("time",None)]

      else:
        dispatcher.utter_message("There are no recorded bookings for you.")
        return []

    else:
      dispatcher.utter_message("You are not in our database. Please contact HR.")
      return [SlotSet('user_verified', 'False')]

  def showNextBooking(self,bookings):

    # Initialise date of next booking with first date in the list of booked seminars and iterate through all dates
          
    for i in range(len(bookings)):
        temp = bookings[i]["date"]
        dateNext = dateparser.parse(temp,settings={'DATE_ORDER': 'DMY'}).date()
        break
    # compare successive dates 
    for i in range(1,len(bookings)):
        temp = bookings[i]["date"]
        if dateComparison(temp,dateNext) == -1:
            dateNext = dateparser.parse(temp,settings={'DATE_ORDER': 'DMY'}).date()
            num = i

    return "{} on {} in {}.".format(bookings[num]["seminar_title"],bookings[num]["date"],
      bookings[num]["location"])


  def showBookingsOnGivenDate(self, seminar_date,matchingID, bookings):

    userGivenDate = dateparser.parse(seminar_date,settings={'DATE_ORDER': 'DMY'}).date()

    matchedSeminars = ["{} in {}".format(ele["seminar_title"],ele["location"]) for ele in bookings 
      if not 'cancellation' in ele \
      if dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() == userGivenDate]

    if len(matchedSeminars) != 0:
      return "Your booked seminars on {} : {}.".format(userGivenDate.strftime("%d.%m.%y"),', '.join(matchedSeminars))
    else:
      return "There are no recorded bookings for you on the specified date."

  def showBookingsWithinPeriod(self,date_period, time, matchingID, bookings):

    # Check if temporal expression extracted by duckling is an interval, i.e. has a "from" and "two" value
    if isinstance(time, dict):
      start = dateparser.parse(time["from"]).date()
      end = dateparser.parse(time["to"]).date()  
    #   If bookings between start and end, add them to the list of matched seminars
      matchedSeminars = ["{} at {} in {}".format(ele["seminar_title"],ele["date"],ele["location"]) for ele in bookings 
        if start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end]

    # If duckling extracted only a day, set this day as start and try to infer the lenght of the interval by 
    #  the value of the date period entity
    elif "week" in date_period.lower() or  "month" in date_period.lower() or "year" in date_period.lower():
      start = dateparser.parse(time,settings={'DATE_ORDER': 'DMY'}).date()
      if "week" or "Week" in date_period:
        end = start + relativedelta(days = 7)
      elif "month" or "Month" in date_period:
        end = start + relativedelta(day=31)
      elif "year" or "Year" in date_period:
        end = start + relativedelta(day=365)

    # If bookings between start and end, add them to the list of matched seminars
      matchedSeminars = ["{} at {} in {}".format(ele["seminar_title"],ele["date"],ele["location"]) for ele in bookings 
        if start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end]

    # if booking is in requested month or season
    else:
      matchedSeminars = []
      for ele in bookings:
        if not "cancellation" in ele:
          if period_check(date_period, ele["date"]):
            matchedSeminars.append("{} at {} in {}".format(ele["seminar_title"],ele["date"],ele["location"]))

    if len(matchedSeminars) != 0:
      return "Your booked seminars for {}: \n{}".format(date_period.capitalize(), "\n".join(matchedSeminars))
      # return "Your booked seminars between {} and {}: {}".format(start.strftime("%d.%m.%y"), 
      #   end.strftime("%d.%m.%Y"), ' ,'.join(matchedSeminars))
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
  def name(self):
    """returns name of the action """
    return "action_book_seminar"

  def run(self, dispatcher, tracker, domain):
    
    """ retrieves slot values """
    matchingID = tracker.get_slot('employee_id')
    course = tracker.get_slot('course')
    city = tracker.get_slot('location')
    userGivenDate = tracker.get_slot('date')
    time = tracker.get_slot('time')

    """ retrieves data snapshots """
    if matchingID is not None:
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
        return [SlotSet("booking_confirmed","False")]

      #  In case necessary slots were not filled previously, ask user to fill them
      if not city:
        dispatcher.utter_template('utter_ask_location', tracker)
        return [SlotSet("booking_confirmed","False")]

      #check if course is offered at user-given location
      seminar = seminars[seminar_id]
      if not city.capitalize() in seminar["locations"]:
        res = "The seminar {} is not offered in {}.".format(seminar["title"],city.capitalize())
        dispatcher.utter_message(res)
        return [SlotSet("booking_confirmed","False"),SlotSet("location", None), SlotSet("date", None)]

      #check if course is offered at user-given date
      if not (userGivenDate or time):
        dispatcher.utter_template('utter_ask_date', tracker)
        return [SlotSet("booking_confirmed","False")]
      else: 
        dateMatch = None
        seminarDates = seminar["locations"][city.capitalize()]
        for ele in seminarDates:
          semdate = ele["date"]
          if userGivenDate:
            if dateparser.parse(userGivenDate,settings={'DATE_ORDER': 'DMY'}).date() == \
            dateparser.parse(semdate,settings={'DATE_ORDER': 'DMY'}).date():
            # or dateComparison(time, semdate) == 0:
              dateMatch = ele
              userGivenDate = str(semdate)
              break
          elif time:
            if dateparser.parse(time).date() == dateparser.parse(semdate,
              settings={'DATE_ORDER': 'DMY'}).date():
              dateMatch = ele
              userGivenDate = str(semdate)
              break

      if dateMatch is None:
        dispatcher.utter_message("The seminar {} is not offered on {}".format(seminar["title"],
        dateparser.parse(time).date()))
        return [SlotSet("booking_confirmed", "False"),SlotSet("date", None)]

      #check if spot still available at given date and location      
      if seminar["capacity"] == dateMatch["occupancy"]:
        dispatcher.utter_message("All seminars about {} are booked out.".format(course))
        return [SlotSet("booking_confirmed","False"),SlotSet("date", None),SlotSet("location",None)]
      else:
        #check if seminar already booked by user 
        if bookings is not None:
          for ele in bookings:
            if not "cancellation" in ele:
              if ele["seminar_id"] == seminar_id and \
              dateparser.parse(ele["date"],settings={'DATE_ORDER': 'DMY'}).date() > date.today():
                res = "You have already booked the seminar {} in {} on {}.".format(course,ele["location"],ele["date"])
                dispatcher.utter_message(res)
                return [SlotSet("booking_confirmed","False"), SlotSet("date", None),SlotSet("location",None),
                SlotSet("course",None)]

        #If not booked, perform booking from here on: First, update occupancy
        occupancy = dateMatch["occupancy"]
        occupancy += 1  
        occupancyRef = seminarRef.child("{}/locations/{}/{}".format(str(seminar_id),city.capitalize(),str(seminarDates.index(dateMatch)))).update({"occupancy": occupancy})

        #Update booking count of matching employee
        countRef.update({str(matchingID): counts+1})

        #Write to DB
        booking_count = len(bookings) + 1 if bookings is not None else 1
        bookingRef.update({
          str(booking_count -1): {
          'date': userGivenDate ,
          'location': city.capitalize(),
          'seminar_id' : seminar_id,
          'seminar_title': seminar["title"]
          }})
        res = "Your booking request for the seminar {} in {} on {} has been forwarded. You will receive a confirmation via email.".format(course.capitalize(),city.capitalize(),userGivenDate)
        dispatcher.utter_message(res)
        
        #check for date clashes
        breaker = True
        res = "You have another seminar on the same day:"
        if bookings is not None:
            for ele in bookings: #ignoring recent booking entry
              if not "cancellation" in ele:
                if ele["date"] == userGivenDate : 
                  res += "\n{} in {} on {}.".format(ele["seminar_title"],ele["location"],ele["date"])
                  breaker = False
            if breaker:
              return [SlotSet("booking_confirmed","True"),SlotSet("date", None),SlotSet("location",None),
              SlotSet("course",None), FollowupAction('action_listen')]
            else:
              buttons=[{'title': 'Yes', 'payload': '/cancel_seminar'},{'title': 'No', 'payload': '/negative'}]
              dispatcher.utter_message(res)
              dispatcher.utter_button_message("Do you want to cancel one seminar?", buttons)
              return [SlotSet("booking_confirmed","True"), SlotSet("location",None),SlotSet("course",None)]
    else:
        dispatcher.utter_message("You are not in our database. Please contact HR.")
        return [SlotSet('user_verified', 'False'), SlotSet("booking_confirmed","False"), SlotSet("date", None),
        SlotSet("location",None), FollowupAction('utter_suggest_help')]
                    
class ActionCancelSeminar(Action):
  def name(self):
    """returns name of the action """
    return "action_cancel_seminar"

  def run(self, dispatcher, tracker, domain):
    """ retrieves slot values """
    matchingID = tracker.get_slot('employee_id')
    course = tracker.get_slot('course')
    city = tracker.get_slot('location')
    seminar_date = tracker.get_slot('date')
    date_period = tracker.get_slot('date-period')
    time = tracker.get_slot('time')

    if matchingID is not None:  
      """ retrieves data snapshots """
      bookingRef = db.reference('bookings/' + str(matchingID))
      bookings = bookingRef.get()

    # matching seminar ID
      if course is None:
        if city or seminar_date:
          dispatcher.utter_template('utter_ask_course_cancel', tracker)
          return [FollowupAction('action_show_bookings')]
        else: 
          dispatcher.utter_message("There is no seminar matching your request.")
          return [SlotSet("cancellation_confirmed","False"), SlotSet("course",None), SlotSet("location",None), SlotSet("date",None)]
      else: 
        seminar_id = matchingSeminar(seminars,course)
        
        if seminar_id is None:
          dispatcher.utter_message("There is no seminar matching your request.")
          return [SlotSet("cancellation_confirmed","False"), SlotSet("course",None), SlotSet("location",None), SlotSet("date",None)]

        #search for corresponding booking
        if bookings is None:
          dispatcher.utter_message("We do not have bookings for you in our database.")
          return []
        else:
          for ele in bookings:
            # ignore cancelled bookings
            if not "cancellation" in ele:
              if ele["seminar_id"]== seminar_id and dateparser.parse(ele["date"],
                settings={'DATE_ORDER': 'DMY'}).date() > date.today():

                dateEqual = True
                locEqual  = True

                #check date in case user defined date or period
                if seminar_date is not None:
                  dateEqual = (dateparser.parse(seminar_date,settings={'DATE_ORDER': 'DMY'}).date() 
                    == dateparser.parse(ele["date"],settings={'DATE_ORDER': 'DMY'}).date())

                elif date_period is not None:
                  # Check if temporal expression extracted by duckling is an interval, i.e. has a "from" and "two" value
                  if isinstance(time, dict):
                    start = dateparser.parse(time["from"]).date()
                    end = dateparser.parse(time["to"]).date()  

                    dateEqual = (start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end)

                  elif "week" in date_period.lower() or  "month" in date_period.lower() or "year" in date_period.lower():
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
                if city is not None:
                  locEqual = city.lower() == ele["location"].lower() 

                if dateEqual and locEqual:
                  #cancel booking by deleting entries
                  seminar_date = ele["date"]
                  city = ele["location"]
                  cancellation = "cancelled on " + str(date.today())
                  bookingRef.update({str(bookings.index(ele)): {'cancellation': cancellation}})

                #Update occupancy
                  try:
                    seminarDates = seminars[seminar_id]["locations"][city.capitalize()]
                    for ele in seminarDates:
                      semdate = ele["date"]
                      if dateparser.parse(seminar_date).date() == dateparser.parse(semdate).date():
                        dateMatch = ele
                        occupancy = ele["occupancy"]
                        occupancy -= 1
                        occupancyRef = seminarRef.child("{}/locations/{}/{}".format(str(seminar_id),
                                        city.capitalize(),str(seminarDates.index(dateMatch)))).update({"occupancy": occupancy})
                        break
                  except:
                    print('Seminar date is not in the database. No occupancy update!')
                
                  res = "Your seminar booking for {} on {} in {} has been cancelled. \n \
                  You will receive a cancellation confirmation.".format(course, seminar_date, city)
                  dispatcher.utter_message(res)
                  return [SlotSet("cancellation_confirmed","True"), SlotSet("course",None), SlotSet("location",None), SlotSet("date",None)]

        # bot message if cancellation was not successful      
        dispatcher.utter_message("There are no bookings according to your request or the requested booking \
                                    is already past and cannot be cancelled anymore.")
        return  [SlotSet("cancellation_confirmed","False"), SlotSet("course",None), SlotSet("location",None), SlotSet("date",None)]

    # no employee ID --> User Verification was not successful
    else:
      dispatcher.utter_message("You are not in the database. Please contact HR.")
      return [SlotSet("cancellation_confirmed","False")]

class ActionProvideDescription(Action):
  def name(self):
    """returns name of the action """
    return "action_provide_description"

  def run(self, dispatcher, tracker, domain):
    """ retrieves slot values """
    course = tracker.get_slot('course')
    seminar_id = matchingSeminar(seminars,course)

    if seminar_id is not None:
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

  def name(self):
    """returns name of the action """
    return "action_display_seminar"

  def run(self, dispatcher, tracker, domain):
    """ retrieves slot values """
    course = tracker.get_slot('course')
    city = tracker.get_slot('location')
    date_period = tracker.get_slot('date-period')
    time = tracker.get_slot('time')

    # If course entity could be extracted, check if corresponding seminar can be found
    if course is not None:
      seminar_id = matchingSeminar(seminars,course)

      # If seminar could be matched, display seminar dates and locations of only this seminar
      if seminar_id is not None:
        seminarRef = db.reference('seminars/' + str(seminar_id))
        seminar = seminarRef.get()

        locs = sorted(seminar["locations"])
        dates = {}

        for loc in locs:
          # Check if date-period was given by user
          if date_period is None:
            dates[loc] = [ele["date"] for ele in seminar["locations"][loc] 
            if ele["occupancy"] < seminar["capacity"]]

          # If date-period was given by user, only display dates in requested period
          else:
            
            if isinstance(time, dict):
              start = dateparser.parse(time["from"]).date()
              end = dateparser.parse(time["to"]).date()  

              dates[loc] = [ele["date"] for ele in seminar["locations"][loc] if ele["occupancy"] < seminar["capacity"] 
              if start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end]

            elif "week" in date_period.lower() or  "month" in date_period.lower() or "year" in date_period.lower():
              start = dateparser.parse(time,settings={'DATE_ORDER': 'DMY'}).date()
              if "week" or "Week" in date_period:
                end = start + relativedelta(days = 7)
              elif "month" or "Month" in date_period:
                end = start + relativedelta(day=31)
              elif "year" or "Year" in date_period:
                end = start + relativedelta(day=365)

              dates[loc] = [ele["date"] for ele in seminar["locations"][loc] if ele["occupancy"] < seminar["capacity"] 
              if start <= dateparser.parse(ele["date"], settings={'DATE_ORDER': 'DMY'}).date() <= end]    

            else:
              dates[loc] = [ele["date"] for ele in seminar["locations"][loc] if ele["occupancy"] < seminar["capacity"] 
              if period_check(date_period, ele["date"])]

          if len(dates[loc]) > 0:
            dates[loc] = sorted(dates[loc], key=lambda x: datetime.strptime(x, '%d/%m/%y'))
        #do not display locations that are fully booked for all dates
        dates = dict( [(k,v) for k,v in dates.items() if len(v)>0])

        if dates:
          res = "The seminar {} is offered at the following locations and dates:\n\n".format(seminar["title"])
          res += '\n'.join(["{:10}: {:<10}".format(key, ', '.join(value)) for key, value in dates.items()])
          dispatcher.utter_message(res)
          return [SlotSet("locations", locs),SlotSet("title", seminar["title"]),SlotSet("seminar_id", seminar_id),
          SlotSet('time', None)] 
        else:
          res = "There are no booking dates available for the seminar {}".format(seminar["title"])
          dispatcher.utter_message(res)
          return[SlotSet('date-period', None), SlotSet('time', None)]
      else:
        res = "We don't offer {} seminars.".format(course)
        dispatcher.utter_message(res)
        return []

    elif city is not None:
      available_seminars = [ele["category"] for ele in seminars if city.capitalize() in ele["locations"]]
          
      if len(available_seminars) != 0:
        res = "We offer seminars in the following categories in {} :\n{}".format(
                                  city.capitalize(), ', '.join(available_seminars))
        dispatcher.utter_message(res)
        return [SlotSet('categories', available_seminars)]
      else: 
        dispatcher.utter_message("There are no seminars offered in {}".format(city))
        return [SlotSet('location', None)]

    elif date_period is not None:
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
          seminar = "{} in {}".format(sem["category"],", ".join(cities))
          available_seminars.append(seminar)

      elif "week" in date_period.lower() or  "month" in date_period.lower() or "year" in date_period.lower():
        start = dateparser.parse(time,settings={'DATE_ORDER': 'DMY'}).date()
        if "week" or "Week" in date_period:
          end = start + relativedelta(days = 7)
        elif "month" or "Month" in date_period:
          end = start + relativedelta(day=31)
        elif "year" or "Year" in date_period:
          end = start + relativedelta(day=365)

        for sem in seminars:
          cities = []
          for loc in sem["locations"]:
            for ele in sem["locations"][loc]:
              if start <= dateparser.parse(ele["date"],settings={'DATE_ORDER': 'DMY'}).date() <= end:
                cities.append(loc)
                break
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
          seminar = sem["category"] + " in {}".format(", ".join(cities))
          available_seminars.append(seminar)

      if len(available_seminars) != 0:
        res = "We offer the following seminars in the specified period:\n{}".format(
          '\n'.join(available_seminars))
        dispatcher.utter_message(res)
        return [SlotSet('categories', available_seminars)]
      else: 
        dispatcher.utter_message("There are no seminars offered in the given period.")
        return []
    else: 
      dispatcher.utter_message("We do not offer courses in the category you specified.")
      return []

class ActionCourseOffering(Action):

  def name(self):
    """returns name of the action """
    return "action_course_offering"

  def run(self, dispatcher, tracker, domain):

    intent = tracker.latest_message['intent'].get('name')

    if intent == 'get_course_offering':
      cats = {ele["category"] for ele in seminars}
      res = "We offer seminars in the following categories: \n\n" + ", ".join(cats)
      dispatcher.utter_message(res)
      return []

      ## TO-DO: add intent to domain file and training data to NLU/core
    elif intent == 'get_course_offering_with_locations':
      cities = {loc for sem in seminars for loc in sem["locations"]}
      res = "We offer seminars in the following cities: \n\n" + ", ".join(cities)
      dispatcher.utter_message(res)
      return [] 

class ActionQueryDate(Action):
    def name(self):
        """returns name of the action """
        return "action_query_date"

    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot("location").capitalize()
        course = tracker.get_slot("course")

        seminar_id = matchingSeminar(seminars,course)

        if seminar_id is not None:
            seminar = seminars[seminar_id]

        # Collect dates of seminar in the corresponding city
            if city in seminar["locations"]:
              dates = [ele["date"] for ele in seminar["locations"][city]]

              dates = sorted(dates, key=lambda x: datetime.strptime(x, '%d/%m/%y'))
              res = "In {} the seminar takes place on those dates: \n{}".format(city, ", ".join(dates))
              dispatcher.utter_message(res)
              return [SlotSet("dates", ', '.join(dates)), SlotSet("title", seminar["title"],
                SlotSet('time', None))]

            # Suggest closest seminar location if seminar not held in specified city 
            else:
                res = "The seminar {} is not offered in {}.".format(seminar["title"],city)
                next_loc = self.nextLocation(city,seminar_id)
                if next_loc:
                    res += "But there is a seminar in {}.".format(next_loc)

                    buttons=[{'title': 'Yes', 'payload': "/affirm}"},{'title': 'No', 'payload': '/negative'}]
                    dispatcher.utter_message(res)
                    dispatcher.utter_button_message("Do you agree with this location?", buttons)
                    return [SlotSet("location",next_loc)]
                else:
                    dispatcher.utter_message(res)
                    return []

    def nextLocation(self, city, seminar_id):
    # Install Module geopy
        from geopy.geocoders import Nominatim
        from geopy import distance

        geolocator = Nominatim(user_agent='myapplication')
        loc_coordinates = []
        loc_distance = {}
        location = geolocator.geocode(city)

         #calculate distance between user's preferred location and seminar locations
        for loc in seminars[seminar_id]["locations"]:
            sem_city = geolocator.geocode(loc)
            loc_coordinates.append((sem_city.latitude, sem_city.longitude))
            loc_distance[loc] = distance.distance((sem_city.latitude, sem_city.longitude),(location.latitude,location.longitude))

        next_loc = min(loc_distance.keys(), key=(lambda k: loc_distance[k]))

        return next_loc

class ActionProvidePrerequisites(Action):
  def name(self):
    """returns name of the action """
    return "action_provide_prerequisites"

  def run(self, dispatcher, tracker, domain):
    """ retrieves slot values """

    course = tracker.get_slot('course')
    prqs = set()
    seminar_id = matchingSeminar(seminars,course)
    
    if seminar_id is not None:
      prqs = seminars[seminar_id]["prerequisites"]
        
    if prqs == "none":
          dispatcher.utter_message("There are no prerequisites.")
          return []
    else:
          dispatcher.utter_message("The prerequisites are {}.".format(", ".join(prqs)))
          return []
  
class ActionQueryLevel(Action):
  def name(self):
    """returns name of the action """
    return "action_query_level"

  def run(self, dispatcher, tracker, domain):
    course = tracker.get_slot('course')

    seminar_id = matchingSeminar(seminars,course)
    if seminar_id is not None:
        level = seminars[seminar_id]["level"]
        dispatcher.utter_message("This is the level of the course: {}".format(level))
        return []
    else:
      dispatcher.utter_message("The level is not specified.")
      return []

class VerifyUser(Action):
  def name(self):
    """returns name of the action """
    return "action_verify_user"

  def run(self, dispatcher, tracker, domain):
    """ retrieves slot values """
    firstname = tracker.get_slot('given-name')
    lastname = tracker.get_slot('last-name')
    
    # Find matching employee identifier
    for e in employees:
      if e["First_name"].lower() == firstname.lower():
        if e["Last_name"].lower() == lastname.lower():
          dispatcher.utter_message("Hello {}.".format(firstname.capitalize()))
          return [SlotSet("user_verified","True"), SlotSet("employee_id",e["employee_id"])]

    dispatcher.utter_template('utter_try_again', tracker)
    return []

class ActionQueryDuration(Action):
  def name(self):
    """returns name of the action """
    return "action_query_duration"

  def run(self, dispatcher, tracker, domain):
    course = tracker.get_slot('course')

    seminar_id = matchingSeminar(seminars,course)
    if seminar_id is not None:
        duration = seminars[seminar_id]["duration (days)"]
        if duration == 1:
          res = "The seminar is scheduled over one day from 9 am to 5 pm.".format(duration)
        elif duration > 1:
          res = "The seminar is scheduled over {} days from 9 am to 5 pm.".format(duration)
        dispatcher.utter_message(res)
        return []
    else:
      dispatcher.utter_message("The duration could not be retrieved.")
      return []

class SeminarForm(FormAction):
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
    return {"date": [self.from_entity(entity="date", intent= ["book_seminar","inform"]),
        self.from_entity(entity="time", intent=["book_seminar", "inform"])],
        "location": self.from_entity(entity="location", intent= ["book_seminar","inform"])}
   
  @staticmethod 
  def is_date(val):
    isDate = False
    if isinstance(val, str):
      if isinstance(dateparser.parse(val),datetime):
        isDate = True
        return isDate
       
  @staticmethod         
  def loc_in_database(val,tracker):
    seminar_id = tracker.get_slot("seminar_id")
    seminar = seminars[seminar_id]
    if val.capitalize() in seminar["locations"].keys():
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
        if not self.is_date(value):
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
        """returns name of the action """
        return "action_location_buttons"

    def run(self, dispatcher, tracker, domain):

        course = tracker.get_slot('course')
        seminars = db.reference('seminars').get()
        seminar_id = matchingSeminar(seminars,course)

        if seminar_id is not None:
          if tracker.get_slot("locations"):
            locations = tracker.get_slot("locations")      
          else:
            return [FollowupAction('action_listen')] 


          if tracker.latest_message['intent'].get('name') == 'other_loc_date':
            buttons = [{'title': loc, 'payload': '/inform{"location": \"' + loc + '\"}'} for loc in locations]
            dispatcher.utter_button_message("Please select a button:", buttons)
            return []
          else:
            seminar = seminars[seminar_id]
            # locations = seminar.get("locations")

            loc_occupancy = {}
            buttons = []

            employee_id = tracker.get_slot("employee_id")
            home_city = employees[employee_id]["location"]

            for loc in locations:
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

            # primary, display locations with occupancy < 70% and sort by distance
            # then display locations with occupancy > 70 % and sort by average occupancy
            sort_by_dis = {}
            sort_by_occ = {}

            for l in list(loc_occupancy):
                if loc_occupancy[l][1] < float('inf'):
                   sort_by_dis[l] = loc_occupancy[l][1]
                else:
                   sort_by_occ[l] = loc_occupancy[l][1]

            loc_buttons = sorted(sort_by_dis.items(), key=lambda x: x[1])
            loc_buttons += sorted(sort_by_occ.items(), key=lambda x: x[1])

            #displaying top 3 locations
            for x in list(loc_buttons)[0:3]:
              buttons.append({'title': x[0], 'payload': '/inform{"location": \"' + x[0].capitalize() + '\"}'})

            buttons.append({'title': "other location", 'payload': "/other_loc_date"})
            dispatcher.utter_button_message("Please select a button:", buttons)
            return []

    def locDistance(self, homecity, destination):
        # Install Module geopy
      from geopy.geocoders import Nominatim
      from geopy import distance

      geolocator = Nominatim(user_agent='myapplication')

      try:
          location = geolocator.geocode(homecity)
          sem_city = geolocator.geocode(destination)
          dis = distance.distance((sem_city.latitude, sem_city.longitude),(location.latitude,location.longitude)).km

      except:
          print(destination, "not found.")
          dis = float('inf')
      return dis

class ActionDateButtons(Action):

  def name(self):
    """returns name of the action """
    return "action_date_buttons"

  def run(self, dispatcher, tracker, domain):
    seminars = db.reference('seminars').get()
    city = tracker.get_slot("location").capitalize()
    course = tracker.get_slot("course")

    seminars = db.reference('seminars').get()
    seminar_id = matchingSeminar(seminars,course)

    if seminar_id is not None:
      seminar = seminars[seminar_id]
      if city in seminar["locations"]:

        if tracker.latest_message['intent'].get('name') == 'other_loc_date':
          buttons = [{'title': loc, 'payload': '/inform{"date": \"' + loc + '\"}'} for ele["date"] in seminar["locations"][city]]
        else:
          #displaying top 2 dates with the fewest participant number
          date_occupancy = {}
          buttons = []

          for ele in seminar["locations"][city]:
            occ = ele["occupancy"]
            date = ele["date"]
          #do not display dates that are fully booked
            if occ < seminar["capacity"]:
              date_occupancy[date] = occ

          date_occupancy = sorted(date_occupancy.items(), key=lambda x: x[1])
          for x in list(date_occupancy)[0:2]: 
            buttons.append({'title': x[0], 'payload': '/inform{"date": \"' + x[0] + '\"}'})

          buttons.append({'title': "other date", 'payload': "/other_loc_date"})
      
          dispatcher.utter_button_message("Please select a button:", buttons)
          return []