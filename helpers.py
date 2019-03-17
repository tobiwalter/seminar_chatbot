#Helper functions that are needed in actions module

def matchingSeminar(seminars,course) -> int:

		for ele in seminars:
			if course.lower() in (d.lower() for d in ele["description"]):
				seminar_id = ele["seminar_id"]
				return seminar_id 