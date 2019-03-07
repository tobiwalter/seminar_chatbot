## 	
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* book_seminar{"course":"Machine Learning"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}

## inform_then_bookSeminar 
* get_course_offering{"course":"Excel"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title":"Advanced Excel functions and formulas"}
* book_seminar{"date":"19/02/19", "location": "Stuttgart"}
	- utter_ask_name
* inform{"given-name":"Cathy","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"102"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	
## inform_then_bookSeminar_Fail_then_GetHelp
* get_course_offering{"course":"Excel"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title": "Advanced Excel functions and formulas"}
* book_seminar{"date":"19/02/19", "location": "Stuttgart"}
	- utter_ask_name
* inform{"given-name":"Megan", "last-name":"Fowler"}
	- action_verify_user
* inform{"given-name":"Megan", "last-name":"Fowler"}
	- action_verify_user
	- utter_suggest_help
* affirm
	- utter_get_help

## inform_bookSeminar_showBookings_cancelSeminar	
* get_course_offering{"course":"Tableau"}
	- action_display_seminar
* get_course_offering{"course":"Python"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
* book_seminar{"course":"Python"}
	- utter_ask_name
* inform{"given-name":"Tina","last-name":"Gibson"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"14"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
* cancel_seminar{"course":"Excel"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}

## story14
* get_course_offering
	- action_course_offering
* get_description{"course":"programming"}
	- action_provide_description
* book_seminar{"location":"Munich"}
	- utter_ask_name
* inform{"given-name":"Rob","last-name":"Cook"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"94"}
	- action_query_date
	- slot{"dates": "18/02/19, 29/02/19, 27/03/19"}
	- slot{"title": "blabla"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}

## story17
* get_course_offering
	- action_course_offering
* get_prerequisites{"course":"Machine Learning"}
	- action_provide_prerequisites
* book_seminar
	- utter_ask_name
* inform{"given-name":"Jim","last-name":"Paul"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"421"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}

## story20
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"952"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* book_seminar{"course":"Data Science"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Machine Learning"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	
## get_description_and_locations_of_course_andBook
* get_description{"course":"Machine Learning"}
	- action_provide_description
* get_prerequisites
	- action_provide_prerequisites
* get_location OR get_dates
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}	
* book_seminar{"location":"Munich","date":"24/03/19"}
	- utter_ask_name
* inform{"given-name": "Patricia", "last-name": "Grey"}
    - slot{"given-name": "Patricia"}
    - slot{"last-name": "Grey"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 7}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}	
	
## show_bookings then book_seminar
* show_bookings{"course-type": "seminars"}
    - utter_ask_name
* inform{"given-name": "max", "last-name": "smith"}
    - slot{"given-name": "max"}
    - slot{"last-name": "smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
* book_seminar{"course": "machine learning"}
    - slot{"course": "machine learning"}
    - action_display_seminar
	- slot{"seminar_id":"4"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Machine Learning"}
    - seminar_form	
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - form: seminar_form
    - slot{"location": "berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "2nd of April"}
    - slot{"date": "2nd of April"}
    - form: seminar_form
    - slot{"date": "2nd of April"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
	- slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}	

## Generated Story 769974900844405482
* show_bookings{"course-type": "seminars"}
    - utter_ask_name
* inform{"given-name": "Patricia", "last-name": "Grey"}
    - slot{"given-name": "Patricia"}
    - slot{"last-name": "Grey"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 7}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
* get_course_offering
    - action_course_offering
* book_seminar{"course":"rhetoric"}
    - action_display_seminar
	- slot{"seminar_id":"4"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - form: seminar_form
    - slot{"location": "berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "30th of November 2018"}
    - slot{"date": "30th of November 2018"}
    - form: seminar_form
    - slot{"date": "30th of November 2018"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## Generated Story -6463177690486665439
* get_course_offering{"course": "Tableau"}
    - slot{"course": "Tableau"}
    - action_display_seminar
* get_course_offering{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
	- slot{"seminar_id":"4"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
* book_seminar{"location": "munich"}
    - slot{"location": "munich"}
    - utter_ask_name
* inform{"given-name": "Patricia", "last-name": "Grey"}
    - slot{"given-name": "Patricia"}
    - slot{"last-name": "Grey"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 7}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "27/12/18"}
    - slot{"date": "27/12/18"}
    - form: seminar_form
    - slot{"date": "27/12/18"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}

## Generated Story 5080578068932025922
* show_bookings{"display-option": "next"}
    - slot{"display-option": "next"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
* book_seminar{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
	- slot{"seminar_id":"4"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "10.11.18"}
    - slot{"date": "10.11.18"}
    - form: seminar_form
    - slot{"date": "10.11.18"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## Generated Story -3751396503439969687
* get_course_offering
    - action_course_offering
* get_prerequisites{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_provide_prerequisites
* get_dates OR get_location
    - action_display_seminar
	- slot{"seminar_id":"4"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Machine Learning"}
* book_seminar{"location": "Berlin", "date": "2nd of April"}
    - slot{"date": "2nd of April"}
    - slot{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - seminar_form
    - form{"name": "seminar_form"}
	- form{"name": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
* get_help
    - utter_get_help

## Generated Story 7541824829953655735
* get_course_offering
    - action_course_offering
* get_dates{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_display_seminar
	- slot{"seminar_id":"4"}
    - slot{"locations": "Cologne, Frankfurt, Stuttgart"}
    - slot{"title": "Leadership Behaviour"}
* book_seminar{"date": "24.02.19"}
    - slot{"date": "24.02.19"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Thompson"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Thompson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 3}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - form: seminar_form
    - slot{"location": "Cologne"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
	
## Generated Story -7543584780551948522
* get_dates{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
	- slot{"seminar_id":"4"}
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Machine Learning"}
* book_seminar{"location": "Munich", "time": "2019-04-02T00:00:00.000-07:00", "date": "2nd April"}
    - slot{"date": "2nd April"}
    - slot{"location": "Munich"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
	
## Generated Story -1047672868992554109
* get_dates{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
	- slot{"seminar_id":"4"}
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Persuasion and Influence"}
* book_seminar{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Thompson"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Thompson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 3}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "10/03/19", "time": "2019-10-03T00:00:00.000-07:00"}
    - slot{"date": "10/03/19"}
    - form: seminar_form
    - slot{"date": "10/03/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
	
## cancel_show_book
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* book_seminar
	- action_course_offering
	- utter_ask_course_book
* inform{"course":"Programming"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"[Munich, Berlin, Frankfurt]"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	
## cancel_then show bookings
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
*show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	
## cancel_show_book
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	
* book_seminar{"course":"Data Science"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"[Munich, Berlin, Frankfurt]"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	
## show_book_cancel_show
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
* book_seminar{"course":"Machine Learning"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	
## show_book_cancel
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
* book_seminar{"course":"Machine Learning"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	
## book_cancel_show
* book_seminar{"course":"Python","location":"Munich"}
	- utter_ask_name
* inform{"given-name":"Rob","last-name":"Cook"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"94"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* show_bookings	
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
		
## course_offering & booking a seminar - verification fails
* get_course_offering
	- action_course_offering
* book_seminar{"course":"programming"}
    - utter_ask_name
* inform{"given-name": "Tim", "last-name": "Miller"}
    - slot{"given-name": "Tim"}
    - slot{"last-name": "Miller"}
    - action_verify_user
* inform{"given-name": "Tim", "last-name": "Miller"}
    - slot{"given-name": "Tim"}
    - slot{"last-name": "Miller"}
    - action_verify_user
    - utter_suggest_help
* affirm
    - utter_get_help
	
## story20
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"952"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* get_course_offering
	- action_course_offering
* book_seminar{"course":"Data Science"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Machine Learning"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	
## show_book_cancel with get_course_offering
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
* get_course_offering
	- action_course_offering
* book_seminar{"course":"Machine Learning"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}

	

	


 


	



	

	

	



	

	

	


	
