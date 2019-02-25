## smalltalk
* other_smalltalk
	- utter_no_chitchat

## introduction
* introduction
	- utter_introduction
	
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