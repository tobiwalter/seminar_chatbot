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
    - form: seminar_form
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
    - form: seminar_form
    - slot{"location": "Cologne"}
    - slot{"requested_slot": "date"}
* introduction
    - utter_introduction
    - form: seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "24.02."}
    - slot{"date": "24.02."}
    - form: seminar_form
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
    - form: seminar_form
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
    - form: seminar_form
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
    - form: seminar_form
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
    - slot{"location": null}
	
## unhappy_path_seminar_form_ask for location
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
* get_location
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - form: seminar_form
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
    - slot{"location": null}
	
## unhappy_path_seminar_form_ask for dates
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
    - form: seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* get_dates
    - action_query_date
    - form: seminar_form
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
    - form: seminar_form
    - slot{"requested_slot": "location"}
* other_smalltalk
    - utter_no_chitchat
    - form: seminar_form
    - slot{"requested_slot": "location"}
* other_smalltalk
    - utter_no_chitchat
    - form: seminar_form
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
    - form: seminar_form
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
    - form: seminar_form
    - slot{"requested_slot": "location"}
* stop
    - utter_ask_continue
* negative
    - action_deactivate_form
    - form{"name": null}
	
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
    - form: seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* stop
    - utter_ask_continue
* negative
    - action_deactivate_form
    - form{"name": null}
	
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
    - form: seminar_form
    - slot{"requested_slot": "location"}
* stop
    - utter_ask_continue
* affirm
    - form: seminar_form
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
    - slot{"location": null}
	
## unhappy_path: stop, continue and ask for location
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
    - form: seminar_form
    - slot{"requested_slot": "location"}
* get_location
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - form: seminar_form
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
* stop
	- utter_ask_continue
* affirm
    - form: seminar_form
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - form: seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* get_dates
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - form: seminar_form
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
    - slot{"location": null}