## show_bookings_basic
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
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## show_bookings_location_specified 
* show_bookings{"location":"Frankfurt"}
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Brown"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"0"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## show_bookings_on_specific_date
* show_bookings{"date":"5th of November"}
	- utter_ask_name
* inform{"given-name":"Mary","last-name":"Grey"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"13"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## showBookingsInPeriod_firstFail_thenSuccess
* show_bookings{"date-period":"this year"}
	- utter_ask_name
* inform{"given-name":"Tom","last-name":"Anderson"}
	- action_verify_user
* inform{"given-name":"Thomas","last-name":"Anderson"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"18"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## showBookings_then_getInformation
* show_bookings{"location":"Berlin"}
	- utter_ask_name
* inform{"given-name":"Jim","last-name":"Paul"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"421"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
* get_course_offering{"course":"Excel"}
	- action_display_seminar
	- slot{"seminar_id":"4"}
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title": "Advanced Excel functions and formulas"}
* thank
	- utter_no_worries
	
## story18
* show_bookings
	- utter_ask_name
* inform{"given-name":"Frrd","last-name":"Baker"}
	- action_verify_user
*inform{"given-name":"Fred","last-name":"Baker"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"15"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## story19
* show_bookings
	- utter_ask_name
* inform{"given-name":"Frrd","last-name":"Baker"}
	- action_verify_user
* get_help
	- utter_get_help

## Generated Story 964340541549888998
* show_bookings{"course-type": "seminars", "date": "05th March"}
    - slot{"date": "05th March"}
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
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## show_the_next_booking
* show_bookings{"display-option":"next"}
	- utter_ask_name
* inform{"given-name": "judith", "last-name": "anderson"}
	- action_verify_user
	- slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}	
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}

## Generated Story 5145335876734410380
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
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## Generated Story -3630320044724628870
* show_bookings{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - utter_ask_name
* inform{"given-name": "Ron", "last-name": "Moore"}
    - slot{"given-name": "Ron"}
    - slot{"last-name": "Moore"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 4}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## Generated Story 261112219490772306
* show_bookings{"course-type": "seminars"}
    - utter_ask_name
* inform{"given-name": "Zach", "last-name": "Miles"}
    - slot{"given-name": "Zach"}
    - slot{"last-name": "Miles"}
    - action_verify_user
* inform{"given-name": "Zach", "last-name": "Miles"}
    - slot{"given-name": "Zach"}
    - slot{"last-name": "Miles"}
    - action_verify_user
    - utter_suggest_help
* affirm
    - utter_get_help
	
## Generated Story 261112219490772306
* show_bookings{"course-type": "seminars"}
    - utter_ask_name
* inform{"given-name": "Zach", "last-name": "Miles"}
    - slot{"given-name": "Zach"}
    - slot{"last-name": "Miles"}
    - action_verify_user
* inform{"given-name": "Zach", "last-name": "Miles"}
    - slot{"given-name": "Zach"}
    - slot{"last-name": "Miles"}
    - action_verify_user
    - utter_suggest_help
* negative
	- utter_do_something_else
	
## smalltalk while asking for name 
* show_bookings
	- utter_ask_name
* other_smalltalk
	- utter_no_chitchat
* inform{"given-name":"Mak","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified": "True"}
    - slot{"employee_id": 48}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## show_bookings in period
* show_bookings{"date-period":"January"}
	- utter_ask_name
* inform{"given-name":"Tony","last-name":"Blair"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"10"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## Generated Story -5392053354662535431
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
	- slot{"display-option": null}
	- slot{"booking-type": null}
* other_smalltalk
    - utter_no_chitchat
	
## Generated Story 1526465989610235901
* show_bookings
    - utter_ask_name
* other_smalltalk
    - utter_no_chitchat
* inform{"given-name": "Judith", "last-name": "Anderson"}
    - slot{"given-name": "Judith"}
    - slot{"last-name": "Anderson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 8}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
* praise
	- utter_thanks

## show bookings in date-period	
* show_bookings{"date-period":"summer"}
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Brown"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"0"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
	
## show_bookings_bookingtype
* show_bookings{"booking-type":"past"}
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
	- slot{"display-option": null}
	- slot{"booking-type": null}
