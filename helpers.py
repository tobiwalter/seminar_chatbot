import dateparser

#Helper functions that are needed in actions module

def matchingSeminar(seminars,course) -> int:

		for ele in seminars:
			if course.lower() in (d.lower() for d in ele["description"]):
				seminar_id = ele["seminar_id"]
				return seminar_id 

def dateComparison(date1, date2) -> int:
		if dateparser.parse(date1,settings={'DATE_ORDER': 'DMY'}).date() == \
			 dateparser.parse(date2,settings={'DATE_ORDER': 'DMY'}).date():
			 return 0
		elif dateparser.parse(date1,settings={'DATE_ORDER': 'DMY'}).date() < \
				 dateparser.parse(date2,settings={'DATE_ORDER': 'DMY'}).date():
			 return -1
		else: return 1 
