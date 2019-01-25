1a## no_course_available              
* welcome              
	- utter_welcome	
* book_seminar{"course":"programming"}
	- utter_ask_name
* inform{"first-name":"John","last-name":"Doe"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	
## start_general_than_book course 
* book_seminar
	- action_course_offering
* book_seminar{"course": "programming"}
	- action_display_seminar
	- slot{"locations":"[Munich, Berlin, Frankfurt]"}
	- slot{"dates": "[27/12/18]"}
	- slot{"title": "Python for beginners"}
	- utter_book_where
* book_seminar{"location": "Munich"}
	- action_select_date 
* book_seminar{"seminar_date":"27/12/18"}
	- utter_ask_name
* book_seminar{"given-name":"Sam","last-name":"Brown"}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}

## show_bookings_basic
* show_bookings
	- utter_ask_name
* inform{"given-name":"Max","last-name":"Smith"}
	- action_show_bookings
* thank
	- utter_no_worries
	
## show_bookings_location_specified 
* show_bookings{"location":"Frankfurt"}
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Brown"}
	- action_show_bookings
* thank
	- utter_no_worries
	
## show_bookings_on_specific_date
* show_bookings{"date":"5th of November"}
	- utter_ask_name
* inform{"given-name":"Mary","last-name":"Grey"}
	- action_show_bookings
* thank
	- utter_no_worries

## show_bookings_then_book_seminar 
* show_bookings{"date-period":"January"}
	- utter_ask_name
* inform{"given-name":"Tony","last-name":"Blair"}
	- action_show_bookings
* book_seminar{"course":"rhetoric","location": "Munich"}
	- action_display_seminar
	- slot{"dates":"[10/11/18,30/11/18,17/12/18]"}
	- slot{"title": "Python for beginners"}
	- slot {"locations": "[Berlin,Munich,Frankfurt]"}
* book_seminar{"date":"30/11/18"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries

## show_bookings_then_cancel_seminar_then_book_seminar
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_show_bookings
* cancel_seminar{"course":"programming"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* book_seminar{"course":"Machine Learning"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries
	
## showBookingsInPeriod_firstFail_thenSuccess
* show_bookings{"date-period":"this year"}
* show_bookings{"date-period":"this year"}
	- utter_ask_name
* inform{"first-name":"Tom","last-name":"Anderson"}
	- action_show_bookings
	- slot{"user_verified":"False"}
	- utter_try_again
* inform{"first-name":"Thomas","last-name":"Anderson"}
	- action_show_bookings
	- slot{"user_verified":"True"}
	
## inform_then_bookSeminar 
* get_general_info{"course":"Excel"}
	- action_display_seminar
	- slot{"dates":"[19/02/19, 07/03/19, 21/03/19]"}
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
* book_seminar{"seminar_date":"19/02/19", "location": "Stuttgart"}
	- utter_ask_name
* book_seminar{"given-name":"Cathy", "last-name":"Reed"}
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
	- action_book_seminar
	- slot{"user_verified":"False"}
	- utter_try_again
* inform{"given-name":"Megan", "last-name":"Fowler"}
	- action_book_seminar
	- slot{"user_verified":"False"}
	- utter_try_again
* get_help
	- utter_get_help

## inform_bookSeminar_showBookings_cancelSeminar	
* get_general_info{"course":"Tableau"}
	- action_display_seminar
	- utter_no_course
* get_general_info{"course":"Python"}
	- action_display_seminar
	- slot{"locations":"[Munich, Berlin, Frankfurt]"}
	- slot{"dates": "[27/12/18]"}
	- slot{"title": "Python for beginners"}
	- utter_book_where
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tina","last-name":"Gibson"}
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
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries
* bye
	- utter_bye


# story15
* welcome
	- utter_welcome
* show_bookings{"location":"Berlin"}
	- utter_ask_name
* inform{"first-name":"Jim","last-name":"Paul"}
	- action_show_bookings
* get_general_info{"course":"Excel"}
	- action_display_seminar
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"dates": "[07/03/19, 19/02/19, 21/03/19]"}
	- slot{"title": "Advanced Excel functions and formulas"}
	- utter_book_where
* thank
	- utter_no_worries

# story16
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- utter_ask_name
* inform{"first-name":"Paul","last-name":"Moore"}
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* bye
	- utter_bye

# story17
* welcome
	- utter_welcome
* get_general_info
	- action_course_offering
* get_prerequisites{"course":"Machine Learning"}
	- action_provide_prerequisites
* book_seminar
	- utter_ask_name
* inform{"first-name":"Jim","last-name":"Paul"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries

# story18
* show_bookings
	- utter_ask_name
* inform{"first-name":"Frrd","last-name":"Baker"}
	- action_show_bookings
	- slot{"user_verified":"False"}
	- utter_try_again
* inform{"first-name":"Fred","last-name":"Baker"}
	- action_show_bookings
* thank
	- utter_no_worries

# story19
* show_bookings
	- utter_ask_name
* inform{"first-name":"Frrd","last-name":"Baker"}
	- action_show_bookings
	- slot{"user_verified":"False"}
	- utter_try_again
* get_help
	- utter_get_help

# story20
* show_bookings
	- utter_ask_name
* inform{"given-name":"Tim","last-name":"Miller"}
	- action_show_bookings
* cancel_seminar{"course":"rhetoric"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed":"True"}
* book_seminar{"course":"Data Science"}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
* thank
	- utter_no_worries









	

	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	

	
	
	
	
	
	
	
	


	
	


## Generated Story 9165719372477610666
* show_bookings
    - utter_ask_name
* inform{"given-name": "max", "last-name": "smith"}
    - slot{"given-name": "max"}
    - slot{"last-name": "smith"}
    - action_show_bookings
* book_seminar{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
* book_seminar{"location": "frankfurt"}
    - slot{"location": "frankfurt"}
    - action_select_date
* book_seminar{"date": "February 19"}
    - slot{"date": "February 19"}
    - action_book_seminar
* thank
    - utter_no_worries
* bye
    - utter_bye

