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
	- slot{"time": null}
    - slot{"location": null}	
	- slot{"course": null}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}

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
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}	
	
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
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}	
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}

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
    - utter_ask_course_book
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" :null}

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
	
## test story 10 - unhappy path
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
* get_dates
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
	- slot{"seminar_id":"7"}
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	
## test story 11
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	
## test story 12 
* cancel_seminar{"course": "programming"}
    - slot{"course": "programming"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
    - utter_are_you_sure
* affirm
    - action_cancel_seminar
    - slot{"cancellation_confirmed": "False"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
	- utter_suggest_help
* affirm
	- utter_get_help
	
## test story 13
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
	
## test story 14
* show_bookings
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Richards"}
	- action_verify_user	
	- slot{"user_verified":"True"}
	- slot{"employee_id":"193"}
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

## test story 15
* show_bookings
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Richards"}
	- action_verify_user	
	- slot{"user_verified":"True"}
	- slot{"employee_id":"193"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}	
* cancel_seminar{"location":"Munich"}
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
	
## test story 16: cancel seminar date specified - fail
* cancel_seminar{"date":"March 20"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
* inform{"given-name": "Mike", "last-name": "Garcia"}
    - slot{"given-name": "Mike"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
	- utter_suggest_help
* affirm
	- utter_get_help 
	
## test story 17: cancel seminar affirm but then stop
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* stop
	- utter_ask_continue
* negative
	- utter_do_something_else
	
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
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
* thank
	- utter_no_worries
	
## test story 19
* introduction
	- utter_introduction
* other_smalltalk
	- utter_no_chitchat
* book_seminar
	- utter_ask_name
* inform{"given-name":"Tom","last-name":"Reid"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_course_offering
	- utter_ask_course_book
* get_description{"course":"Excel"}
	- action_provide_description
	- utter_ask_course_book
* inform{"course":"Excel"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	
## test story 20
* age
	- utter_no_chitchat
* other_smalltalk
	- utter_no_chitchat
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_level{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_query_level
	- utter_ask_course_book
* get_duration
	- action_query_duration
	- utter_ask_course_book
* get_dates
    - action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
	- utter_ask_course_book
* book_seminar{"date": "May 15", "location": "Berlin"}
    - slot{"date": "May 15"}
    - slot{"location": "Berlin"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": "Berlin"}
    - slot{"date": "May 15"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	
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
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	
## test story 22
* show_bookings
    - utter_ask_name
* other_smalltalk
    - utter_no_chitchat
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
	
## test story 23
* cancel_seminar{"course":"programming"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"False"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}	
	- utter_suggest_help
* negative
	- utter_do_something_else
* negative
	- utter_bye
	
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
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
	
## test story 26
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
* cancel_seminar
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"Machine Learning"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}		
	
## test story 27
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
* get_location{"course":"Programming"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"[Munich, Berlin, Frankfurt]"}
	- slot{"title": "Python for beginners"}
	- utter_ask_course_book
* inform{"course":"Python"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
* show_bookings
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	
## test story 28
* get_prerequisites{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_prerequisites
* get_level
    - action_query_level
* thank
    - utter_no_worries

## test story 29
* cancel_seminar{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
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
	
## test story 30
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
	
## test story 31
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	
## test story 32
* get_level{"course":"Machine Learning"}
	- action_query_level
* get_duration
	- action_query_duration
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
	- slot{"time": null}
    - slot{"location": null}	
	- slot{"course": null}
* show_bookings
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}

## test story 33
* book_seminar{"course": "leadership", "date-period": "June", "time": "2019-05-01T00:00:00.000+02:00"}
    - slot{"course": "rhetoric"}
    - slot{"date-period": "May"}
    - slot{"time": "2019-05-01T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
	- slot{"date-period": null}
	- slot{"time": null}
	- utter_do_something_else
* get_dates
	- action_display_seminar
    - slot{"locations": ["Berlin", "Cologne", "Frankfurt", "Munich"]}
    - slot{"title": "Persuasion and Influence"}
    - slot{"seminar_id": 0}
* book_seminar{"location":"Berlin", "date":"13/04/19"}
    - seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
    - slot{"course": null}

## test story 34
* book_seminar{"location": "Leipzig"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- slot{"categories": "[x,y,z]"}
	- utter_ask_course_book
* inform{"course": "Python"}
	- action_query_date
	- slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Python for beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* get_duration
	- action_query_duration
	- seminar_form
	- slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	
## test story 35	
* get_course_offering{"course-type": "seminar"}
    - action_course_offering
* get_description{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_provide_description
* get_level{"user-level": "beginners"}
    - slot{"user-level": "beginners"}
    - action_query_level
* get_duration
    - action_query_duration
* get_dates
    - action_display_seminar
    - slot{"locations": ["Cologne", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
    - slot{"time": null}
* book_seminar{"location": "Cologne", "date": "20/05/19", "time": "2019-05-19T00:00:00.000+02:00"}
    - slot{"date": "20/05/19"}
    - slot{"location": "Cologne"}
    - slot{"time": "2019-05-19T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "Judith", "last-name": "Anderson"}
    - slot{"given-name": "Judith"}
    - slot{"last-name": "Anderson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 8}
    - seminar_form
    - form{"name": "seminar_form"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
* show_bookings
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
* cancel_seminar{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - utter_ask_course_cancel
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
* inform{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_cancel_seminar
    - slot{"cancellation_confirmed": "True"}
    - slot{"course": null}
    - slot{"location": null}
    - slot{"date": null}
* thank
    - utter_no_worries

## test story 36	
* get_course_offering{"course":"Excel"} 
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title":"Advanced Excel functions and formulas"}
* get_duration
	- action_query_duration
* other_smalltalk
	- utter_no_chitchat
* introduction
	- utter_introduction
* get_location{"course":"Excel"} 
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title":"Python"}
* book_seminar{"date":"19/02/19", "location": "Stuttgart"}
	- utter_ask_name
* inform{"given-name":"Cathy","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"102"}
	- seminar_form
	- form{"name":"seminar_form"}
	- seminar_form
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
* bye
	- utter_bye
	
## test story 37
* book_seminar{"date-period": "May", "time": "2019-05-01T00:00:00.000+02:00"}
    - slot{"date-period": "May"}
    - slot{"time": "2019-05-01T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
    - slot{"categories": ["Rhetoric in Berlin, Cologne, Frankfurt, Munich", "Data Science in Berlin, Frankfurt, Leipzig, Munich", "Programming in Berlin, Frankfurt, Leipzig, Munich", "Excel in Berlin, Erfurt, Hamburg, Stuttgart", "Management in Cologne, Frankfurt, Leipzig, Stuttgart"]}
    - utter_ask_course_book
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
    - utter_ask_course_book
* get_dates{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Frankfurt", "Leipzig", "Munich"]}
    - slot{"title": "Python for Beginners"}
    - slot{"seminar_id": 2}
    - slot{"time": null}
    - utter_ask_course_book
* inform{"course": "programming", "location": "Leipzig"}
    - slot{"course": "programming"}
    - slot{"location": "Leipzig"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": "Leipzig"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "15/05/19"}
    - slot{"date": "15/05/19"}
    - form: seminar_form
    - slot{"date": "15/05/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
    - followup{"name": "action_listen"}
* other_smalltalk
    - utter_no_chitchat
* bad
    - utter_i''m sorry
* insult
    - utter_no_insult
	
## test story 38
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
* get_duration	
	- action_query_duration
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	
## test story 39
* book_seminar+get_dates{"course":"programming"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	
## test story 40
* book_seminar{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- slot{"categories": "[x,y,z]"}
	- utter_ask_course_book
* inform{"course": "Python"}
	- action_query_date
	- slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Python for beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"course": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
* cancel_seminar
	- utter_ask_course_cancel
* inform{"course": "Excel"}
	- action_cancel_seminar
	- slot{"cancellation_confirmed": "True"}
	
## test story 41
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
	- slot{"seminar_id":"7"}
	- slot{"locations": "Berlin, Munich, Frankfurt"}
	- slot{"title": "Python for Beginners"}
	- seminar_form
	- form{"name": "seminar_form"}
* other_loc_date{"other_location":"True"}
	- action_show_all_buttons
	- action_listen
* inform{"location": "Berlin"}
	- seminar_form
	- form{"name": null}
	- action_book_seminar
	- slot{"booking_confirmed": "True"}
	- slot{"date": null}
	- slot{"time": null}
	- slot{"location": null}
	- slot{"course" : null}

## test story 42
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




	

	
	
	
	
	

	





	


	






