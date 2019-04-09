## Generated Story -29924221942365485
* welcome
    - utter_welcome
* get_course_offering{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Machine Learning"}
    - slot{"seminar_id": 1}
    - slot{"time": null}
* get_duration
    - action_query_duration
* get_description
    - action_provide_description
* book_seminar{"location": "Stuttgart"}
    - slot{"location": "Stuttgart"}
    - utter_ask_name
* inform{"given-name": "Ron", "last-name": "Moore"}
    - slot{"given-name": "Ron"}
    - slot{"last-name": "Moore"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 4}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "17/04/19"}
    - slot{"date": "17/04/19"}
    - form: seminar_form
    - slot{"date": "17/04/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": false}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
    - slot{"date-period": null}
    - followup{"name": "utter_do_something_else"}
    - utter_do_something_else
* book_seminar{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Frankfurt", "Hamburg", "Leipzig", "Munich"]}
    - slot{"title": "Python for Beginners"}
    - slot{"seminar_id": 2}
    - slot{"time": null}
* book_seminar{"location": "stuttgart"}
    - slot{"location": "stuttgart"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* get_prerequisites
    - action_provide_prerequisites
    - action_listen
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "02/05/19"}
    - slot{"date": "02/05/19"}
    - form: seminar_form
    - slot{"date": "02/05/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": false}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
    - slot{"date-period": null}
    - followup{"name": "utter_do_something_else"}
    - utter_do_something_else
* show_bookings{"display-option": "all"}
    - slot{"display-option": "all"}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
* thank
    - utter_no_worries

## Generated Story 3343874950408195985
* welcome
    - utter_welcome
* get_course_offering{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Frankfurt", "Hamburg", "Leipzig", "Munich"]}
    - slot{"title": "Python for Beginners"}
    - slot{"seminar_id": 2}
    - slot{"time": null}
* get_description
    - action_provide_description
* get_duration
    - action_query_duration
* get_occupancy
    - action_query_occupancy
* book_seminar{"location": "munich"}
    - slot{"location": "munich"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": "munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "15/05/19"}
    - slot{"date": "15/05/19"}
    - form: seminar_form
    - slot{"date": "15/05/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - followup{"name": "action_listen"}
* inform{"given-name": "Ron", "last-name": "Moore"}
    - slot{"given-name": "Ron"}
    - slot{"last-name": "Moore"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 4}
    - seminar_form
    - form{"name": "seminar_form"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": false}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
    - slot{"date-period": null}
    - followup{"name": "utter_do_something_else"}
    - utter_do_something_else
* book_seminar{"course": "Machine Learning", "location": "munich"}
    - slot{"course": "Machine Learning"}
    - slot{"location": "munich"}
    - action_query_date
    - slot{"location": "Stuttgart"}
* affirm
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* get_prerequisites
    - action_provide_prerequisites
    - action_listen
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "17/04/19"}
    - slot{"date": "17/04/19"}
    - form: seminar_form
    - slot{"date": "17/04/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": false}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
    - slot{"date-period": null}
    - followup{"name": "utter_do_something_else"}
    - utter_do_something_else
* show_bookings{"display-option": "all"}
    - slot{"display-option": "all"}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
* thank
    - utter_no_worries

## Generated Story 6237414721162952305
* get_course_offering{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Frankfurt", "Hamburg", "Leipzig", "Munich"]}
    - slot{"title": "Python for Beginners"}
    - slot{"seminar_id": 2}
    - slot{"time": null}
* book_seminar{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 2}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* get_prerequisites
    - action_provide_prerequisites
    - action_listen
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "02/05/19"}
    - slot{"date": "02/05/19"}
    - form: seminar_form
    - slot{"date": "02/05/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": false}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
    - slot{"date-period": null}
    - followup{"name": "utter_do_something_else"}
    - utter_do_something_else
* get_course_offering{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Machine Learning"}
    - slot{"seminar_id": 1}
    - slot{"time": null}
* get_duration{"course-type": "seminar"}
    - action_query_duration
* get_description
    - action_provide_description
* get_occupancy
    - action_query_occupancy
* book_seminar
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* other_loc_date
    - action_show_all_buttons
    - action_listen
    - form: followup{"name": "action_listen"}
    - slot{"other_date": null}
    - slot{"other_location": null}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* other_loc_date
    - action_show_all_buttons
    - action_listen
    - form: followup{"name": "action_listen"}
    - slot{"other_date": null}
    - slot{"other_location": null}
* form: inform{"date": "18/05/19"}
    - slot{"date": "18/05/19"}
    - seminar_form
    - slot{"date": "18/05/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": false}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
    - slot{"date-period": null}
    - followup{"name": "utter_do_something_else"}
    - utter_do_something_else
* show_bookings{"display-option": "all"}
    - slot{"display-option": "all"}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
* thank+bye
    - utter_thanks_bye

## Generated Story 3765303842878788430
* welcome
    - utter_welcome
* book_seminar
    - action_book_seminar
    - followup{"name": "action_listen"}
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 2}
    - action_course_offering
    - utter_ask_course_book
* inform{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Frankfurt", "Hamburg", "Leipzig", "Munich"]}
    - slot{"title": "Python for Beginners"}
    - slot{"seminar_id": 2}
    - slot{"time": null}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - form: seminar_form
    - slot{"location": "berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "25/04/19"}
    - slot{"date": "25/04/19"}
    - form: seminar_form
    - slot{"date": "25/04/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": true}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"date-period": null}
    - slot{"location": null}
    - slot{"course": null}
    - followup{"name": "action_listen"}
* cancel_seminar
    - utter_ask_course_cancel
* book_seminar{"course": "programming", "location": "Berlin"}
    - slot{"course": "programming"}
    - slot{"location": "Berlin"}
    - utter_ask_continue
* affirm
    - action_cancel_seminar
    - slot{"cancellation_confirmed": true}
    - slot{"course": null}
    - slot{"location": null}
    - slot{"date": null}
    - utter_do_something_else
* show_bookings{"display-option": "all"}
    - slot{"display-option": "all"}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
* thank
    - utter_no_worries

