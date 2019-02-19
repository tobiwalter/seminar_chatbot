## no_course_available              
* welcome              
utter_welcome	
* book_seminar{"course":"Math"}
utter_ask_name
* book_seminar{"first-name":"John","last-name":"Doe"}
action_book_seminar
slot{"booking_confirmed":"False"}
utter_no_seminar

## start_general_than_book course 
* book_seminar
action_course_offering
* book_seminar{"course": "Programming"}
action_display_seminar
slot{"locations":"[Munich, Berlin, Frankfurt]"}
slot{"dates": ["27/12/18]"}
slot{"title": "Python for beginners"}
* book_seminar{"location": "Munich"}
action_select_date 
* book_seminar{"seminar_date":"27/12/18"}
utter_ask_name
* book_seminar{"given-name":"Sam","last-name":"Brown"}
action_book_seminar 
slot{"booking_confirmed":"True"}

## show_bookings_basic
* show_bookings
utter_ask_name
* show_bookings{"given-name":"Max","last-name":"Smith"}
action_show_bookings
	
## show_bookings_location_specified 
* show_bookings{"location":"Frankfurt"}
utter_ask_name
* show_bookings{"given-name":"Sam","last-name":"Brown"}
action_show_bookings
* thank
utter_no_worries
	
## show_bookings_on_specific_date
* show_bookings{"seminar_date":"5th of November"}
utter_ask_name
* show_bookings{"given-name":"Mary","last-name":"Grey"}
action_show_bookings

## show_bookings_then_book_seminar 
* show_bookings{"date-period":"January"}
utter_ask_name
* show_bookings{"given-name":"Tony","last-name":"Blair"}
action_show_bookings
* book_seminar{"course:"rhetoric","location": "Munich"}
action_display_seminar
slot{"dates":"[10/11/18,30/11/18,17/12/18]"}
slot{"title": "Python for beginners"}
* book_seminar{"seminar_date":"30/11/18"}
action_book_seminar
slot{"booking_confirmed":"True"}
* thank
utter_no_worries

## show_bookings_then_cancel_seminar_then_book_seminar
* show_bookings
utter_ask_name
* show_bookings{"given-name":"Tim","last-name":"Miller"}
action_show_bookings
* cancel_seminar{"course":"Programming"}
action_cancel_seminar_affirm
* affirm
action_cancel_seminar
slot{"cancellation_confirmed":"True"}
* book_seminar{"course":"Programming"}
action_select_date 
* book_seminar{"seminar_date":"05/03/2019"}
action_book_seminar
slot{"booking_confirmed":"True"}
* thank
utter_no_worries
	
## showBookingsInPeriod_firstFail_thenSuccess
* show_bookings{"date-period":"this year"}
utter_ask_name
* show_bookings
slot{"user_verified":"False"}
utter_try_again
* show_bookings{"given-name":"Tom", "last-name":"Franklin"}
slot{"user_verified":"True"}
	
## inform_then_bookSeminar 
* seminar_info{"course":"Excel"}
action_display_seminar
slot{"dates":"[19/02/19, 07/03/19, 21/03/19]"}
slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
* book_seminar{"seminar_date":"19/02/19", "location": "Stuttgart"}
utter_ask_name
* book_seminar{"given-name":"Cathy", "last-name":"Reed"}
action_book_seminar
slot{"booking_confirmed":"True"}
	
## inform_then_bookSeminar_Fail_then_GetHelp
* seminar_info{"course":"Excel"}
action_display_seminar
slot{"dates":"[19/02/19, 07/03/19, 21/03/19]"}
slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
* book_seminar{"date":"19/02/19", "location": "Stuttgart"}
utter_ask_name
* book_seminar{"given-name":"Megan", "last-name":"Fowler"}
action_book_seminar
slot{"user_verified":"False"}
utter_try_again
* book_seminar{"given-name":"Megan", "last-name":"Fowler"}
action_book_seminar
slot{"user_verified":"False"}
utter_try_again
* get_help
utter_get_help

## inform_bookSeminar_showBookings_cancelSeminar
* seminar_info{"course":"Tableau"}
action_display_seminar
* seminar_info{"course":"Python"}
action_display_seminar
slot{"locations":"[Munich, Berlin, Frankfurt]"}
slot{"dates": ["27/12/18]"}
slot{"title": "Python for beginners"}
* show_bookings
utter_ask_name
* show_bookings{"given-name":"Tina","last-name":"Gibson"}
action_show_bookings
* cancel_seminar{"course":"Excel"}
action_cancel_seminar
* affirm
action_cancel_seminar
slot{"cancellation_confirmed":"True"}
	
## retrieveInfos_then_book
* get_description{"course":"Machine Learning"}
action_provide_description
* get_prerequisites 
action_provide_prerequisites
* get_dates
action_provide_datesWithLocation
slot{"dates":"[[24/03/19, 02/04/19]"}
slot{"locations":"[Berlin, Munich, Frankfurt]"}
* book_seminar{"location":"Frankfurt"}
utter_ask_name
* book_seminar{"given-name":"Tina","last-name":"Gibson"}
action_book_seminar
slot{"booking_confirmed":"True"}
* thank
utter_no_worries
	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	

	
	
	
	
	
	
	
	


	
	
