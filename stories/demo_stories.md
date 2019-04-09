## Sam Brown
* book_seminar{"course":"leadership"}	
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
* show_bookings{"display-option":"next"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
	- slot{"time": null}
* show_bookings
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
* thank+bye
	- utter_thanks_bye
	
## Jane Love
* welcome
	- utter_welcome
* get_course_offering{"course":"programming"}
	- action_display_seminar
	- slot{"seminar_id":"7"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
* get_description
	- action_provide_description
* get_duration
	- action_query_duration
* get_occupancy
	- action_query_occupancy
* book_seminar{"location":"Munich"}
	- utter_ask_name
* inform{"given-name":"John","last-name":"Doe"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"53"}
	- seminar_form
	- form{"name":"seminar_form"}
* get_prerequisites
	- action_provide_prerequisites
	- seminar_form
	- form{"name":null} 
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* get_course_offering
	- action_course_offering
* book_seminar{"course": "Machine Learning", "location":"Munich"}
	- action_query_date
	- slot{"location": "Stuttgart"}
* affirm
	- action_query_date
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "Machine Learning"}
	- seminar_form
	- form{"name":"seminar_form"}
* get_occupancy{"date":"07/05/19"}
	- action_query_occupancy
	- seminar_form
	- form{"name":null} 
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* show_bookings
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
* praise
	- utter_thanks
	
## Max Smith
* ask_whatspossible
	- utter_whatspossible
* other_smalltalk
	- utter_no_chitchat
* get_course_offering{"location": "Berlin"}
	- action_display_seminar
	- slot{"categories":"[x,y,z]"}
* get_level{"course":"Excel"}
	- action_query_level
* get_description
	- action_provide_description
* book_seminar
	- utter_ask_name
* inform{"given-name":"John","last-name":"Doe"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"53"}
	- action_query_date
	- slot{"dates":"x,y,z"}
	- slot{"title": "Python for beginners"} 	
	- seminar_form
	- form{"name":"seminar_form"}
* other_smalltalk	
	- utter_no_chitchat
	- seminar_form
	- form{"name":null} 
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* cancel_seminar
	- utter_ask_course_cancel
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}	
	- slot{"display-option": null}
	- slot{"booking-type": null}
* inform{"course": "Excel"} OR inform{"course": "Excel", "date":"18/09/19"} OR inform{"course": "Excel", "location":"Munich"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
	- slot{"time": null}
* praise
	- utter_thanks
* thank+bye
	- utter_thanks_bye
	
## David Wagner 
* book_seminar{"course":"Excel", "date-period": "spring"}
    - slot{"course": "Excel"}
    - slot{"date-period": "spring"}
    - slot{"time": "2019-05-01T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user	
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
	- slot{"seminar_id":"7"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Excel"}
	- seminar_form
    - form{"name": "seminar_form"}
* other_loc_date{"other_location":"True"}
	- action_show_all_buttons
* inform{"location":"Hamburg"}
	- seminar_form
* other_loc_date{"other_date":"True"}
	- action_show_all_buttons
* stop 
	- utter_ask_continue
* negative
	- utter_do_something_else
* bad 
	- utter_i''m sorry
	
## Generated Story -8114647200784749199
* welcome
    - utter_welcome
* ask_whatspossible
    - utter_whatspossible
* get_description{"course": "leadership "}
    - slot{"course": "leadership "}
    - action_provide_description
* get_course_offering{"course": "Math"}
    - slot{"course": "Math"}
    - action_display_seminar
    - slot{"course": null}
    - slot{"location": null}
    - slot{"time": null}
    - slot{"date": null}
    - slot{"date-period": null}
    - utter_do_something_else
* book_seminar{"date-period": "June"}
    - slot{"date-period": "June"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Thompson"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Thompson"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 3}
    - action_display_seminar
    - slot{"date-period": null}
    - slot{"time": null}
    - followup{"name": "utter_do_something_else"}
    - utter_do_something_else
* negative
    - utter_bye
	
## Generated Story -938838891292
* get_location
    - action_course_offering
* get_course_offering{"location": "Leipzig"}
    - slot{"location": "Leipzig"}
	- action_display_seminar
	- slot{"categories":"[x,y,z]"}
* get_dates{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_query_date
    - slot{"dates": ["x,y,z"]}
    - slot{"title": "Advanced Excel functions and formulas"}
* get_occupancy
    - action_query_occupancy
* get_duration
    - action_query_duration
* other_smalltalk
    - utter_no_chitchat
* get_prerequisites
    - action_provide_prerequisites
* book_seminar
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 9}
    - seminar_form
    - form{"name": "seminar_form"}
* other_loc_date{"other_date": "True"}
    - action_show_all_buttons
    - slot{"other_date": null}
    - slot{"other_location": null}
* form: inform{"date": "07/05/19"}
    - seminar_form
    - form{"name": null}
    - action_book_seminar
    - slot{"booking_confirmed": false}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
    - slot{"date-period": null}
    - followup{"name": "utter_do_something_else"}
    - utter_do_something_else

	
	


	
	


	
	

	

	
	
	
	
	
	
	
