## smalltalk
* other_smalltalk
	- utter_no_chitchat

## ask_whatspossible
* ask_whatspossible
	- utter_whatspossible
	
## age
* age
	- utter_no_chitchat
	
## welcome
* welcome              
	- utter_welcome	

## thanks
* thank
	- utter_no_worries
	
## goodbye
* bye
	- utter_bye
	- action_restart

## bad 
* bad
    - utter_i''m sorry

## suggest help because of failed verification
* inform{"given-name":"Mak","last-name":"Miller"}
	- action_verify_user
* inform{"given-name":"Mak","last-name":"Miller"}
	- action_verify_user
	- utter_suggest_help
* get_help
	- utter_get_help
	
	
## provide name first fail then succeed
* inform{"given-name":"Tim","last-name":"Thomas"}
	- action_verify_user
* inform{"given-name":"Tim","last-name":"Thomas"}
	- action_verify_user
	- slot{"user_verified": "True"}
    - slot{"employee_id": 48}
	
	
## user asks for help right away
* inform{"given-name":"Mak","last-name":"Miller"}
	- action_verify_user
* get_help
	- utter_get_help
	
## thank and goodbye
* thank+bye
	- utter_thanks_bye
	- action_restart
	
## praise
* praise
	- utter_thanks
	
## praise, thanks and goodbye
* praise
	- utter_thanks
* thank+bye
	- utter_thanks_bye
	- action_restart
	
## insult
* insult
	- utter_no_insult 	

## ask name with smalltalk intent 
* show_bookings
    - utter_ask_name
* other_smalltalk
    - utter_no_chitchat
    - utter_ask_name
	
