## no_course_available              
* welcome              
	- utter_welcome	
* book_seminar{"course":"programming"}
	- utter_ask_name
* inform{"given-name":"John","last-name":"Doe"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"53"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"} 
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	
## start_general_than_book course 
* book_seminar
	- utter_ask_name
* inform{"given-name":"Tom","last-name":"Reid"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_course_offering
	- utter_ask_course
* inform{"course":"Programming"}
	- action_display_seminar
	- slot{"locations":"[Munich, Berlin, Frankfurt]"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}

## show_bookings_basic
* show_bookings
	- utter_ask_name
* inform{"given-name":"Max","last-name":"Smith"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"2"}
	- action_show_bookings
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
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
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
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* thank
	- utter_no_worries
	
## showBookingsInPeriod_firstFail_thenSuccess
* show_bookings{"date-period":"this year"}
	- utter_ask_name
* inform{"given-name":"Tom","last-name":"Anderson"}
	- action_verify_user
* inform{"given-name":"Thomas","last-name":"Anderson"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"18"}
	- action_show_bookings

## inform_then_bookSeminar 
* get_course_offering{"course":"Excel"}
	- action_display_seminar
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title":"Advanced Excel functions and formulas"}
* book_seminar{"date":"19/02/19", "location": "Stuttgart"}
	- utter_ask_name
* inform{"given-name":"Cathy","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"102"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	
## inform_then_bookSeminar_Fail_then_GetHelp
* get_course_offering{"course":"Excel"}
	- action_display_seminar
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title": "Advanced Excel functions and formulas"}
* book_seminar{"date":"19/02/19", "location": "Stuttgart"}
	- utter_ask_name
* inform{"given-name":"Megan", "last-name":"Fowler"}
	- action_verify_user
* inform{"given-name":"Megan", "last-name":"Fowler"}
	- action_verify_user
	- utter_suggest_help
* affirm
	- utter_get_help

## inform_bookSeminar_showBookings_cancelSeminar	
* get_course_offering{"course":"Tableau"}
	- action_display_seminar
* get_course_offering{"course":"Python"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
* book_seminar{"course":"Python"}
	- utter_ask_name
* inform{"given-name":"Tina","last-name":"Gibson"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"14"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
	
* show_bookings
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Richards"}
	- action_verify_user	
	- slot{"user_verified":"True"}
	- slot{"employee_id":"193"}
	- action_show_bookings
* cancel_seminar{"course":"Excel"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}

## story12
* book_seminar{"user-level":"beginners","course":"Python"}
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Richards"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"109"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* thank
	- utter_no_worries

## story13
* welcome
	- utter_welcome
* book_seminar{"course":"Python","location":"Munich"}
	- utter_ask_name
* inform{"given-name":"Rob","last-name":"Cook"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"94"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* thank
	- utter_no_worries
* bye
	- utter_bye

## story14
* welcome
	- utter_welcome
* get_course_offering
	- action_course_offering
* get_description{"course":"programming"}
	- action_provide_description
* book_seminar{"location":"Munich"}
	- utter_ask_name
* inform{"given-name":"Rob","last-name":"Cook"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"94"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* thank
	- utter_no_worries
* bye
	- utter_bye


## showBookings_then_getInformation
* welcome
	- utter_welcome
* show_bookings{"location":"Berlin"}
	- utter_ask_name
* inform{"given-name":"Jim","last-name":"Paul"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"421"}
	- action_show_bookings
* get_course_offering{"course":"Excel"}
	- action_display_seminar
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title": "Advanced Excel functions and formulas"}
* thank
	- utter_no_worries

## story16
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
* bye
	- utter_bye

## story17
* welcome
	- utter_welcome
* get_course_offering
	- action_course_offering
* get_prerequisites{"course":"Machine Learning"}
	- action_provide_prerequisites
* book_seminar
	- utter_ask_name
* inform{"given-name":"Jim","last-name":"Paul"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"421"}
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
* thank
	- utter_no_worries

## story18
* show_bookings
	- utter_ask_name
* inform{"given-name":"Frrd","last-name":"Baker"}
	- action_verify_user
*inform{"given-name":"Fred","last-name":"Baker"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"15"}
	- action_show_bookings
* thank
	- utter_no_worries

## story19
* show_bookings
	- utter_ask_name
* inform{"given-name":"Frrd","last-name":"Baker"}
	- action_verify_user
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
	- slot{"title": "Machine Learning"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":"null"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
    - slot{"location": null}
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
    - slot{"date": null}
    - slot{"location": null}
	
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
	- slot{"booking_confirmed": "False"}
* get_help
    - utter_get_help
	
## get_description_and_dates_of_course
* get_description{"course":"Machine Learning"}
	- action_provide_description
* get_prerequisites
	- action_provide_prerequisites
* get_dates OR get_location
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}

## get_description_and_locations_of_course
* get_description{"course":"Machine Learning"}
	- action_provide_description
* get_prerequisites
	- action_provide_prerequisites
* get_location OR get_dates
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}	
	
	
## get_description_and_locations_of_course_andBook
* get_description{"course":"Machine Learning"}
	- action_provide_description
* get_prerequisites
	- action_provide_prerequisites
* get_location
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
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
	- slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}	
	
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
    - slot{"date": null}
    - slot{"location": null}	

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
* get_course_offering
    - action_course_offering
* book_seminar{"course":"rhetoric"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
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
    - slot{"date": null}
    - slot{"location": null}
	
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
* get_course_offering{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
* thank
    - utter_no_worries

## Generated Story 5921147929666083831
* get_course_offering{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Persuasion and Influence"}

## Generated Story -6463177690486665439
* get_course_offering{"course": "Tableau"}
    - slot{"course": "Tableau"}
    - action_display_seminar
* get_course_offering{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
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
* inform{"given-name": "judith", "last-name": "anderson"}
    - slot{"given-name": "judith"}
    - slot{"last-name": "anderson"}
    - action_verify_user
	- utter_suggest_help
* affirm
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
* get_course_offering{"course-type": "seminars"}
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
    - slot{"date": null}
    - slot{"location": null}
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
	
## show_the_next_booking
* show_bookings{"display-option":"next"}
	- utter_ask_name
* inform{"given-name": "judith", "last-name": "anderson"}
	- action_verify_user
	- slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_show_bookings
* thank
	- utter_no_worries
	
## get_course_description
*get_course_offering
	- action_course_offering
*get_description{"course":"Python"}
	- action_provide_description
	
## get_course_prerequesites
*get_course_offering
	- action_course_offering
*get_prerequisites{"course":"Python"}
	- action_provide_prerequisites
	
## get_course_dates
*get_course_offering
	- action_course_offering
*get_dates{"course":"Python"}
	- action_display_seminar
	- slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
	
## get_offering_specific_course
*get_course_offering{"course":"Excel"}
	- action_display_seminar
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title":"Advanced Excel functions and formulas"}
*get_prerequisites
	- action_provide_prerequisites
	
## get_course_locations
*get_course_offering
	- action_course_offering
*get_location{"course":"Python"}
	- action_display_seminar
	- slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}

## Generated Story -3751396503439969687
* get_course_offering
    - action_course_offering
* get_prerequisites{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_provide_prerequisites
* get_dates
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Machine Learning"}
* book_seminar{"location": "Berlin", "date": "2nd of April"}
    - slot{"date": "2nd of April"}
    - slot{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
* get_help
    - utter_get_help

## Generated Story 7541824829953655735
* get_course_offering
    - action_course_offering
* get_dates{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_display_seminar
    - slot{"locations": "Cologne, Frankfurt, Stuttgart"}
    - slot{"title": "Leadership Behaviour"}
* book_seminar{"date": "24.02.19"}
    - slot{"date": "24.02.19"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Thompson"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Thompson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 3}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - form: seminar_form
    - slot{"location": "Cologne"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}

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
* bad
    - utter_i''m sorry
* negative

## Generated Story 1532980813945416615
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
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "24.03.19"}
    - slot{"date": "24.03.19"}
    - form: seminar_form
    - slot{"date": "24.03.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## Generated Story 5906864830090693214
* welcome
    - utter_welcome
* book_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_display_seminar
    - slot{"locations": "Cologne, Frankfurt, Stuttgart"}
    - slot{"title": "Leadership Behaviour"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "February 22"}
    - slot{"date": "February 22"}
    - form: seminar_form
    - slot{"date": "February 22"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## Generated Story 6994048039071921318
* book_seminar{"course": "Excel"}
    - slot{"course": "Excel"}
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
	- action_verify_user
	- slot{"user_verified":"True"}
    - action_display_seminar
    - slot{"locations": "Erfurt, Berlin, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Stuttgart"}
    - slot{"location": "Stuttgart"}
    - form: seminar_form
    - slot{"location": "Stuttgart"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "21/03/19"}
    - slot{"date": "21/03/19"}
    - form: seminar_form
    - slot{"date": "21/03/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
* thank
    - utter_no_worries
	
## Generated Story -5546799112556677101
* book_seminar{"course": "programming"}
    - slot{"course": "programming"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_display_seminar
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
	
## Generated Story -2575533301097699461
* book_seminar{"course": "machine learning", "location": "Berlin"}
    - slot{"course": "machine learning"}
    - slot{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
	- action_verify_user
	- slot{"user_verified":"True"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "24.03.19"}
    - slot{"date": "24.03.19"}
    - form: seminar_form
    - slot{"date": "24.03.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
* book_seminar{"course": "leadership", "location": "Cologne"}
    - slot{"course": "leadership"}
    - slot{"location": "Cologne"}
    - action_display_seminar
    - slot{"locations": "Cologne, Frankfurt, Stuttgart"}
    - slot{"title": "Leadership Behaviour"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "Feb 24"}
    - slot{"date": "Feb 24"}
    - form: seminar_form
    - slot{"date": "Feb 24"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
	- slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
## Generated Story 1481861754237016664
* welcome
    - utter_welcome
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
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "05.03.19"}
    - slot{"date": "05.03.19"}
    - form: seminar_form
    - slot{"date": "05.03.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## Generated Story 5145335876734410380
* show_bookings{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_show_bookings

## Generated Story 1389723753389721879
* show_bookings
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - action_show_bookings
* get_course_offering
    - action_course_offering
* get_prerequisites{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_provide_prerequisites

## Generated Story 2515710135921758139
* book_seminar{"course": "machine learning"}
    - slot{"course": "machine learning"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"5"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
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

## Generated Story 2746093808326620672
* book_seminar
    - utter_ask_name
* inform{"given-name": "Ron", "last-name": "Moore"}
    - slot{"given-name": "Ron"}
    - slot{"last-name": "Moore"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 4}
    - action_course_offering
    - utter_ask_course
* inform{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "19.02.19"}
    - slot{"date": "19.02.19"}
    - form: seminar_form
    - slot{"date": "19.02.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## Generated Story -8066266476318493533
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
* get_dates
    - action_display_seminar
    - slot{"locations": "Erfurt, Berlin, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}
* thank
    - utter_no_worries
	
## Get level 
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
* get_level
    - action_query_level
*thank
    - utter_no_worries
	
## Get prerequisites and level 
* get_prerequisites{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_prerequisites
* get_level
    - action_query_level
*thank
    - utter_no_worries
	
## Generated Story -1833706628232292838
* book_seminar{"course": "leadership"}
    - slot{"course": "leadership"}
    - utter_ask_name
* inform{"given-name": "Ron", "last-name": "Moore"}
    - slot{"given-name": "Ron"}
    - slot{"last-name": "Moore"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 4}
    - action_display_seminar
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
* form: inform{"date": "24/02/19"}
    - slot{"date": "24/02/19"}
    - form: seminar_form
    - slot{"date": "24/02/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## Generated Story -3630320044724628870
* show_bookings{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - utter_ask_name
* inform{"given-name": "Ron", "last-name": "Moore"}
    - slot{"given-name": "Ron"}
    - slot{"last-name": "Moore"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 4}
    - action_show_bookings
	
## Generated Story 261112219490772306
* show_bookings{"course-type": "seminars"}
    - utter_ask_name
* inform{"given-name": "Zach", "last-name": "Miles"}
    - slot{"given-name": "Zach"}
    - slot{"last-name": "Miles"}
    - action_verify_user
* inform{"given-name": "Zach", "last-name": "Miles"}
    - slot{"given-name": "Zach"}
    - slot{"last-name": "Miles"}
    - action_verify_user
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
* thank
    - utter_no_worries
	
## Generated Story 2264916548854418086
* book_seminar{"course": "Excel"}
    - slot{"course": "Excel"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
    - slot{"locations": "Erfurt, Berlin, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Erfurt"}
    - slot{"location": "Erfurt"}
    - form: seminar_form
    - slot{"location": "Erfurt"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
* show_bookings{"display-option": "all"}
    - slot{"display-option": "all"}
    - action_show_bookings

## Generated Story 4938161388784026970
* get_course_offering
    - action_course_offering
* book_seminar{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 9}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "munich"}
    - slot{"location": "munich"}
    - form: seminar_form
    - slot{"location": "munich"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "30/11/18"}
    - slot{"date": "30/11/18"}
    - form: seminar_form
    - slot{"date": "30/11/18"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

## Generated Story -8904879758837973854
* get_description{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_provide_description
* get_level{"user-level": "beginners"}
    - slot{"user-level": "beginners"}
    - action_query_level

## Generated Story -8089746694420545386
* get_level{"course": "programming", "user-level": "beginners"}
    - slot{"course": "programming"}
    - slot{"user-level": "beginners"}
    - action_query_level
* get_prerequisites
    - action_provide_prerequisites
* thank
    - utter_no_worries
	
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
	
## query date when location already given-name
* get_dates{"course":"programming","location":"Berlin"}
	- action_query_date

## query date when location already given-name
* get_course_offering
	- action_course_offering
* get_dates{"course":"programming","location":"Berlin"}
	- action_query_date
	
## smalltalk
* other_smalltalk
	- utter_no_chitchat

## introduction
* introduction
	- utter_no_chitchat
	
## age
* age
	- utter_no_chitchat
	
## smalltalk while asking for name 
* show_bookings
	- utter_ask_name
* other_smalltalk
	- utter_no_chitchat
* inform{"given-name":"Mak","last-name":"Miller"}
	- action_verify_user
	- slot{"user_verified": "True"}
    - slot{"employee_id": 48}
	- action_show_bookings

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
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* other_smalltalk
    - utter_no_chitchat
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
* deny
    - action_deactivate_form
    - form{"name": "null"}
	
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
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": "null"}
	
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
	


	
	


	


	
			
	
	
	
	
	







