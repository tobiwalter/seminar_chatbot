## Generated Story 6612259313248420894
* book_seminar{"course-type": "lab", "course": "programming"}
    - slot{"course": "programming"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "27/12/18, 19/02/19, 05/03/19"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - form: seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19.02.19"}
    - slot{"date": "19.02.19"}
    - form: seminar_form
    - slot{"date": "19.02.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}

## Generated Story -4106895962687868317
* welcome
    - utter_welcome
* book_seminar
    - utter_ask_name
* inform{"given-name": "max", "last-name": "smith"}
    - slot{"given-name": "max"}
    - slot{"last-name": "smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - action_course_offering
    - utter_ask_course
* inform{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_display_seminar
    - slot{"locations": "Berlin, Erfurt, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - form: seminar_form
    - slot{"location": "Berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "07/03/19", "time": "2019-07-03T00:00:00.000-07:00"}
    - slot{"date": "07/03/19"}
    - form: seminar_form
    - slot{"date": "07/03/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## Generated Story -6669491543552044542
* welcome
    - utter_welcome
* get_description{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_provide_description
* get_level
    - action_query_level
* book_seminar
    - utter_ask_name
* inform{"given-name": "Mark", "last-name": "Miller"}
    - slot{"given-name": "Mark"}
    - slot{"last-name": "Miller"}
    - action_verify_user
* inform{"given-name": "Mark", "last-name": "Miller"}
    - slot{"given-name": "Mark"}
    - slot{"last-name": "Miller"}
    - action_verify_user
    - utter_suggest_help
* affirm
    - utter_get_help

## Generated Story 2565811538605007234
* get_course_offering{"course": "Tableau"}
    - slot{"course": "Tableau"}
    - action_display_seminar
* get_course_offering{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Python for Beginners"}
* book_seminar
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 5}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* get_dates
    - action_query_date
    - action_listen
    - slot{"dates": "27/02/19, 19/03/19, 05/04/19"}
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "05/04"}
    - slot{"date": "05/04"}
    - form: seminar_form
    - slot{"date": "05/04"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## Generated Story 492852742587451376
* get_course_offering
    - action_course_offering
* get_description{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_provide_description
* book_seminar{"location": "Munich"}
    - slot{"location": "Munich"}
    - utter_ask_name
* inform{"given-name": "Ron", "last-name": "Moore"}
    - slot{"given-name": "Ron"}
    - slot{"last-name": "Moore"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 4}
    - action_display_seminar
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "30st of March", "time": "2019-03-30T00:00:00.000-07:00"}
    - slot{"date": "30st of March"}
    - form: seminar_form
    - slot{"date": "30st of March"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
* get_course_offering{"course": "Tableau"}
    - slot{"course": "Tableau"}
    - action_display_seminar
* get_course_offering{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Python for Beginners"}
* book_seminar
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 5}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* get_dates
    - action_query_date
    - action_listen
    - slot{"dates": "27/02/19, 19/03/19, 05/04/19"}
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "05/04"}
    - slot{"date": "05/04"}
    - form: seminar_form
    - slot{"date": "05/04"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

