## Ron Moore
* book_seminar{"course:"leadership"}
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
* cancel_seminar{"course":"rhetoric"}
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
* thank+bye
	- utter_thanks_bye
	
## Jane Love
* welcome
	- utter_welcome
* get_course_offering{"course":"programming"}
	- action_course_offering
* get_location
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
* get_prerequisities
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
* book_seminar{"course": "Machine Learning", "location": "Munich"}
	- action_query_date
	- slot{"location": "Stuttgart"}
* affirm
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
* show_bookings
	- action_show_bookings
* praise
	- utter_thanks
	
## Max Smith
* ask_whatspossible
	- utter_whatspossible
* other_smalltalk
	- utter_no_chitchat
* get_course_offering{"location": "Berlin"}
	- action_course_offering
* get_level
	- action_query_level
* get_description
	- action_provide_description
* book_seminar
	- utter_ask_name
* inform{"given-name":"John","last-name":"Doe"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"53"}
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
* inform{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
	
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
	- seminar_form
* other_loc_date{"other_date":"True"}
	- action_show_all_buttons
* stop
	- utter_ask_continue
* negative
	- utter_do_something_else
* bad 
	- utter_i''m sorry
	

	
	


	
	


	
	

	

	
	
	
	
	
	
	
