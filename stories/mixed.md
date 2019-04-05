## 	mixed 1
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}			
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
## mixed 2 
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
* cancel_seminar
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"Excel"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}			
* book_seminar{"location":"Frankfurt"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- utter_ask_course_book
* inform{"course":"Excel"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}

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
	- slot{"course": null}
	- slot{"date-period": null}
	
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
* 	
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
	- slot{"course": null}
	- slot{"date-period": null}
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
* cancel_seminar{"course":"Excel"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		

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
	- slot{"course": null}
	- slot{"date-period": null}

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
	- slot{"course": null}
	- slot{"date-period": null}

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
	- slot{"date-period": null}
	- slot{"time": null}
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
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
	- slot{"course": null}
	- slot{"date-period": null}
	
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
	- slot{"course": null}
	- slot{"date-period": null}
	
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
	- slot{"date-period": null}
	- slot{"time": null}
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
	- slot{"course": null}
	- slot{"date-period": null}

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
	- slot{"date-period": null}
	- slot{"time": null}
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
	- slot{"course": null}
	- slot{"date-period": null}
* praise	
	- utter_thanks
	
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
    - slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}

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
	- slot{"date-period": null}
	- slot{"time": null}
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
	- slot{"course": null}
	- slot{"date-period": null}
	
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
    - slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
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
    - slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
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
    - slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
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
    - slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
## cancel_show_book
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
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
	- slot{"course": null}
	- slot{"date-period": null}
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	
## cancel_then show bookings
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
*show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	
## cancel_show_book
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
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
	- slot{"course": null}
	- slot{"date-period": null}
	
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
	- slot{"date-period": null}
	- slot{"time": null}
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
	- slot{"course": null}
	- slot{"date-period": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	
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
	- slot{"date-period": null}
	- slot{"time": null}
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
	- slot{"course": null}
	- slot{"date-period": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
	
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
	- slot{"course": null}
	- slot{"date-period": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
* show_bookings	
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
		
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
	- slot{"date-period": null}
	- slot{"time": null}
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
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
	- slot{"course": null}
	- slot{"date-period": null}
* praise
	- utter_thanks
	
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
	- slot{"date-period": null}
	- slot{"time": null}
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
	- slot{"course": null}
	- slot{"date-period": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
	- slot{"cancellation_confirmed":"True"}
	
## show_book_cancel with get_course_offering
* cancel_seminar{"course":"Machine Learning"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* negative
	- utter_do_something_else
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
	- slot{"course": null}
	- slot{"date-period": null}
	
## cancel_show_get_infos
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
* get_course_offering
	- action_course_offering
* get_description{"course":"Excel"}
	- action_provide_description
* get_dates{"location":"Munich"}
	- action_query_date
	
## Generated Story -1331700729346410498
* get_dates{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Persuasion and Influence"}
    - slot{"seminar_id": 0}
* book_seminar{"time": "2019-03-10T00:00:00.000-08:00", "date": "10th of March"}
    - slot{"date": "10th of March"}
    - slot{"time": "2019-03-10T00:00:00.000-08:00"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* thank
    - utter_no_worries
	
## demo story
* show_bookings
	- utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
	- slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
* get_course_offering
	- action_course_offering
* get_description{"course":"Excel"}
	- action_provide_description
* get_location
	- action_display_seminar
	- slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Persuasion and Influence"}
    - slot{"seminar_id": 0}
* book_seminar{"location":"Munich"}
	- seminar_form
	- form: seminar_form
	- form{"name": null}
	- action_book_seminar
	- slot{"booking_confirmed": "True"}
	- slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* cancel_seminar{"course":"Excel"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
* thank+bye
	- utter_thanks_bye
    - action_restart

## Generated Story 6392539147915856992
* show_bookings
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 9}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
* cancel_seminar{"location": "Munich"}
    - slot{"location": "Munich"}
    - utter_ask_course_cancel
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
* inform{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - utter_are_you_sure
* affirm
    - action_cancel_seminar
    - slot{"cancellation_confirmed": "True"}
    - slot{"course": null}
    - slot{"location": null}
    - slot{"date": null}
* get_course_offering
    - action_course_offering
* thank
    - utter_no_worries

## Generated Story 3608197111403174318
* book_seminar
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_course_offering
    - utter_ask_course_book
* get_description{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_provide_description
* get_level{"user-level": "beginners"}
    - slot{"user-level": "beginners"}
    - action_query_level
* get_description{"course": "programming"}
    - slot{"course": "programming"}
    - action_provide_description
* book_seminar
    - action_display_seminar
    - slot{"locations": ["Berlin", "Frankfurt", "Leipzig", "Munich"]}
    - slot{"title": "Python for Beginners"}
    - slot{"seminar_id": 2}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"date": "14/05/19"}
    - slot{"date": "14/05/19"}
    - form: seminar_form
    - slot{"date": "14/05/19"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}


## booking two seminars
* book_seminar{"date-period": "spring", "time": {"from": "2019-03-20T00:00:00.000+01:00", "to": "2019-06-22T00:00:00.000+02:00"}}
    - slot{"date-period": "spring"}
    - slot{"time": {"from": "2019-03-20T00:00:00.000+01:00", "to": "2019-06-22T00:00:00.000+02:00"}}
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 9}
    - action_display_seminar
	- slot{"categories": "[x,y,z]"}
    - utter_ask_course_book
* inform{"course": "Machine Learning", "location": "Frankfurt"}
    - slot{"course": "Machine Learning"}
    - slot{"location": "Frankfurt"}
    - action_query_date
    - slot{"dates": "24/04/19, 02/05/19, 10/05/19"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* get_course_offering{"location":"Frankfurt"}
	- action_display_seminar
	- slot{"categories":"[x,y,z]"}
* get_duration{"course":"programming"}
	- action_query_duration
* get_description
	- action_provide_description
* get_dates
	- action_query_date
	- slot{"dates": "18/02/19, 29/02/19, 27/03/19"}
	- slot{"title": "blabla"}
* book_seminar{"date" : "18/02/19"}
    - seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* praise
	- utter_thanks
* thank+bye
	- utter_thanks_bye
    - action_restart
	
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
* get_occupancy
	- action_query_occupancy
* book_seminar{"location":"Munich"}
	- seminar_form
	- form: seminar_form
	- form{"name": null}
	- action_book_seminar
	- slot{"booking_confirmed": "True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
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
	- slot{"date-period": null}
	- slot{"time": null}
* get_course_offering
	- action_course_offering
* get_occupancy{"course": "Machine Learning"}
	- action_query_occupancy
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
	- slot{"cancellation_confirmed":"True"}
* thank+bye
	- utter_thanks_bye
	
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
	- slot{"date-period": null}
	- slot{"time": null}
* get_occupancy{"course": "Excel"}
	- action_query_occupancy
* thank
	- utter_no_worries
	
## show_book_cancel with get_course_offering and get_occupancy
* cancel_seminar{"course":"Machine Learning"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* negative
	- utter_do_something_else
* get_course_offering
	- action_course_offering
* get_occupancy{"course":"programming"}
	- action_query_occupancy
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
## get two descriptions of seminars
* book_seminar{"date-period": "spring"}
    - slot{"date-period": "spring"}
	- utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- utter_ask_course_book
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
	- utter_ask_course_book
* get_description{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_provide_description
	- utter_ask_course_book
* inform{"course": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"course": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}	
	- slot{"date-period": null}
	
## cancel seminar ask whats possible	
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* negative
	- utter_do_something_else
* ask_whatspossible
	- utter_whatspossible
* show_bookings
	- action_show_bookings
	
## ask whats possible
* get_course_offering
    - action_course_offering
* get_dates{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_display_seminar
    - slot{"locations": ["Cologne", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
    - slot{"time": null}
* book_seminar{"location": "Stuttgart"}
    - slot{"location": "Stuttgart"}
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
* form: inform{"date": "April 24", "time": "2019-04-24T00:00:00.000+02:00"}
    - slot{"date": "April 24"}
    - slot{"time": "2019-04-24T00:00:00.000+02:00"}
    - form: seminar_form
    - slot{"date": "April 24"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
    - slot{"date-period": null}
* show_bookings{"course-type": "seminars"}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
* ask_whatspossible
	- utter_whatspossible
* cancel_seminar{"course": "programming"}
    - slot{"course": "programming"}
    - utter_are_you_sure
* affirm
    - action_cancel_seminar
    - slot{"cancellation_confirmed": "True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* thank
    - utter_no_worries
	
## ask_whatspossible
* ask_whatspossible
	- utter_whatspossible
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"952"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
* get_description{"course":"Excel"}
	- action_provide_description 
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
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
	- slot{"course": null}
	- slot{"date-period": null}
	
## get bunch of info than book
* ask_whatspossible	
	- utter_whatspossible
* get_course_offering{"course":"Python"}
	- action_display_seminar
    - slot{"locations": ["Cologne", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
    - slot{"time": null}
* get_level
	- action_query_level
* get_occupancy
	- action_query_occupancy
* get_course_offering
	- action_course_offering
* get_description{"course":"Excel"}
	- action_provide_description
* get_duration
	- action_query_duration
* get_level
	- action_query_level
* book_seminar+get_dates
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"952"} 	
	- action_display_seminar
    - slot{"locations": ["Cologne", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
    - slot{"time": null}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
## get bunch of info than book
* ask_whatspossible	
	- utter_whatspossible
* get_course_offering{"course":"Python"}
	- action_display_seminar
    - slot{"locations": ["Cologne", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
    - slot{"time": null}
* get_occupancy
	- action_query_occupancy
* get_description{"course":"Excel"}
	- action_provide_description
* get_duration
	- action_query_duration
* get_dates{"location":"Munich"}
	- action_query_date
    - slot{"dates": "24/04/19, 02/05/19, 10/05/19"}
    - slot{"title": "Machine Learning"}
* book_seminar{"date":"24/04/19"}
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"952"} 	
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* ask_whatspossible	
	- utter_whatspossible
* thank+bye
	- utter_thanks_bye
	
## ask whats possible than show bookings
* ask_whatspossible	
	- utter_whatspossible
* show_bookings
	- utter_ask_name
* inform{"given-name":"Max","last-name":"Smith"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"2"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}	
* get_description{"course":"Excel"}
	- action_provide_description
* get_description{"course":"Python"}
	- action_provide_description
* get_prerequisites
	- action_provide_prerequisites
* get_location
	- action_display_seminar
* book_seminar{"date":"18/05/2019"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
## book_seminar and show bookings
* welcome
	- utter_welcome
* ask_whatspossible
	- utter_whatspossible
* other_smalltalk
	- utter_no_chitchat
* get_course_offering
	- action_course_offering
* get_description{"course":"Excel"}
	- action_provide_description
* get_dates
	- action_display_seminar
    - slot{"locations": ["Cologne", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
    - slot{"time": null}
* get_occupancy{"location":"Munich"}
	- action_query_occupancy
* book_seminar{"date":"17/03/19"}
	- utter_ask_name
* inform{"given-name":"Max","last-name":"Smith"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"2"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* show_bookings	
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"time": null}
	- slot{"date-period": null}
	
## book seminar wo course specified	
* welcome
	- utter_welcome
* ask_whatspossible
	- utter_whatspossible
* book_seminar
	- utter_ask_name
* inform{"given-name":"Tom","last-name":"Reid"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_course_offering
	- utter_ask_course_book
* get_description{"course":"programming"}
	- action_provide_description
	- utter_ask_course_book
* inform{"course":"Programming"}
	- action_display_seminar
	- slot{"seminar_id":"7"}
	- slot{"locations":"[Munich, Berlin, Frankfurt]"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* age
	- utter_no_chitchat
* thank+bye	
	- utter_thanks_bye

## multi-intent: book seminar & get dates 
* book_seminar+get_dates{"course":"programming", "location":"Munich"}
	- utter_ask_name
* inform{"given-name":"Rob","last-name":"Cook"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"94"}
	- action_query_date
	- slot{"dates":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* show_bookings	
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"time": null}
	- slot{"date-period": null}
	
## multi-intent: book seminar cour& get locations
* book_seminar+get_location{"course":"programming"}
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
* ask_whatspossible 
	- utter_whatspossible
	- seminar_form
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* cancel_seminar
	- utter_ask_course_cancel
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	- slot{"time":null}
* inform{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"booking_confirmed":"False"}
	- slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	- utter_suggest_help

	

	
	
	

	
	
	

	
	

	



	


 


	



	

	

	



	

	

	


	
