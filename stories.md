## no_course_available              
* welcome              
	- utter_welcome	
* book_seminar{"course":"programming"}
	- utter_ask_name
* inform{"first-name":"John","last-name":"Doe"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"53"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"dates": "27/12/18, 19/02/19, 05/03/19"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	
## start_general_than_book course 
* book_seminar
	- utter_ask_name
* inform{"first-name":"Tom","last-name":"Reid"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_course_offering
	- utter_ask_course
* inform{"course":"Programming"}
	- action_display_seminar
	- slot{"locations":"[Munich, Berlin, Frankfurt]"}
	- slot{"dates": "[27/12/18]"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}

## show_bookings_basic
* show_bookings
	- utter_ask_name
* inform{"given-name":"Max","last-name":"Smith"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"2"}
* thank
	- utter_no_worries
	
## show_bookings_location_specified 
* show_bookings{"location":"Frankfurt"}
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Brown"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"0"}
	- action_show_bookings
* thank
	- utter_no_worries
	
## show_bookings_on_specific_date
* show_bookings{"date":"5th of November"}
	- utter_ask_name
* inform{"given-name":"Mary","last-name":"Grey"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"13"}
	- action_show_bookings
* thank
	- utter_no_worries

## show_bookings_then_book_seminar 
* show_bookings{"date-period":"January"}
	- utter_ask_name
* inform{"given-name":"Tony","last-name":"Blair"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"10"}
	- action_show_bookings
* book_seminar{"course":"rhetoric","location": "Munich"}
	- action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "10/11/18, 30/11/18, 17/12/18"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries

## show_bookings_then_cancel_seminar_then_book_seminar
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_show_bookings
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* book_seminar{"course":"Machine Learning"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"dates": "24/03/19, 02/04/19"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries
	
## showBookingsInPeriod_firstFail_thenSuccess
* show_bookings{"date-period":"this year"}
	- utter_ask_name
* inform{"first-name":"Tom","last-name":"Anderson"}
	- action_verify_user
	- slot{"user_verified":"False"}
* inform{"first-name":"Thomas","last-name":"Anderson"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"18"}
	- action_show_bookings

## inform_then_bookSeminar 
* get_general_info{"course":"Excel"}
	- action_display_seminar
	- slot{"dates":"[19/02/19, 07/03/19, 21/03/19]"}
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title":"Advanced Excel functions and formulas"}
* book_seminar{"date":"19/02/19", "location": "Stuttgart"}
	- utter_ask_name
* inform{"given-name":"Cathy","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"102"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	
## inform_then_bookSeminar_Fail_then_GetHelp
* get_general_info{"course":"Excel"}
	- action_display_seminar
	- slot{"dates":"[19/02/19, 07/03/19, 21/03/19]"}
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title": "Advanced Excel functions and formulas"}
* book_seminar{"date":"19/02/19", "location": "Stuttgart"}
	- utter_ask_name
* inform{"given-name":"Megan", "last-name":"Fowler"}
	- action_verify_user
	- slot{"user_verified":"False"}
* inform{"given-name":"Megan", "last-name":"Fowler"}
	- action_verify_user
	- slot{"user_verified":"False"}
* get_help
	- utter_get_help

## inform_bookSeminar_showBookings_cancelSeminar	
* get_general_info{"course":"Tableau"}
	- action_display_seminar
* get_general_info{"course":"Python"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"dates": "27/12/18, 19/02/19, 05/03/19"}
	- slot{"title": "Python for beginners"}
* book_seminar{"course":"Python"}
	- utter_ask_name
* inform{"given-name":"Tina","last-name":"Gibson"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"14"}
	- action_book_seminar
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- slot{"booking_confirmed":"True"}
* show_bookings
	- action_show_bookings
* cancel_seminar{"course":"Excel"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}

## story12
* book_seminar{"user-level":"beginners","course":"Python"}
	- utter_ask_name
* inform{"first-name":"Sam","last-name":"Richards"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"109"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries

## story13
* welcome
	- utter_welcome
* book_seminar{"course":"Python","location":"Munich"}
	- utter_ask_name
* inform{"first-name":"Rob","last-name":"Cook"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"94"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"dates": "27/12/18, 19/02/19, 05/03/19"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries
* bye
	- utter_bye

## story14
* welcome
	- utter_welcome
* get_general_info
	- action_course_offering
* get_description{"course":"programming"}
	- action_provide_description
* book_seminar{"location":"Munich"}
	- utter_ask_name
* inform{"first-name":"Rob","last-name":"Cook"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"94"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"dates": "27/12/18, 19/02/19, 05/03/19"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries
* bye
	- utter_bye


## story15
* welcome
	- utter_welcome
* show_bookings{"location":"Berlin"}
	- utter_ask_name
* inform{"first-name":"Jim","last-name":"Paul"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"421"}
	- action_show_bookings
* get_general_info{"course":"Excel"}
	- action_display_seminar
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"dates": "[07/03/19, 19/02/19, 21/03/19]"}
	- slot{"title": "Advanced Excel functions and formulas"}
* thank
	- utter_no_worries

## story16
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- utter_ask_name
* inform{"first-name":"Paul","last-name":"Moore"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"310"}
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* bye
	- utter_bye

## story17
* welcome
	- utter_welcome
* get_general_info
	- action_course_offering
* get_prerequisites{"course":"Machine Learning"}
	- action_provide_prerequisites
* book_seminar
	- utter_ask_name
* inform{"first-name":"Jim","last-name":"Paul"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"421"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"dates": "24/03/19, 02/04/19"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries

## story18
* show_bookings
	- utter_ask_name
* inform{"first-name":"Frrd","last-name":"Baker"}
	- action_verify_user
	- slot{"user_verified":"False"}
*inform{"first-name":"Fred","last-name":"Baker"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"15"}
	- action_show_bookings
* thank
	- utter_no_worries

## story19
* show_bookings
	- utter_ask_name
* inform{"first-name":"Frrd","last-name":"Baker"}
	- action_verify_user
	- slot{"user_verified":"False"}
* get_help
	- utter_get_help

## story20
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"952"}
	- action_show_bookings
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* book_seminar{"course":"Data Science"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"dates": "24/03/19, 02/04/19"}
	- slot{"title": "Machine Learning"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries
	
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
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "27/12/18, 19/02/19, 05/03/19"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* get_description
    - action_provide_description
    - action_listen
    - seminar_form
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
    - slot{"date": "None"}
    - slot{"location": "None"}
* thank
    - utter_no_worries
	

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
    - slot{"locations": "Cologne, Frankfurt, Stuttgart"}
    - slot{"dates": "22/02/19, 24/02/19, 24/03/19"}
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
    - utter_chitchat
    - action_listen
    - seminar_form
    - slot{"requested_slot": "date"}
* form: inform{"date": "24.02."}
    - slot{"date": "24.02."}
    - form: seminar_form
    - slot{"date": "24.02."}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": "None"}
    - slot{"location": "None"}
	
## Generated Story -1788118622721339584
* book_seminar
    - action_course_offering
* book_seminar{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - utter_ask_name
* inform{"given-name": "Patricia", "last-name": "Grey"}
    - slot{"given-name": "Patricia"}
    - slot{"last-name": "Grey"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 7}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "10/11/18, 30/11/18, 17/12/18"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "30th of november"}
    - slot{"date": "30th of november"}
    - form: seminar_form
    - slot{"date": "30th of november"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
* get_help
    - utter_get_help
	
## get_description_and_dates_of_course
* get_description{"course":"Machine Learning"}
	- action_provide_description
* get_prerequisites
	- action_provide_prerequisites
* get_dates
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"dates": "24/03/19, 02/04/19"}
	- slot{"title": "Python for beginners"}

## get_description_and_locations_of_course
* get_description{"course":"Machine Learning"}
	- action_provide_description
* get_prerequisites
	- action_provide_prerequisites
* get_locations
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"dates": "24/03/19, 02/04/19"}
	- slot{"title": "Python for beginners"}	
	
	
## get_description_and_locations_of_course
* get_description{"course":"Machine Learning"}
	- action_provide_description
* get_prerequisites
	- action_provide_prerequisites
* get_locations
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"dates": "24/03/19, 02/04/19"}
	- slot{"title": "Python for beginners"}	
* book_seminar{"location":"Munich","date":"24/03/19"}
	- utter_ask_name
* inform{"given-name": "Patricia", "last-name": "Grey"}
    - slot{"given-name": "Patricia"}
    - slot{"last-name": "Grey"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 7}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
* thank
	- utter_no_worries


	

	

	
	









	

	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	

	
	
	
	
	
	
	
	


	

## Generated Story -5698336889111899031
* show_bookings{"course-type": "seminars"}
    - utter_ask_name
* inform{"given-name": "max", "last-name": "smith"}
    - slot{"given-name": "max"}
    - slot{"last-name": "smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - action_show_bookings
* book_seminar{"course": "machine learning"}
    - slot{"course": "machine learning"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - form: seminar_form
    - slot{"location": "berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "2nd of April"}
    - slot{"date": "2nd of April"}
    - form: seminar_form
    - slot{"date": "2nd of April"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
	- slot{"booking_confirmed": "True"}

## Generated Story 769974900844405482
* welcome
    - utter_welcome
* show_bookings{"course-type": "seminars"}
    - utter_ask_name
* inform{"given-name": "Patricia", "last-name": "Grey"}
    - slot{"given-name": "Patricia"}
    - slot{"last-name": "Grey"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 7}
    - action_show_bookings
* get_general_info
    - action_course_offering
    - utter_ask_course
* inform{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "10/11/18, 30/11/18, 17/12/18"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "berlin"}
    - slot{"location": "berlin"}
    - form: seminar_form
    - slot{"location": "berlin"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "30th of November 2018"}
    - slot{"date": "30th of November 2018"}
    - form: seminar_form
    - slot{"date": "30th of November 2018"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}

## Generated Story 964340541549888998
* show_bookings{"course-type": "seminars", "date": "05th March"}
    - slot{"date": "05th March"}
    - utter_ask_name
* inform{"given-name": "Patricia", "last-name": "Grey"}
    - slot{"given-name": "Patricia"}
    - slot{"last-name": "Grey"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 7}
    - action_show_bookings
* thank
    - utter_no_worries

## Generated Story -6785827853527499108
* get_general_info{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "27/12/18, 19/02/19, 05/03/19"}
    - slot{"title": "Python for Beginners"}
* thank
    - utter_no_worries

## Generated Story 5921147929666083831
* get_general_info{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "10/11/18, 30/11/18, 17/12/18"}
    - slot{"title": "Persuasion and Influence"}

## Generated Story -6463177690486665439
* get_general_info{"course": "Tableau"}
    - slot{"course": "Tableau"}
    - action_display_seminar
* get_general_info{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "27/12/18, 19/02/19, 05/03/19"}
    - slot{"title": "Python for Beginners"}
* book_seminar{"location": "munich"}
    - slot{"location": "munich"}
    - utter_ask_name
* inform{"given-name": "Patricia", "last-name": "Grey"}
    - slot{"given-name": "Patricia"}
    - slot{"last-name": "Grey"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 7}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "27/12/18"}
    - slot{"date": "27/12/18"}
    - form: seminar_form
    - slot{"date": "27/12/18"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
* bad
    - utter_i''m sorry

## Generated Story 6766012708966849594
* book_seminar{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - utter_ask_name
* inform{"given-name": "judith", "last-name": "anderson"}
    - slot{"given-name": "judith"}
    - slot{"last-name": "anderson"}
    - action_verify_user
    - slot{"user_verified": "False"}
* inform{"given-name": "judith", "last-name": "anderson"}
    - slot{"given-name": "judith"}
    - slot{"last-name": "anderson"}
    - action_verify_user
    - slot{"user_verified": "False"}
* get_help
    - utter_get_help

## Generated Story 3038923335748662179
* book_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
    - utter_ask_name
* inform{"given-name": "judith", "last-name": "anderson"}
    - slot{"given-name": "judith"}
    - slot{"last-name": "anderson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 8}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
* bad
	- utter_i''m sorry
	
## Generated Story 158831049711918748
* get_general_info{"course-type": "seminars"}
    - action_course_offering
* get_description{"course": "machine learning"}
    - slot{"course": "machine learning"}
    - action_provide_description
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
* get_prerequisites
    - action_provide_prerequisites
* thank
    - utter_no_worries





## Generated Story 5080578068932025922
* show_bookings{"display-option": "next"}
    - slot{"display-option": "next"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_show_bookings
* book_seminar{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "10/11/18, 30/11/18, 17/12/18"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "10.11.18"}
    - slot{"date": "10.11.18"}
    - form: seminar_form
    - slot{"date": "10.11.18"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": "None"}
    - slot{"location": "None"}
* bye
    - utter_bye

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
	
## book2seminars_1
* book_seminar{"course": "leadership", "date": "24th February", "location": "Stuttgart"}
    - slot{"course": "leadership"}
    - slot{"date": "24th February"}
    - slot{"location": "Stuttgart"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
* book_seminar{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "10/11/18, 30/11/18, 17/12/18"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "30.11.18"}
    - slot{"date": "30.11.18"}
    - form: seminar_form
    - slot{"date": "30.11.18"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## book2seminars_2
* book_seminar{"course": "programming", "location": "berlin"}
    - slot{"course": "programming"}
    - slot{"location": "berlin"}
    - utter_ask_name
* inform{"given-name": "Judith", "last-name": "Anderson"}
    - slot{"given-name": "Judith"}
    - slot{"last-name": "Anderson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 8}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "27/12/18, 19/02/19, 05/03/19"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "05/03/19"}
    - slot{"date": "05/03/19"}
    - form: seminar_form
    - slot{"date": "05/03/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
* book_seminar{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "02.04.19"}
    - slot{"date": "02.04.19"}
    - form: seminar_form
    - slot{"date": "02.04.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
* thank
    - utter_no_worries



