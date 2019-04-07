## showBookings 
* show_bookings{"date-period":"this year"}
	- utter_ask_name
* inform{"given-name":"Tom","last-name":"Anderson"}
	- action_verify_user
* get_help
	- utter_get_help
	
## cancel a seminar - deny	
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* get_help
	- utter_get_help
	
## Generated Story 2028561068192250204
* cancel_seminar{"course": "machine learning"}
    - slot{"course": "machine learning"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}	
    - utter_are_you_sure
* affirm
    - action_cancel_seminar
    - slot{"cancellation_confirmed": "True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* get_help
	- utter_get_help
	
## get_course_prerequesites
* get_course_offering
	- action_course_offering
* get_prerequisites{"course":"Python"}
	- action_provide_prerequisites
* get_help
	- utter_get_help
	
## book_seminar_specifying_course       
* book_seminar{"course":"programming"}
	- utter_ask_name
* inform{"given-name":"John","last-name":"Doe"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"53"}
	- action_display_seminar
	- slot{"seminar_id":"7"}
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
* get_help
	- utter_get_help

## book_seminar_specifying_course       
* book_seminar{"course":"programming"}
	- utter_ask_name
* inform{"given-name":"John","last-name":"Doe"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"53"}
	- action_display_seminar
	- slot{"seminar_id":"7"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
* get_help
	- action_deactivate_form
	- utter_get_help
	
## Generated Story 6619672501531644928
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
* get_help
	- utter_get_help
	
	
## Trying to book seminar in date-period in which no seminars available
* book_seminar{"course": "rhetoric", "date-period": "May", "time": "2019-05-01T00:00:00.000+02:00"}
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
* get_help
	- utter_get_help

## Trying to book seminar at location at which no seminars available
* book_seminar{"location": "Paris"}
    - slot{"location": "Paris"}
    - utter_ask_name
* inform{"given-name": "Judith", "last-name": "Anderson"}
    - slot{"given-name": "Judith"}
    - slot{"last-name": "Anderson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 8}
    - action_display_seminar
    - slot{"location": null}
    - utter_do_something_else
* get_location
    - action_course_offering
* get_course_offering{"location":"Munich"}
	- action_display_seminar
	- slot{"categories":"[a,b,c]"}
* get_dates{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_query_date
    - slot{"dates": "30/04/19, 10/05/19, 30/05/19"}
    - slot{"title": "Persuasion and Influence"}
* get_help	
	- utter_get_help
	
## Trying to book seminar at location at which no seminars available
* book_seminar{"location": "Paris"}
    - slot{"location": "Paris"}
    - utter_ask_name
* inform{"given-name": "Judith", "last-name": "Anderson"}
    - slot{"given-name": "Judith"}
    - slot{"last-name": "Anderson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 8}
    - action_display_seminar
    - slot{"location": null}
    - utter_do_something_else
* get_help
	- utter_get_help

## Trying to book seminar at location at which no seminars available
* book_seminar{"location": "Paris"}
    - slot{"location": "Paris"}
    - utter_ask_name
* inform{"given-name": "Judith", "last-name": "Anderson"}
    - slot{"given-name": "Judith"}
    - slot{"last-name": "Anderson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 8}
    - action_display_seminar
    - slot{"location": null}
    - utter_do_something_else
* book_seminar{"location": "Frankfurt"}
	- action_display_seminar
	- slot{"categories": "[x,y,z]"}
	- utter_ask_course_book
* get_help
	- utter_get_help
	
## book 2 seminars with course offering in between
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
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}	
	- slot{"date-period": null}
* book_seminar
	- action_course_offering
	- utter_ask_course_book
* get_help
	- utter_get_help
	
## book seminar what's possible
* ask_whatspossible
	- utter_whatspossible
* get_help	
	- utter_get_help
	
## book seminar what's possible
* get_course_offering
	- action_course_offering
* get_help	
	- utter_get_help
	
## book seminar what's possible
* get_course_offering{"location":"Berlin"}
	- action_display_seminar
	- slot{"categories": "[x,y,z]"}
* get_help	
	- utter_get_help
