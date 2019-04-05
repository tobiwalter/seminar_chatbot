## cancel a seminar
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* bye
	- utter_bye
	- action_restart

## cancel a seminar - deny	
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* negative
	- utter_do_something_else
* negative
	- utter_bye
	- action_restart

## cancel a seminar - deny	
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* negative
	- utter_do_something_else
	
## Generated Story 2028561068192250204
* cancel_seminar{"course": "machine learning"}
    - slot{"course": "machine learning"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
    - utter_are_you_sure
* affirm
    - action_cancel_seminar
    - slot{"cancellation_confirmed": True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}

## Generated Story 6806321299963726368
* cancel_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
    - utter_are_you_sure
* affirm
    - action_cancel_seminar
	- slot{"cancellation_confirmed":False}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
	- utter_suggest_help
* negative
	- utter_do_something_else	
	
## Generated Story 6806321299963726368
* cancel_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
    - utter_are_you_sure
* affirm
    - action_cancel_seminar
	- slot{"cancellation_confirmed":False}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
	- utter_suggest_help
* affirm
	- utter_get_help

## Generated Story 4074317787840752391
* cancel_seminar{"course": "programming"}
    - slot{"course": "programming"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
    - utter_are_you_sure
* affirm
    - action_cancel_seminar
    - slot{"cancellation_confirmed": True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* thank
    - utter_no_worries
	

## Generated Story -1597762326665473517
* cancel_seminar{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
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
	
## Generated Story -1597762326665473517
* cancel_seminar{"course": "Machine Learning"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
    - slot{"course": "Machine Learning"}
    - utter_are_you_sure
* negative
	- utter_do_something_else

## Generated Story -1597762326665473517
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
	
## cancel seminar no course specified - fail
* cancel_seminar
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
* inform{"given-name": "Mike", "last-name": "Garcia"}
    - slot{"given-name": "Mike"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
	- utter_suggest_help
* negative
	- utter_do_something_else
* negative
	- utter_bye
	
## cancel seminar no course specified - succeed 
* cancel_seminar
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"Data Science"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* thank+bye
	- utter_thanks_bye
	- action_restart
	
## cancel seminar loc specified - succeed 
* cancel_seminar{"location":"Berlin"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"Data Science"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* praise
	- utter_thanks
	
## cancel seminar date specified - succeed 
* cancel_seminar{"date":"March 20"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"Data Science"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
	
## cancel seminar smalltalk intent
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_are_you_sure
* other_smalltalk
	- utter_no_chitchat
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* bye
	- utter_bye
	- action_restart

## cancel seminar affirm but then stop
* cancel_seminar{"course":"rhetoric"}
	- utter_ask_name
* stop
	- utter_ask_continue
* negative
	- utter_do_something_else
	
## cancel seminar no course specified - succeed 2
* cancel_seminar
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_ask_course_cancel
	- action_show_bookings
* inform{"course":"Data Science"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* thank+bye
	- utter_thanks_bye

## cancel seminar no course specified - cancel_seminar intent x 2
* cancel_seminar
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_ask_course_cancel
	- action_show_bookings
* cancel_seminar{"course":"Data Science"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* thank+bye
	- utter_thanks_bye
	
## cancel seminar date specified - succeed 
* cancel_seminar{"date":"March 20"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_ask_course_cancel
	- action_show_bookings
* cancel_seminar{"course":"Data Science"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}

## cancel seminar loc specified - succeed 
* cancel_seminar{"location":"Berlin"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_ask_course_cancel
	- action_show_bookings
* cancel_seminar{"course":"Data Science"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
* thank+bye
	- utter_thanks_bye
	- utter_thanks_bye
	
## cancel seminar date specified - succeed 
* ask_whatspossible
	- utter_whatspossible
* cancel_seminar{"date":"March 20"}
	- utter_ask_name
* inform{"given-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":True}
	- slot{"employee_id":"310"}	
	- utter_ask_course_cancel
	- action_show_bookings
* cancel_seminar{"course":"Data Science"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":True}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}



