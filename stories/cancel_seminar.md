## cancel a seminar
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
* bye
	- utter_bye

## cancel a seminar - deny	
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* negative
	- utter_do_something_else
* negative
	- utter_bye

## cancel a seminar - deny	
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* negative
	- utter_do_something_else
	
## Generated Story 2028561068192250204
* cancel_seminar{"course": "machine learning"}
    - slot{"course": "machine learning"}
    - utter_are_you_sure
* affirm
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_cancel_seminar
    - slot{"cancellation_confirmed": "True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}

## Generated Story 6806321299963726368
* cancel_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
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
	
## Generated Story 6806321299963726368
* cancel_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
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
* affirm
	- utter_get_help

## Generated Story 4074317787840752391
* cancel_seminar{"course": "programming"}
    - slot{"course": "programming"}
    - utter_are_you_sure
* affirm
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 9}
    - action_cancel_seminar
    - slot{"cancellation_confirmed": "True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* thank
    - utter_no_worries
	

## Generated Story -1597762326665473517
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
	
## Generated Story -1597762326665473517
* cancel_seminar{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - utter_are_you_sure
* negative
	- utter_do_something_else

## Generated Story -1597762326665473517
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
	
## cancel seminar no course specified - fail
* cancel_seminar
	- utter_ask_course_cancel
* inform{"course":"Data Science"}
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
	
## cancel seminar no course specified - succeed 
* cancel_seminar
	- utter_ask_course_cancel
* inform{"course":"Data Science"}
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
	
## cancel seminar loc specified - succeed 
* cancel_seminar{"location":"Berlin"}
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"Data Science"}
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
	
## cancel seminar loc specified - fail
* cancel_seminar{"location":"Berlin"}
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"Data Science"}
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
	
## cancel seminar date specified - succeed 
* cancel_seminar{"date":"March 20"}
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"Data Science"}
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
	
## cancel seminar date specified - fail
* cancel_seminar{"location":"March 20"}
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"Data Science"}
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
	
## cancel seminar smalltalk intent
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* other_smalltalk
	- utter_no_chitchat
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
* bye
	- utter_bye

## cancel seminar affirm but then stop
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- utter_ask_name
* stop
	- utter_ask_continue
* negative
	- utter_do_something_else
