## test story 1 
* book_seminar{"course": "machine learning", "location": "Berlin"}
    - slot{"course": "machine learning"}
    - slot{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
	- action_verify_user
	- slot{"user_verified":"True"}
    - action_query_date
	- slot{"dates": "24/03/19, 02/04/19"}
	- slot{"title": "blabla"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "24.03.19"}
    - slot{"date": "24.03.19"}
    - form: seminar_form
    - slot{"date": "24.03.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}	
* book_seminar{"course": "leadership", "location": "Cologne"}
    - slot{"course": "leadership"}
    - slot{"location": "Cologne"}
    - action_query_date
	- slot{"dates": "24/03/19, 02/04/19"}
	- slot{"title": "blabla"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "Feb 24"}
    - slot{"date": "Feb 24"}
    - form: seminar_form
    - slot{"date": "Feb 24"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
	- slot{"booking_confirmed": "True"}
	- slot{"date": null}
    - slot{"location": null}
	
## test story 2
* welcome
    - utter_welcome
* book_seminar{"course": "programming"}
    - slot{"course": "programming"}
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 9}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
	- slot{"seminar_id":"7"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "05.03.19"}
    - slot{"date": "05.03.19"}
    - form: seminar_form
    - slot{"date": "05.03.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## test story 3
* show_bookings{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_show_bookings

## test story 4
* show_bookings
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - action_show_bookings
* get_course_offering
    - action_course_offering
* get_prerequisites{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_provide_prerequisites

## test story 5 
* book_seminar{"course": "machine learning"}
    - slot{"course": "machine learning"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"5"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Machine Learning"}
	- slot{"seminar_id":"7"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "02.04.19"}
    - slot{"date": "02.04.19"}
    - form: seminar_form
    - slot{"date": "02.04.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## test story 6
* book_seminar
    - utter_ask_name
* inform{"given-name": "Ron", "last-name": "Moore"}
    - slot{"given-name": "Ron"}
    - slot{"last-name": "Moore"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 4}
    - action_course_offering
    - utter_ask_course
* inform{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
	- slot{"seminar_id":"7"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19.02.19"}
    - slot{"date": "19.02.19"}
    - form: seminar_form
    - slot{"date": "19.02.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## test story 7	
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
* get_dates
    - action_display_seminar
    - slot{"locations": "Erfurt, Berlin, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}	
	- slot{"seminar_id":"7"}
* thank
    - utter_no_worries
	
## test story 8
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
* get_level
    - action_query_level
*thank
    - utter_no_worries
	
## test story 9	
* book_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
    - utter_ask_name
* inform{"given-name": "Ron", "last-name": "Moore"}
    - slot{"given-name": "Ron"}
    - slot{"last-name": "Moore"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 4}
    - action_display_seminar
    - slot{"locations": "Cologne, Frankfurt, Stuttgart"}
    - slot{"title": "Leadership Behaviour"}
	- slot{"seminar_id":"7"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - form: seminar_form
    - slot{"location": "Cologne"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "24/02/19"}
    - slot{"date": "24/02/19"}
    - form: seminar_form
    - slot{"date": "24/02/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## test story 10
* welcome
    - utter_welcome
* book_seminar
    - utter_ask_name
* inform{"given-name": "max", "last-name": "smith"}
    - slot{"given-name": "max"}
    - slot{"last-name": "smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - action_course_offering
    - utter_ask_course
* inform{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_display_seminar
    - slot{"locations": "Berlin, Erfurt, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}
	- slot{"seminar_id":"7"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - form: seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "07/03/19", "time": "2019-07-03T00:00:00.000-07:00"}
    - slot{"date": "07/03/19"}
    - form: seminar_form
    - slot{"date": "07/03/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## test story 11
* welcome
    - utter_welcome
* get_description{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_provide_description
* get_level
    - action_query_level
* book_seminar
    - utter_ask_name
* inform{"given-name": "Mark", "last-name": "Miller"}
    - slot{"given-name": "Mark"}
    - slot{"last-name": "Miller"}
    - action_verify_user
* inform{"given-name": "Mark", "last-name": "Miller"}
    - slot{"given-name": "Mark"}
    - slot{"last-name": "Miller"}
    - action_verify_user
    - utter_suggest_help
* affirm
    - utter_get_help
	
## test story 12 - unhappy path
* get_course_offering{"course": "Tableau"}
    - slot{"course": "Tableau"}
    - action_display_seminar
* get_course_offering{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Python for Beginners"}
	- slot{"seminar_id":"7"}
* book_seminar{"course": "programming"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 5}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* get_dates
    - action_query_date
    - slot{"dates": "27/02/19, 19/03/19, 05/04/19"}
	- slot{"title": "blabla"}
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "05/04"}
    - slot{"date": "05/04"}
    - form: seminar_form
    - slot{"date": "05/04"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## test story 13
* book_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 9}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
	- slot{"seminar_id":"7"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* other_smalltalk
	- utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "location"}
* stop
    - utter_ask_continue
* affirm
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - form: seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - form: seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## test story 15 
* cancel_seminar{"course": "programming"}
    - slot{"course": "programming"}
    - utter_are_you_sure
* affirm
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - action_cancel_seminar
    - slot{"cancellation_confirmed": "False"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
	- utter_suggest_help
	
## test story 16
* welcome
    - utter_welcome
* get_description{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_provide_description
* get_level
    - action_query_level
* book_seminar
    - utter_ask_name
* inform{"given-name": "Mark", "last-name": "Miller"}
    - slot{"given-name": "Mark"}
    - slot{"last-name": "Miller"}
    - action_verify_user
* inform{"given-name": "Mark", "last-name": "Miller"}
    - slot{"given-name": "Mark"}
    - slot{"last-name": "Miller"}
    - action_verify_user
    - utter_suggest_help
* affirm
    - utter_get_help
	
## test story 17
* show_bookings
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Richards"}
	- action_verify_user	
	- slot{"user_verified":"True"}
	- slot{"employee_id":"193"}
	- action_show_bookings
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
	
	
## test story 18
* welcome
	- utter_welcome
* get_course_offering{"course":"rhetoric"}
	- action_display_seminar
	- slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Persuasion and Influence"}
	- slot{"seminar_id":"9"}
* book_seminar{"location":"Munich"}
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Richards"}
	- action_verify_user	
	- slot{"user_verified":"True"}
	- slot{"employee_id":"193"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - form: seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
	- slot{"booking_confirmed": "False"}
* thank
	- utter_no_worries
	
## test story 19
* introduction
	- utter_introduction
* other_smalltalk
	- utter_no_chitchat
	
## test story 20
* age
	- utter_no_chitchat
* other_smalltalk
	- utter_no_chitchat
	
## test story 21
* book_seminar{"course": "Data Science", "location": "Munich"}
    - slot{"course": "Data Science"}
    - slot{"location": "Munich"}
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 9}
    - action_query_date
    - slot{"dates": "24/03/19, 02/04/19"}
	- slot{"title": "blabla"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* stop
    - utter_ask_continue
* affirm
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "2nd April", "time": "2019-04-02T00:00:00.000-07:00"}
    - slot{"date": "2nd April"}
    - form: seminar_form
    - slot{"date": "2nd April"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
	
## test story 22
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
* other_smalltalk
    - utter_no_chitchat
	
## test story 23
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
	- slot{"employee_id": 2}
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"False"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}	
	- utter_suggest_help
* negative
	- utter_do_something_else
* negative
	
## test story 24
* get_course_offering
	- action_course_offering
* get_location{"course":"Excel"}
	- action_display_seminar
	- slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Advanced Excel functions and formulas"}
	- slot{"seminar_id":"7"}
* get_level
	- action_query_level
	
## test story 25
* get_course_offering
	- action_course_offering
* get_prerequisites{"course":"Machine Learning"}
	- action_provide_prerequisites
	
## test story 26
* book_seminar{"course":"Python","location":"Munich"}
	- utter_ask_name
* inform{"given-name":"Rob","last-name":"Cook"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"94"}
	- action_query_date
	- slot{"dates": "24/03/19, 02/04/19"}
	- slot{"title": "blabla"}	
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
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* show_bookings	
	- action_show_bookings
	
## test story 27
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_show_bookings
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
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
	
	
## test story 28
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
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
	
* book_seminar
	- action_course_offering
	- utter_ask_course
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
	
## test story 29
* get_prerequisites{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_prerequisites
* get_level
    - action_query_level
*thank
    - utter_no_worries

## test story 30
* cancel_seminar{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - utter_are_you_sure
* affirm
	- utter_ask_name
* inform{"given-name": "Mike", "last-name": "Garcia"}
    - slot{"given-name": "Mike"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
* inform{"given-name": "Mike", "last-name": "Garcia"}
    - slot{"given-name": "Mike"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
	- utter_suggest_help
* affirm
	- utter_get_help 

	
	
	
	
	

	





	


	






