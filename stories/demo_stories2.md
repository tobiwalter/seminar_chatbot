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

## Generated Story 4885585345892436726
* book_seminar{"course": "programming"}
    - slot{"course": "programming"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 5}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Frankfurt", "Hamburg", "Leipzig", "Munich"]}
    - slot{"title": "Python for Beginners"}
    - slot{"seminar_id": 2}
    - slot{"time": null}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - form: seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "25/04/19"}
    - slot{"date": "25/04/19"}
    - form: seminar_form
    - slot{"date": "25/04/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar

## Generated Story 1502101200603100177
* book_seminar{"course": "programming"}
    - slot{"course": "programming"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 5}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Frankfurt", "Hamburg", "Leipzig", "Munich"]}
    - slot{"title": "Python for Beginners"}
    - slot{"seminar_id": 2}
    - slot{"time": null}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "12/05/19", "time": "2019-12-05T00:00:00.000+01:00"}
    - slot{"date": "12/05/19"}
    - slot{"time": "2019-12-05T00:00:00.000+01:00"}
    - form: seminar_form
    - slot{"date": "12/05/19"}
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

## Generated Story 1896157743717369461
* get_course_offering
    - action_course_offering
* get_description{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_provide_description
* book_seminar{"course-type": "seminar"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 10}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Machine Learning"}
    - slot{"seminar_id": 1}
    - slot{"time": null}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Leipzig"}
    - slot{"location": "Leipzig"}
    - form: seminar_form
    - slot{"location": "Leipzig"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "15/04/19"}
    - slot{"date": "15/04/19"}
    - form: seminar_form
    - slot{"date": "15/04/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
* thank
    - utter_no_worries

## Generated Story 2022506860074247300
* welcome
    - utter_welcome
* book_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 0}
    - action_display_seminar
    - slot{"locations": ["Bremen", "Cologne", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
    - slot{"time": null}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* stop
    - utter_do_something_else
* book_seminar{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
    - action_listen
    - slot{"locations": ["Berlin", "Cologne", "Frankfurt", "Munich", "Stuttgart"]}
    - slot{"title": "Persuasion and Influence"}
    - slot{"seminar_id": 0}
    - slot{"time": null}
    - seminar_form
    - slot{"requested_slot": "location"}
* other_loc_date
    - action_show_all_buttons
    - action_listen
    - form: followup{"name": "action_listen"}
    - slot{"other_date": null}
    - slot{"other_location": null}
* form: inform{"location": "Stuttgart"}
    - slot{"location": "Stuttgart"}
    - seminar_form
    - slot{"location": "Stuttgart"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "15/04/19"}
    - slot{"date": "15/04/19"}
    - form: seminar_form
    - slot{"date": "15/04/19"}
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
* thank
    - utter_no_worries

## Generated Story -5258049985866327169
* book_seminar{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 0}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Cologne", "Frankfurt", "Munich", "Stuttgart"]}
    - slot{"title": "Persuasion and Influence"}
    - slot{"seminar_id": 0}
    - slot{"time": null}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "24/04/19"}
    - slot{"date": "24/04/19"}
    - form: seminar_form
    - slot{"date": "24/04/19"}
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
* negative
    - utter_do_something_else
* book_seminar{"course": "excel"}
    - slot{"course": "excel"}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
    - slot{"time": null}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Stuttgart"}
    - slot{"location": "Stuttgart"}
    - form: seminar_form
    - slot{"location": "Stuttgart"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "30/04/19", "time": "2019-04-19T00:00:00.000+02:00"}
    - slot{"date": "30/04/19"}
    - slot{"time": "2019-04-19T00:00:00.000+02:00"}
    - form: seminar_form
    - slot{"date": "30/04/19"}
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
* show_bookings{"display-option": "all"}
    - slot{"display-option": "all"}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
    - slot{"display-option": null}
    - slot{"booking-type": null}
* bye
    - utter_bye

## Generated Story -8729165206592532689
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 10}
    - utter_whatspossible
* get_course_offering
    - action_course_offering
* get_description{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_provide_description
* get_occupancy
    - action_query_occupancy
* get_duration{"course-type": "seminar "}
    - action_query_duration
* get_prerequisites
    - action_provide_prerequisites
* book_seminar
    - action_display_seminar
    - slot{"locations": ["Bremen", "Cologne", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
    - slot{"time": null}
    - action_book_seminar
    - slot{"booking_confirmed": false}
    - followup{"name": "action_location_buttons"}
    - action_location_buttons
* inform{"location": "Bremen"}
    - slot{"location": "Bremen"}
    - action_book_seminar
    - slot{"booking_confirmed": false}
    - followup{"name": "action_date_buttons"}
    - action_date_buttons
* inform{"date": "26/04/19"}
    - slot{"date": "26/04/19"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"date": "26/04/19"}
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
    - utter_do_something_else
* show_bookings{"display-option": "all"}
    - slot{"display-option": "all"}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
    - slot{"display-option": null}
    - slot{"booking-type": null}
* book_seminar{"course": "excel", "location": "Bremen"}
    - slot{"course": "excel"}
    - slot{"location": "Bremen"}
    - action_query_date
    - slot{"location": "Hamburg"}
* affirm
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "20/04/19", "time": "2019-04-19T00:00:00.000+02:00"}
    - slot{"date": "20/04/19"}
    - slot{"time": "2019-04-19T00:00:00.000+02:00"}
    - form: seminar_form
    - slot{"date": "20/04/19"}
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
    - utter_do_something_else
* show_bookings{"display-option": "all"}
    - slot{"display-option": "all"}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
    - slot{"display-option": null}
    - slot{"booking-type": null}
* thank+bye
    - action_restart

## Generated Story -8622729361247247968
* inform{"given-name": "Ron", "last-name": "Moore"}
    - slot{"given-name": "Ron"}
    - slot{"last-name": "Moore"}
    - action_verify_user
    - slot{"user_verified": true}
    - slot{"employee_id": 4}
* ask_whatspossible
    - utter_whatspossible
* get_course_offering
    - action_course_offering
* get_description{"course": "excel"}
    - slot{"course": "excel"}
    - action_provide_description
* book_seminar{"course-type": "seminar"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Stuttgart"}
    - slot{"location": "Stuttgart"}
    - form: seminar_form
    - slot{"location": "Stuttgart"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "20/05/19", "time": "2019-05-19T00:00:00.000+02:00"}
    - slot{"date": "20/05/19"}
    - slot{"time": "2019-05-19T00:00:00.000+02:00"}
    - form: seminar_form
    - slot{"date": "20/05/19"}
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
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
    - slot{"display-option": null}
    - slot{"booking-type": null}
    - utter_ask_course_cancel
* cancel_seminar{"course": "excel", "location": "Stuttgart", "date": "10/05/19", "time": "2019-10-05T00:00:00.000+02:00"}
    - slot{"course": "excel"}
    - slot{"date": "10/05/19"}
    - slot{"location": "Stuttgart"}
    - slot{"time": "2019-10-05T00:00:00.000+02:00"}
    - utter_are_you_sure
* affirm
    - action_cancel_seminar
    - slot{"cancellation_confirmed": true}
    - slot{"course": null}
    - slot{"location": null}
    - slot{"date": null}
    - slot{"time": null}
    - followup{"name": "action_listen"}
* show_bookings{"display-option": "all"}
    - slot{"display-option": "all"}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
    - slot{"display-option": null}
    - slot{"booking-type": null}
* bye
    - utter_bye


