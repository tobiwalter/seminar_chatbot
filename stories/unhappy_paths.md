## unhappy_path_seminar_form_1
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
    - slot{"requested_slot": "location"}
* get_description
    - action_provide_description
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path_seminar_form_2
* book_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Thompson"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Thompson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 3}
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Cologne, Frankfurt, Stuttgart"}
    - slot{"title": "Leadership Behaviour"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - seminar_form
    - slot{"location": "Cologne"}
    - slot{"requested_slot": "date"}
* introduction
    - utter_introduction
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "24.02."}
    - slot{"date": "24.02."}
    - seminar_form
    - slot{"date": "24.02."}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}	
	
## unhappy_path_seminar_form_2.1
* book_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Thompson"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Thompson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 3}
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Cologne, Frankfurt, Stuttgart"}
    - slot{"title": "Leadership Behaviour"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* introduction
    - utter_introduction
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - seminar_form
    - slot{"location": "Cologne"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "24.02."}
    - slot{"date": "24.02."}
    - seminar_form
    - slot{"date": "24.02."}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## unhappy_path_seminar_form_3
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* other_smalltalk OR age
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path_seminar_form_3.1
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* other_smalltalk OR age
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path_seminar_form_4
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
    - slot{"requested_slot": "location"}
* get_prerequisites
    - action_provide_prerequisites
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path_seminar_form_4.1
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
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* get_prerequisites
    - action_provide_prerequisites
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path_seminar_form_5
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
    - slot{"requested_slot": "location"}
* get_level
    - action_query_level
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path_seminar_form_5.1
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
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* get_level
    - action_query_level
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## verry_unhappy_path_seminar_form_1
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* other_smalltalk
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "location"}
* other_smalltalk
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "location"}
* other_smalltalk
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## verry_unhappy_path_seminar_form_1
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* other_smalltalk
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "location"}
* other_smalltalk
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "location"}
* other_smalltalk
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## verry_unhappy_path_seminar_form_1.1
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* other_smalltalk
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "date"}
* other_smalltalk
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "date"}
* other_smalltalk
    - utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## stop_but_continue_path_form
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* stop
    - utter_ask_continue
* affirm
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## stop_but_continue_path_form date
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* stop
    - utter_ask_continue
* affirm
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## chitchat stop and really stop path
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* other_smalltalk
	- utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "location"}
* stop
    - utter_ask_continue
* negative
    - action_deactivate_form
    - form{"name": null}
	- utter_do_something_else	
	
## chitchat stop and really stop path date
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* other_smalltalk
	- utter_no_chitchat
    - seminar_form
    - slot{"requested_slot": "location"}
* stop
    - utter_ask_continue
* negative
    - action_deactivate_form
    - form{"name": null}
	- utter_do_something_else	
	
## stop and really stop path 
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* stop
    - utter_ask_continue
* negative
    - action_deactivate_form
    - form{"name": null}
	- utter_do_something_else	
	
## stop and really stop path date
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* stop
    - utter_ask_continue
* negative
    - action_deactivate_form
    - form{"name": null}
	- utter_do_something_else	
	
## chitchat stop but continue path
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
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
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
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path: stop but continue loc
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
    - slot{"requested_slot": "location"}
* stop
	- utter_ask_continue
* affirm
    - seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path: stop, continue and ask for dates
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
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}	
* stop
	- utter_ask_continue
* affirm
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path_seminar_form_17
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
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* get_description
    - action_provide_description
    - seminar_form
	- slot{"requested_slot": "date"}
* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path - show_bookings
* show_bookings
	- utter_ask_name
* other_smalltalk OR age
	- utter_no_chitchat
	- utter_ask_name
* inform{"given-name":"Max","last-name":"Smith"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"2"}
	- action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
	
## unhappy_path stop - cancel_seminar
* cancel_seminar{"course": "machine learning"}
    - slot{"course": "machine learning"}
    - utter_are_you_sure
* affirm
    - utter_ask_name
* stop
	- utter_ask_continue
* negative
	- utter_do_something_else
	
## unhappy_path smalltalk - cancel_seminar
* cancel_seminar{"course": "machine learning"}
    - slot{"course": "machine learning"}
    - utter_are_you_sure
* affirm
    - utter_ask_name
* other_smalltalk
	- utter_no_chitchat
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
	
## smalltalk when booking seminars
* book_seminar{"course": "leadership"}
	- slot{"course": "leadership"}
	- utter_ask_name
* other_smalltalk
	- utter_no_chitchat
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
	- slot{"requested_slot": "location"}
	* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
	* form: inform{"date": "19th February"}
    - slot{"date": "19th February"}
    - seminar_form
    - slot{"date": "19th February"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## book seminar wo course - smalltalk intent 
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
* other_smalltalk
    - utter_no_chitchat
    - utter_ask_course_book
* inform{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Python for Beginners"}
    - slot{"seminar_id": 2}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "05/04/19", "time": "2019-05-04T00:00:00.000-07:00"}
    - slot{"date": "05/04/19"}
    - slot{"time": "2019-05-04T00:00:00.000-07:00"}
    - seminar_form
    - slot{"date": "05/04/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## get_level
* book_seminar{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - action_display_seminar
	- slot{"seminar_id":"4"}
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Machine Learning"}
    - slot{"seminar_id": 1}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* get_level
    - action_query_level
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "24/03/19"}
    - slot{"date": "24/03/19"}
    - seminar_form
    - slot{"date": "24/03/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
	
## unhappy_path_no loc or date fits
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
    - slot{"requested_slot": "location"}
* negative
    - action_deactivate_form
	- utter_do_something_else
	
## unhappy_path_no loc 
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
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* negative
    - action_deactivate_form
	- utter_do_something_else
	
## unhappy path with action_query_date
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
