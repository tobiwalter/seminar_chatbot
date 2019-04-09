## get_description_and_dates/locations_of_course
* get_description{"course":"Machine Learning"}
	- action_provide_description
* get_prerequisites
	- action_provide_prerequisites
* get_dates OR get_location
	- action_display_seminar
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- slot{"seminar_id":"4"}
	
## Generated Story -6785827853527499108
* get_course_offering{ "course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
	- slot{"seminar_id":"4"}

## Generated Story 5921147929666083831
* get_course_offering{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
    - slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Persuasion and Influence"}
	- slot{"seminar_id":"4"}

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
*get_dates{"course":"Python"} OR get_location{"course":"Python"}
	- action_display_seminar
	- slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
	- slot{"seminar_id":"4"}
	
## get_offering_specific_course
*get_course_offering{"course":"Excel"}
	- action_display_seminar
	- slot{"locations":"[Erfurt, Berlin, Stuttgart]"}
	- slot{"title":"Advanced Excel functions and formulas"}
	- slot{"seminar_id":"4"}
*get_prerequisites
	- action_provide_prerequisites
	
## get_course_locations
*get_course_offering
	- action_course_offering
*get_location{"course":"Python"} OR get_dates{"course":"Python"}
	- action_display_seminar
	- slot{"locations": "Berlin, Munich, Frankfurt"}
    - slot{"title": "Python for Beginners"}
	- slot{"seminar_id":"4"}
	
## Generated Story -8066266476318493533
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
* get_dates
    - action_display_seminar
    - slot{"locations": "Erfurt, Berlin, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}
	- slot{"seminar_id":"4"}
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
	
## query date when location already given-name
* get_dates{"course":"programming","location":"Berlin"}
	- action_query_date
	- slot{"dates":"12/02/19"}
	- slot{"title": "xyy"}

## query date when location already given
* get_course_offering
	- action_course_offering
* get_dates{"course":"programming","location":"Berlin"}
	- action_query_date
	- slot{"dates":"12/02/19"}
	- slot{"title": "blabla"}
	
## get prerequisites
* get_prerequisites{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_provide_prerequisites
	
## get duration
* get_duration{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_query_duration
	
## get course offering - course specified	
* get_course_offering{"course":"Python"}
	- action_display_seminar
    - slot{"locations": "Erfurt, Berlin, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}
	- slot{"seminar_id":"4"}

## get course offering - wo course specified	
* get_course_offering
	- action_course_offering
	
## Generated Story -6372168583986864578
* get_course_offering{"course": "linear algebra"}
    - slot{"course": "linear algebra"}
    - action_display_seminar
	
* get_course_offering
    - action_course_offering
* get_level{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_query_level
* get_description
    - action_provide_description
	
## get course offering - loc specified
* get_course_offering{"location":"Berlin"}
	- action_display_seminar
	- slot{"categories": "[x,y,z]"}
	
## get course offering - date-period specified
* get_course_offering{"date-period":"spring"}
	- action_display_seminar
	- slot{"categories": "[x,y,z]"}
	
## get course offering - loc specified but no offering at first location
* get_course_offering{"location":"Braunschweig"}
	- action_display_seminar
* get_course_offering
	- action_course_offering
	
## get occupancy
* get_occupancy{"course":"Excel"}
	- action_query_occupancy

## get course offering and occupancy	
* get_course_offering
    - action_course_offering
* get_occupancy{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_query_occupancy
* get_description
    - action_provide_description

## get course offering, description and occupancy	
* get_course_offering{"course-type": "seminars"}
    - action_course_offering
* get_description{"course": "machine learning"}
    - slot{"course": "machine learning"}
    - action_provide_description
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
* get_occupancy
	- action_query_occupancy
	
## what's possible
* ask_whatspossible
	- utter_whatspossible
	
## what' possible and course offering
* ask_whatspossible
	- utter_whatspossible
* get_course_offering
	- action_course_offering
	
## what' possible, location and course offering
* ask_whatspossible
	- utter_whatspossible
* get_location	
	- action_course_offering
* get_course_offering{"location":"Munich"}
	- action_display_seminar
	- slot{"categories": "[x,y,z]"}

## insult
* insult
    - utter_no_insult
	
## what' possible, location and course offering
* ask_whatspossible
	- utter_whatspossible
* goodbye
	- utter_bye
	- action_restart
	
## what' possible, location and course offering
* ask_whatspossible
	- utter_whatspossible
* thank+bye
	- utter_thanks_bye
	
# get_help
* get_help
    - utter_get_help
	

## what' possible and bad
* ask_whatspossible
	- utter_whatspossible
* bad
	- utter_i''m sorry
* negative
	- utter_bye
	- action_restart
	
## bad
* bad
	- utter_i''m sorry
	
## bad and bye
* bad
	- utter_i''m sorry
* negative
	- utter_bye
	- action_restart
	
## smalltalk and bad
* other_smalltalk
	- utter_no_chitchat
* bad
	- utter_i''m sorry

	
## smalltalk and insult
* other_smalltalk
	- utter_no_chitchat
* insult
	- utter_no_insult
	
## welcome
* welcome
	- utter_welcome
* bad
	- utter_i''m sorry
	
## book seminar no name extracted	
* book_seminar
    - utter_ask_name
* inform
    - action_verify_user
	
## show bookings no name extracted	
* show_bookings
    - utter_ask_name
* inform
    - action_verify_user
	
## book seminar no name extracted	
* cancel_seminar
    - utter_ask_name
* inform
    - action_verify_user
	

	
	


	
