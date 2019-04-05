import dateparser
from datetime import date, datetime

#Helper functions that are needed in actions module

SETTINGS = "{'DATE_ORDER': 'DMY'}"

def matchingSeminar(seminars,course) -> int:

		for ele in seminars:
			if course.lower() in (d.lower() for d in ele["description"]):
				seminar_id = int(ele["seminar_id"])
				return seminar_id 

def dateComparison(date1, date2) -> int:

		if isinstance(date1, date):
			if isinstance(date2, date):
				if date1 == date2: return 0
				elif date1 < date2: return -1
				else: return 1

			else:	
				if date1 == dateparser.parse(date2,settings={'DATE_ORDER': 'DMY'}).date():
				 return 0
				elif date1 < dateparser.parse(date2,settings={'DATE_ORDER': 'DMY'}).date():
					 return -1
				else: return 1 

		elif isinstance(date2, date):
			if dateparser.parse(date1,settings={'DATE_ORDER': 'DMY'}).date() == date2:
			 return 0
			elif dateparser.parse(date1,settings={'DATE_ORDER': 'DMY'}).date() < date2:
				 return -1
			else: return 1 

		else:
			if dateparser.parse(date1,settings={'DATE_ORDER': 'DMY'}).date() == \
					dateparser.parse(date2,settings={'DATE_ORDER': 'DMY'}).date():
					return 0
			elif dateparser.parse(date1,settings={'DATE_ORDER': 'DMY'}).date() < \
					dateparser.parse(date2,settings={'DATE_ORDER': 'DMY'}).date():
					return -1
			else: return 1

def period_check(date_period, date_time):
    from datetime import datetime
    month = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    season = {
        "spring": [3,4,5],
        "summer": [6,7,8],
        "autumn": [9,10,11],
        "winter": [12,1,2]
    }

    date_time = datetime.strptime(date_time, '%d/%m/%y')

    if date_period.lower() in season:
      if date_time.month in season.get(date_period.lower()):
        return True
      else:
        return False
    elif date_period.capitalize() in month:
      if date_time.month == month.get(date_period.capitalize()):
        return True
      else:
        return False
    else:
      return False

def location_check(seminar, location):
    occ = 0
    count = 0
    for ele in seminar["locations"][location]:
        occ += ele["occupancy"]
        count += 1
    if occ < count*seminar["capacity"]:
        return True
    else:
        return False

def date_check(seminar, location, date):
    for i in range(len(seminar["locations"][location])):
        if seminar["locations"][location][i]["date"] == date:
            occ = seminar["locations"][location][i]["occupancy"]

    if occ < seminar["capacity"]:
        return True
    else:
        return False

