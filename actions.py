from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, FollowupAction
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk import ActionExecutionRejection
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import dateparser
import pytz
import locale
import json

# =============================================================================
# Initialize Firebase database instance
# =============================================================================

# Fetch the service account key JSON file contents
# cred = credentials.Certificate('C:\\Users\\Tobias\\Documents\\Uni Mannheim\\Team Project NLU\\service_account_key_thao.json')
cred = credentials.Certificate('/Users/thaonguyen/Documents/Studium/Data Science/Teamprojekt/Seminar-b253e5498290.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
	'databaseURL': 'https://seminar-b9c58.firebaseio.com/'
})

seminarRef = db.reference('seminars')
countRef = db.reference('counts')
bookingRef = db.reference('bookings')
employeesRef = db.reference('employees')
employees = employeesRef.get()
bookings = bookingRef.get()
seminars = seminarRef.get()
counts = countRef.get()
#locale.setlocale(locale.LC_ALL, 'deu_deu')

class ActionShowBookings(Action):

	def name(self):
		"""returns name of the action """
		return "action_show_bookings"

	def run(self, dispatcher, tracker, domain):
		""" retrieves slot values """

		matchingID = tracker.get_slot('employee_id')
		date_period = tracker.get_slot('date-period')
		seminar_date = tracker.get_slot('date')
		city = tracker.get_slot('location')
		bookingtype = tracker.get_slot('booking-type')
		display_option = tracker.get_slot('display-option')
		time = tracker.get_slot('time')

	#    Find booked seminars depending on params given
		if 'matchingID' in locals():
			# global bookingRef  #= db.reference('bookings')
			# global bookings ##= bookingRef.get()
			bookedSeminars = set([])

	#   Check for booking type and add seminars accordingly
			if bookingtype == 'past':
				for i in range(len(bookings)):
					if "cancellation" not in bookings[i]:
						if dateparser.parse(bookings[i]["date"]).date() < date.today():
							if bookings[i]["employee_id"] == matchingID:
								sem = bookings[i]["seminar_title"] + " on "
								+ bookings[i]["date"] + " in " + bookings[i]["location"]
								bookedSeminars.add(sem)
			elif bookingtype == 'upcoming':
				for i in range(len(bookings)):
					if "cancellation" not in bookings[i]:
						if dateparser.parse(bookings[i]["date"]).date() >= date.today():
							if  bookings[i]["employee_id"] == matchingID:
								sem = bookings[i]["seminar_title"] + " on " + bookings[i]["date"] + " in " + bookings[i]["location"]
								bookedSeminars.add(sem)
			else:
				for i in range(len(bookings)):
					if "cancellation" not in bookings[i]:
						if  bookings[i]["employee_id"] == matchingID:
							sem = bookings[i]["seminar_title"]
							bookedSeminars.add(sem)

			if len(bookedSeminars) != 0:
				if display_option == "next" or display_option == "upcoming":
					res = "This is your next seminar: " + self.showNextBooking(bookedSeminars)
				elif seminar_date:
					res = self.showBookingsOnGivenDate(seminar_date,bookedSeminars,matchingID)
				elif date_period:
					res = self.showBookingsWithinPeriod(date_period, time,bookedSeminars, matchingID)
				elif city:
					res = self.showBoookingsAtLocation(city,bookedSeminars,matchingID)
				else:
					bookedSeminars = ', '.join(bookedSeminars)
					res = "These are your booked seminars: " + bookedSeminars

				dispatcher.utter_message(res)
				return [SlotSet("date", None),SlotSet("location",None)]

			else:
				dispatcher.utter_message("There are no recorded bookings for you.")
				return []

		else:
			dispatcher.utter_message("You are not in our database. Please contact HR.")
			return [SlotSet('user_verified', 'False')]

	def showNextBooking(self,bookedSeminars):

		# Initialise date of next booking with first date in the list and iterate through all dates
		for i in range(len(bookings)):
			if "cancellation" not in bookings[i]:
				if bookings[i]["seminar_title"] in bookedSeminars:
					temp = bookings[i]["date"]
					dateNext = dateparser.parse(temp).date()
					break

		for i in range(1,len(bookings)):
			if "cancellation" not in bookings[i]:
				if bookings[i]["seminar_title"] in bookedSeminars:
					temp = bookings[i]["date"]
					if dateparser.parse(temp).date() <= dateNext:
						dateNext = dateparser.parse(temp).date()
						num = i

		return bookings[num]["seminar_title"]


	def showBookingsOnGivenDate(self,seminar_date,bookedSeminars,matchingID):

		given_date = dateparser.parse(seminar_date).date()
		matchedSeminars = set()

		for i in range(len(bookings)):
			if "cancellation" not in bookings[i]:
				if (bookings[i]["seminar_title"] in bookedSeminars and
				dateparser.parse(bookings[i]["date"]).date() == given_date and
				bookings[i]["employee_id"] == matchingID):

					sem = bookings[i]["seminar_title"]
					matchedSeminars.add(sem)

		if len(matchedSeminars) != 0:
			return "Your booked seminars on {} : {}.".format(given_date.strftime("%d.%m.%y"),', '.join(matchedSeminars))
		else:
			return "There are no recorded bookings for you on the specified date."

	def showBookingsWithinPeriod(self,date_period, time,bookedSeminars, matchingID):

		if isinstance(time, dict):
			start = dateparser.parse(time["from"]).date()
			end = dateparser.parse(time["to"]).date()
		else: 
			start = dateparser.parse(time)
			if "week" in date_period:
				end = start + relativedelta(days = 7)
			elif "month" in date_period:
				end = start + relativedelta(day=31)
			elif "year" in date_period:
				end = start + relativedelta(day=365)

	#   If bookings between start and end, add them to the list of matched seminars

		matchedSeminars = set()
		for i in range(len(bookings)):
			if "cancellation" not in bookings[i]:
				if (bookings[i]["seminar_title"] in bookedSeminars and
				start <= pytz.utc.localize(dateparser.parse(bookings[i]["date"],settings={'DATE_ORDER': 'DMY'})) <= end and
				bookings[i]["employee_id"] == matchingID):

					sem = bookings[i]["seminar_title"] + " on " + bookings[i]["date"]
					matchedSeminars.add(sem)

		if len(matchedSeminars) != 0:
			return "Your booked seminars between {} and {}: {}".format(start.strftime("%d.%m.%y"), end.strftime("%d.%m.%Y"), ' ,'.join(matchedSeminars))
		else:
			return "There are no recorded bookings for you within the specified period."

	def showBoookingsAtLocation(self,city, bookedSeminars, matchingID):

		matchedSeminars = set()
		for i in range(len(bookings)):
			if "cancellation" not in bookings[i]:
				if (bookings[i]["seminar_title"] in bookedSeminars and
				bookings[i]["location"].lower() == city.lower() and
				bookings[i]["employee_id"] == matchingID):

					sem = bookings[i]["seminar_title"] + " on " + bookings[i]["date"]
					matchedSeminars.add(sem)

		if len(matchedSeminars) != 0:
			return "Your booked seminars in {} : {}".format(city,', '.join(matchedSeminars))
		else:
			return "There are no recorded bookings for you in {}".format(city)

class ActionBookSeminar(Action):
	def name(self):
		"""returns name of the action """
		return "action_book_seminar"

	def run(self, dispatcher, tracker, domain):
		""" retrieves slot values """
		# countRef = db.reference('counts')
		# counts = countRef.get()
		# bookingRef = db.reference('bookings')
		# bookings = bookingRef.get()

		matchingID = tracker.get_slot('employee_id')
		course = tracker.get_slot('course')
		city = tracker.get_slot('location').capitalize()
		userGivenDate = tracker.get_slot('date')

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

		if "seminar_id" not in locals():
			res = "The seminar you requested is not being offered."
			dispatcher.utter_message(res)
			return [SlotSet("booking_confirmed","False")]

		if not city:
			dispatcher.utter_template('utter_ask_location', tracker)
			return [SlotSet("booking_confirmed","False")]

		if not userGivenDate:
			dispatcher.utter_template('utter_ask_date', tracker)
			return [SlotSet("booking_confirmed","False")]

		#check location
		seminar = seminars[seminar_id]
		if not city in seminar["locations"]:
			res = "The seminar {} is not offered in {}.".format(seminar["title"],city)
			dispatcher.utter_message(res)
			return [SlotSet("booking_confirmed","False"),SlotSet("location", None)]

		#check date
		dateMatch = False
		for d in seminar["locations"][city]:
			if dateparser.parse(userGivenDate).date() == dateparser.parse(d).date():
				dateMatch = True
				seminar_date = str(d)
				break

		if not dateMatch:
			dispatcher.utter_message("The seminar {} is not offered on {}".format(seminar["title"], userGivenDate))
			return [SlotSet("booking_confirmed", "False"),SlotSet("date", None),SlotSet("location",None)]

		#check occupancy    
		if seminar["capacity"] > seminar["occupancy"]:
			occupancy = seminar["occupancy"]

			#check if already booked
			for i in range(len(bookings)):
				if "cancellation" not in bookings[i]:
					if bookings[i]["employee_id"] == matchingID and bookings[i]["location"].lower() == city.lower() and bookings[i]["seminar_id"] == seminar_id: #could add OR --> check date against given seminar date
						res = "You have already booked the seminar {} in {} on {}.".format(course,city,bookings[i]["date"])
						dispatcher.utter_message(res)
						return [SlotSet("booking_confirmed","False"), SlotSet("date", None),SlotSet("location",None)]

			#Update occupancy
			seminarRef.child(str(seminar_id)).update({"occupancy": occupancy + 1})

			#Update bookingcount
			booking_count = len(bookings) + 1
			countRef.update({"booking_count": booking_count})

			#Write to DB
			bookingRef.update({
				str(booking_count-1): {
					'date': seminar_date,
					'employee_id': matchingID,
					'location': city,
					'seminar_id' : seminar_id,
					'seminar_title': seminar["title"]
				}})
			res = "Your booking request for the seminar {} in {} on {} has been forwarded. You will receive a confirmation via email.".format(course.capitalize(),city,seminar_date)
			dispatcher.utter_message(res)
			return [SlotSet("booking_confirmed","True"),SlotSet("date", None),SlotSet("location",None)]
		else:
			dispatcher.utter_message("All seminars about {} are booked out.".format(course))
			return [SlotSet("booking_confirmed","False"),SlotSet("date", None),SlotSet("location",None)]

			#TO BE DONE: date suggestion, capacity check

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

		if matchingID is None:
			dispatcher.utter_message("You are not in the database. Please contact HR.")
			return [SlotSet("cancellation_confirmed","False")]

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
			
		if 'seminar_id' not in locals():
			 dispatcher.utter_message("There is no seminar matching your request.")
			 return [SlotSet("cancellation_confirmed","False")]

		#search for corresponding booking
		breaker = False
		for j in range(len(bookings)):
			if "cancellation" not in bookings[j]:
				if bookings[j]["employee_id"] == matchingID and bookings[j]["seminar_id"]== seminar_id and dateparser.parse(bookings[j]["date"]).date() > date.today():
					breaker_1 = True
					breaker_2 = True

					#check date in case user defined date
					if seminar_date:
						breaker_1 = (dateparser.parse(seminar_date).date() == dateparser.parse(bookings[j]["date"]).date())

					#check location in case user defined location
					if city:
						breaker_2 = city.lower() == bookings[j]["location"].lower()

					breaker = breaker_1 and breaker_2

				if breaker:
					#cancel booking by deleting entries
					seminar_date = bookings[j]["date"]
					city = bookings[j]["location"]
					cancellation = "cancelled on " + str(date.today())
					bookingRef.update({
								str(j): {
									'cancellation': cancellation
								}})
#                    booking_count = len(bookings) - 1
#                    countRef.update({"booking_count": booking_count})
					occupancy = seminars[seminar_id]["occupancy"] - 1
#                    TO-DO!! Updating occupancy does not work yet 
					seminarRef.update({
					str(seminar_id) + '/occupancy': occupancy        
								})
					res = "Your seminar booking for " + course + " on " + seminar_date + " in " + city + " has been cancelled. You will receive a cancellation confirmation."
					dispatcher.utter_message(res)
					return [SlotSet("cancellation_confirmed","True")]

		dispatcher.utter_message("You don't have bookings according to your request.")
		return  [SlotSet("cancellation_confirmed","False")]

class ActionProvideDescription(Action):
<<<<<<< HEAD
	def name(self):
		"""returns name of the action """
		return "action_provide_description"

	def run(self, dispatcher, tracker, domain):
		""" retrieves slot values """

		course = tracker.get_slot('course')
		user_level = tracker.get_slot('user-level')

		for j in range(len(seminars)):
			breaker = False
			for k in range(len(seminars[j]["description"])):
				if seminars[j]["description"][k].lower() == course.lower():
					seminar_id = seminars[j]["seminar_id"]
					breaker = True
					break
			if breaker:
				break

		if "seminar_id" in locals():
			seminar = seminars[seminar_id]
			# res = "The seminar {} is described as follows: \n \
			# {} \n".format(seminar["title"], seminar["text"])
			# dispatcher.utter_message(res)
			attachment = json.dumps([{"fallback": seminar['text'], #only if client doesn't show formatted text
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
=======
    def name(self):
        """returns name of the action """
        return "action_provide_description"

    def run(self, dispatcher, tracker, domain):
        """ retrieves slot values """

        course = tracker.get_slot('course').strip()
        user_level = tracker.get_slot('user-level')

        for j in range(len(seminars)):
            breaker = False
            for k in range(len(seminars[j]["description"])):
                if seminars[j]["description"][k].lower() == course.lower():
                    seminar_id = seminars[j]["seminar_id"]
                    breaker = True
                    break
            if breaker:
                break

        if "seminar_id" in locals():
            seminar = seminars[seminar_id]
            # res = "The seminar {} is described as follows: \n \
            # {} \n".format(seminar["title"], seminar["text"])
            # dispatcher.utter_message(res)
            attachment = json.dumps([{"fallback": seminar['text'], #only if client doesn't show formatted text
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
>>>>>>> f28ac7ac680ad33e4dbd2802c4c485b7820a90aa

class ActionDisplaySeminar (Action):
	def name(self):
		"""returns name of the action """
		return "action_display_seminar"

	def run(self, dispatcher, tracker, domain):
		""" retrieves slot values """
		
## TO-DO: Implement scenario when user provides user-level variable 
<<<<<<< HEAD
		course = tracker.get_slot('course')

#        If course given, display locations and dates of seminar
		if course:
			for j in range(len(seminars)):
				breaker = False
				for k in range(len(seminars[j]["description"])):
					if seminars[j]["description"][k].lower() == course.lower():
						seminar_id = seminars[j]["seminar_id"]
						breaker = True
						break
				if breaker:
					break

			if "seminar_id" in locals():
				seminar = seminars[seminar_id]
				locs = seminar.get("locations")
				res = "The seminar {} is offered at the following locations and dates: \n \n".format(seminar["title"])
				res += '\n '.join(["{:10}: {:<10}".format(key, ', '.join(value)) for key, value in locs.items()])

				dispatcher.utter_message(res)
				return [SlotSet("locations", ', '.join(locs.keys())),
						SlotSet("title", seminar["title"]), SlotSet("seminar_id", seminar_id)]

			else:
				res = "We don't offer seminars in {}.".format(course)
				#  possible to call actionCourseOffering here?
				dispatcher.utter_message(res)
				return []
		else: 
			dispatcher.utter_message("I did not understand the course you specified")
			return []
	
=======
        course = tracker.get_slot('course')
        city = tracker.get_slot('location').capitalize()

        # If course given, display locations and dates of seminar
        if course:
            for j in range(len(seminars)):
                breaker = False
                for k in range(len(seminars[j]["description"])):
                    if seminars[j]["description"][k].lower() == course.lower():
                        seminar_id = seminars[j]["seminar_id"]
                        breaker = True
                        break
                if breaker:
                    break

            if "seminar_id" in locals():
                seminar = seminars[seminar_id]
                locs = seminar.get("locations")
                res = "The seminar {} is offered at the following locations and dates:\n\n".format(seminar["title"])
                res += '\n'.join(["{:10}: {:<10}".format(key, ', '.join(value)) for key, value in locs.items()])

                dispatcher.utter_message(res)
                return [SlotSet("locations", ', '.join(locs.keys())),
                        SlotSet("title", seminar["title"]), SlotSet("seminar_id", seminar_id)]

            else:
                res = "We don't offer {} seminars.".format(course)
                #  possible to call actionCourseOffering here?
                dispatcher.utter_message(res)
                return []

        elif city:
            available_seminars = []
            for j in range(len(seminars)):
              if city in seminars[j]["locations"]:
                available_seminars.append(seminars[j]["category"]) ## can also display available dates here

            if len(available_seminars) != 0:
              res = "We have seminars in the following categories in {} :\n{}".format(city, 
                                                  ', '.join(available_seminars))
              dispatcher.utter_message(res)
              return []
            else: 
              dispatcher.utter_message("There are no seminars offered in {}".format(city))
              return []
        else: 
            dispatcher.utter_message("We do not offer courses in the category you specified.")
            return []

>>>>>>> f28ac7ac680ad33e4dbd2802c4c485b7820a90aa
class ActionCourseOffering(Action):

	def name(self):
		"""returns name of the action """
		return "action_course_offering"

	def run(self, dispatcher, tracker, domain):
		""" retrieves slot values """
		cats = set()
		for j in range(len(seminars)):
			cats.add(seminars[j]["category"].capitalize())

		res = "We offer seminars in the following categories: \n\n" + ", ".join(cats)
		dispatcher.utter_message(res)
		return []

class ActionLocationButtons(Action):

	def name(self):
		"""returns name of the action """
		return "action_location_buttons"

	def run(self, dispatcher, tracker, domain):
		locations = tracker.get_slot('locations')
		buttons=[]

		if not locations:
			course = tracker.get_slot('course')

			for j in range(len(seminars)):
				breaker = False
				for k in range(len(seminars[j]["description"])):
					if seminars[j]["description"][k].lower() == course.lower():
						seminar_id = seminars[j]["seminar_id"]
						breaker = True
						break
				if breaker:
					break

				if "seminar_id" in locals():
					seminar = seminars[seminar_id]
					locations = seminar.get("locations")
		else:
			locations = locations.split(",")

		for loc in locations:
			loc = loc.strip()
			buttons.append({'title': loc, 'payload': "/inform{'location': " + loc.capitalize() + "}"})
		
		dispatcher.utter_button_message("", buttons)
		return []

class ActionDateButtons(Action):

	def name(self):
		"""returns name of the action """
		return "action_date_buttons"

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot("location").capitalize()
		course = tracker.get_slot("course")

		for j in range(len(seminars)):
			breaker = False
			for k in range(len(seminars[j]["description"])):
				if seminars[j]["description"][k].lower() == course.lower():
					seminar_id = seminars[j]["seminar_id"]
					breaker = True
					break
			if breaker:
				break

		if "seminar_id" in locals():
			seminar = seminars[seminar_id]

		if location in seminar["locations"]:
			dates = seminar["locations"][location]
		else:
			dates = []

		buttons=[]

		for d in dates:
			buttons.append({'title': d, 'payload': "/inform{'date': " + d + "}"})
		
		dispatcher.utter_button_message("", buttons)
		return []

class ActionQueryDate(Action):

	def name(self):
		"""returns name of the action """
		return "action_query_date"

	def run(self, dispatcher, tracker, domain):
		city = tracker.get_slot("location").capitalize()
		course = tracker.get_slot("course")

		for j in range(len(seminars)):
			breaker = False
			for k in range(len(seminars[j]["description"])):
				if seminars[j]["description"][k].lower() == course.lower():
					seminar_id = seminars[j]["seminar_id"]
					breaker = True
					break
			if breaker:
				break

		if "seminar_id" in locals():
			seminar = seminars[seminar_id]

		# Collect dates of seminar in the corresponding city
		if city in seminar["locations"]:
			dates = seminar["locations"][city]
			res = "In {} the seminar takes place on those dates: {}".format(city, ", ".join(dates))
			dispatcher.utter_message(res)
			return [SlotSet("dates", ', '.join(dates)), SlotSet("title", seminar["title"])]

		# Suggest closest seminar location if seminar not held in specified city 
		else:
			res = "The seminar {} is not offered in {}.".format(seminar["title"],city)
			next_loc = self.nextLocation(city,seminar_id)
			if next_loc:
				res += " But there is a seminar in {}. Do you agree with this location?".format(next_loc)

			buttons=[{'title': 'Yes', 'payload': "/bye}"},{'title': 'No', 'payload': '/negative'}]
			dispatcher.utter_message(res)
			dispatcher.utter_button_message("Do you agree with this location?", buttons)
			return [SlotSet("location",next_loc)]

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
		for j in range(len(seminars)):
			breaker = False
			if course.lower() in (d.lower() for d in seminars[j]["description"]):
				if seminars[j]["prerequisites"] == "none":
					dispatcher.utter_message("There are no prerequisites.")
					return []
				else:
					for k in range(len(seminars[j]["prerequisites"])):
						prqs.add(seminars[j]["prerequisites"][k])
						breaker = True
			if breaker:
				break
		dispatcher.utter_message(", ".join(prqs))
		return []
	
class ActionQueryLevel(Action):
	def name(self):
		"""returns name of the action """
		return "action_query_level"

	def run(self, dispatcher, tracker, domain):
		course = tracker.get_slot('course')
		
		for j in range(len(seminars)):
			if course.lower() in (d.lower() for d in seminars[j]["description"]):
				level = seminars[j]["level"]
				dispatcher.utter_message("This is the level of the course: {}".format(level))
				return []
		
		#Message given back to user if no level is specified 
		dispatcher.utter_message("The level is not specified.")
		return []


class VerifyUser(Action):
	def name(self):
		"""returns name of the action """
		return "action_verify_user"

	def run(self, dispatcher, tracker, domain):
		""" retrieves slot values """
#        If bot performs user verification twice, silently return nothing
		if tracker.get_slot("employee_id"):
			return []

		firstname = tracker.get_slot('given-name')
		lastname = tracker.get_slot('last-name')
		
		# Find matching employee identifier
		for i in range(len(employees)):
			if employees[i]["First_name"].lower() == firstname.lower():
				if employees[i]["Last_name"].lower() == lastname.lower():
					dispatcher.utter_message("Hello {}.".format(firstname.capitalize()))
					return [SlotSet("user_verified","True"), SlotSet("employee_id",employees[i]["employee_id"])]

		dispatcher.utter_template('utter_try_again', tracker)
		return []

class SeminarForm(FormAction):
	RANDOMIZE = False

	def name(self):
		return "seminar_form"

	@staticmethod
	def required_slots(tracker):
	   
		if tracker.get_slot('time'):
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
		return []
