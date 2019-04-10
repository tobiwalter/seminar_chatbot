## book_seminar_specifying_course         
* book_seminar{"course":"programming"}
	- utter_ask_name
* inform{"given-name":"John","last-name":"Doe"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"53"}
	- action_display_seminar
	- slot{"seminar_id":"7"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null} 
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
## book_seminar wo specifying course
* book_seminar
	- utter_ask_name
* inform{"given-name":"Tom","last-name":"Reid"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"91"}
	- action_course_offering
	- utter_ask_course_book
* inform{"course":"Programming"}
	- action_display_seminar
	- slot{"seminar_id":"7"}
	- slot{"locations":"[Munich, Berlin, Frankfurt]"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
## story12
* book_seminar{"user-level":"beginners","course":"Python"}
	- utter_ask_name
* inform{"given-name":"Sam","last-name":"Richards"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"109"}
	- action_display_seminar
	- slot{"seminar_id":"7"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* thank
	- utter_no_worries
	
## story13
* book_seminar{"course":"Python","location":"Munich"}
	- utter_ask_name
* inform{"given-name":"Rob","last-name":"Cook"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"94"}
	- action_query_date
	- slot{"dates":"24/03/19, 02/04/19"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
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
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}	
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* book_seminar{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
	- slot{"seminar_id":"7"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}

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
    - action_query_date
	- slot{"seminar_id":"7"}
    - slot{"dates": "24/03/19, 02/04/19"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* book_seminar{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
	- slot{"seminar_id":"7"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
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
	- slot{"seminar_id":"7"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## Generated Story 5906864830090693214
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
	- slot{"seminar_id":"7"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}

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
	- slot{"seminar_id":"7"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}

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
* form: inform{"date": "05/03/19"}
    - slot{"date": "05/03/19"}
   - form: seminar_form
    - slot{"date": "05/03/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}

## book2seminars 3 
* book_seminar{"course": "machine learning", "location": "Berlin"}
    - slot{"course": "machine learning"}
    - slot{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
	- action_verify_user
	- slot{"user_verified":"True"}
    - action_query_date
    - slot{"dates": "24/03/19, 02/04/19"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* book_seminar{"course": "leadership", "location": "Cologne"}
    - slot{"course": "leadership"}
    - slot{"location": "Cologne"}
    - action_query_date
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "Leadership Behaviour"}
    - form: seminar_form
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
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
	- slot{"seminar_id":"7"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## Generated Story 2746093808326620672
* ask_whatspossible
	- utter_whatspossible
* what_information
	- utter_what_information
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
* inform{"course": "programming"}
    - slot{"course": "programming"}
    - action_display_seminar
	- slot{"seminar_id":"7"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## Generated Story 6612259313248420894
* book_seminar{"course": "programming"}
    - slot{"course": "programming"}
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
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
* form: inform{"date": "19.02.19"}
    - slot{"date": "19.02.19"}
    - form: seminar_form
    - slot{"date": "19.02.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* insult
    - utter_no_insult
	
	
## book seminar no course specified
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
* inform{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "02/04/19", "time": "2019-02-04T00:00:00.000-08:00"}
    - slot{"date": "02/04/19"}
    - form: seminar_form
    - slot{"date": "02/04/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}		
	- slot{"course" : null}
	- slot{"date-period": null}

## book seminar no course specified 
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
* inform{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "02/04/19", "time": "2019-02-04T00:00:00.000-08:00"}
    - slot{"date": "02/04/19"}
    - form: seminar_form
    - slot{"date": "02/04/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## book seminar no course specified 
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
* inform{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Frankfurt"}
    - slot{"location": "Frankfurt"}
    - form: seminar_form
    - slot{"location": "Frankfurt"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "10/48/98"}
    - slot{"date": "10/48/98"}
    - form: seminar_form
    - slot{"date": null}
    - slot{"requested_slot": "date"}
* form: inform{"date": "30/03/19", "time": "2019-03-19T00:00:00.000-07:00"}
    - slot{"date": "30/03/19"}
    - form: seminar_form
    - slot{"date": "30/03/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* book_seminar{"course":"rhetoric","location": "Munich"}
	- action_query_date
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "Persuasion and Influence"}
    - seminar_form
    - form{"name": "seminar_form"}
	- form{"name":null}
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## Generated Story 4938161388784026970
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
	- slot{"seminar_id":"7"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}

## book seminar verification fails	
* book_seminar
    - utter_ask_name
* inform{"given-name": "Tim", "last-name": "Miller"}
    - slot{"given-name": "Tim"}
    - slot{"last-name": "Miller"}
    - action_verify_user
* inform{"given-name": "Tim", "last-name": "Miller"}
    - slot{"given-name": "Tim"}
    - slot{"last-name": "Miller"}
    - action_verify_user
    - utter_suggest_help
* affirm
    - utter_get_help
	
## book seminar verification fails	
* book_seminar
    - utter_ask_name
* inform
    - action_verify_user
* inform
    - action_verify_user
    - utter_suggest_help
* affirm
    - utter_get_help
	
## book seminar verification fails	
* book_seminar
    - utter_ask_name
* inform
    - action_verify_user
* get_help
    - utter_get_help
	
## book seminar verification fails	
* book_seminar{"course":"Machine Learning", "location":"Berlin"}
    - utter_ask_name
* inform{"given-name": "Tim", "last-name": "Miller"}
    - slot{"given-name": "Tim"}
    - slot{"last-name": "Miller"}
    - action_verify_user
* inform{"given-name": "Tim", "last-name": "Miller"}
    - slot{"given-name": "Tim"}
    - slot{"last-name": "Miller"}
    - action_verify_user
    - utter_suggest_help
* affirm
    - utter_get_help
	
## book seminar verification fails
* book_seminar{"course":"programming"}
    - utter_ask_name
* inform{"given-name": "Tim", "last-name": "Miller"}
    - slot{"given-name": "Tim"}
    - slot{"last-name": "Miller"}
    - action_verify_user
* inform{"given-name": "Tim", "last-name": "Miller"}
    - slot{"given-name": "Tim"}
    - slot{"last-name": "Miller"}
    - action_verify_user
    - utter_suggest_help
* affirm
    - utter_get_help
	
## book 2 seminars
* book_seminar{"course": "machine learning", "location": "Berlin"}
    - slot{"course": "machine learning"}
    - slot{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - action_query_date
    - slot{"dates": "18/03/19, 26/03/19"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"} 
    - slot{"date": "24.03.19"}
    - slot{"date": "24.03.19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* book_seminar{"course": "leadership", "location": "Cologne"}
    - slot{"course": "leadership"}
    - slot{"location": "Cologne"}
	- action_query_date
    - slot{"dates": "18/03/19, 26/03/19"}
    - slot{"title": "Leadership Behaviour"}
    - seminar_form   
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
    - slot{"date": "Feb 24"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar   <!-- predicted: action_listen -->
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## book_seminar giving wrong location
* book_seminar{"course": "Excel", "location": "Frankfurt"}
    - slot{"course": "Excel"}
    - slot{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_query_date
    - slot{"location": "Stuttgart"}
* affirm
    - action_query_date
    - slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Advanced Excel functions and formulas"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
##  book_seminar giving wrong location 2
* book_seminar{"course": "Excel", "location": "Frankfurt"}
    - slot{"course": "Excel"}
    - slot{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_query_date
    - slot{"location": "Stuttgart"}
* affirm
    - action_query_date
    - slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Advanced Excel functions and formulas"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
	- slot{"time": null}
    - slot{"date": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
##  book_seminar giving wrong location and rejecting recommended loc but booking at other
* book_seminar{"course": "Excel", "location": "Frankfurt"}
    - slot{"course": "Excel"}
    - slot{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_query_date
    - slot{"location": "Stuttgart"}
* negative
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Erfurt, Berlin, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}
	- utter_book_somewhere_else
* affirm OR inform{"location":"Berlin"}
	- seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}

##  book_seminar giving wrong location and rejecting recommended and not booking somewhere else 
* book_seminar{"course": "Excel", "location": "Frankfurt"}
    - slot{"course": "Excel"}	
    - slot{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
    - action_query_date
    - slot{"location": "Stuttgart"}
* negative
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Erfurt, Berlin, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}
	- utter_book_somewhere_else
* negative
	- utter_do_something_else
	
## book seminar only city given
* book_seminar{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- slot{"categories":"[x,y,z]"}
	- utter_ask_course_book
* inform{"course": "Python"}
	- action_query_date
	- slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Python for beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## book seminar verification fails once	
* book_seminar{"course":"Machine Learning"}
    - utter_ask_name
* inform{"given-name": "Mak", "last-name": "Smith"}
    - slot{"given-name": "Tim"}
    - slot{"last-name": "Miller"}
    - action_verify_user
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 2}
    - action_display_seminar
	- slot{"seminar_id":"7"}
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## Generated Story 4423079056173582957
* book_seminar
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
* inform{"given-name": "Max", "last-name": "Smith"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Smith"}
    - action_verify_user
    - utter_suggest_help
* negative
    - utter_do_something_else
* negative
    - utter_bye
    - action_restart
	
## book seminar at other location or date
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
* other_loc_date{"other_location":"True"}
	- action_show_all_buttons
* inform{"course":"Machine Learning"}
	- seminar_form
	- form{"name": null}
	- action_book_seminar
	- slot{"booking_confirmed": "True"}
	- slot{"date": null}
	- slot{"time": null}
	- slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}

## book seminar without course specified at other loc or date
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
* inform{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* other_loc_date{"other_location":"True"}
	- action_show_all_buttons
* inform{"course":"Machine Learning"}
	- seminar_form
	- slot{"requested_slot": "location"}
* inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}	
    - slot{"requested_slot": "date"}
* form: inform{"date": "02/04/19", "time": "2019-02-04T00:00:00.000-08:00"}
    - slot{"date": "02/04/19"}
    - form: seminar_form
    - slot{"date": "02/04/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}	
	- slot{"course" : null}	
	- slot{"date-period": null}
	
## book seminar without course specified at other loc or date
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
* inform{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - slot{"requested_slot": "date"}
* other_loc_date{"other_date":"True"}
	- action_show_all_buttons
* inform{"date":"15/03/19"}
	- seminar_form
	- slot{"requested_slot": "date"}
* form: inform{"date": "02/04/19", "time": "2019-02-04T00:00:00.000-08:00"}
    - slot{"date": "02/04/19"}
    - form: seminar_form
    - slot{"date": "02/04/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}		
	- slot{"course" : null}
	- slot{"date-period": null}

# book seminar with action query date other location or date
* book_seminar{"course":"machine learning", "location": "Berlin"}
    - slot{"course": "machine learning"}
    - slot{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
	- action_verify_user
	- slot{"user_verified":"True"}
    - action_query_date
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* other_loc_date{"other_date":"True"}
	- action_show_all_buttons
* inform{"date":"15/03/19"}
	- seminar_form
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
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## book seminar date clash - cancel seminar yes
* book_seminar{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- slot{"categories":"[x,y,z]"}
	- utter_ask_course_book
* inform{"course": "Python"}
	- action_query_date
	- slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Python for beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"course": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* cancel_seminar
	- utter_ask_course_cancel
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}	
	- slot{"display-option": null}
	- slot{"booking-type": null}
* inform{"course": "Excel"} OR inform{"course":"Excel","date":"18/09/19"} OR inform{"course": "Excel", "location":"Munich"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed": "True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
	- slot{"time": null}

## book seminar date clash - cancel seminar no
* book_seminar{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- slot{"categories":"[x,y,z]"}	
	- utter_ask_course_book
* inform{"course": "Python"}
	- action_query_date
	- slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Python for beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"course": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* negative
	- utter_do_something_else
	
## Generated Story 6619672501531644928
* book_seminar{"date-period": "spring"}
    - slot{"date-period": "spring"}
	- utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- utter_ask_course_book
* inform{"course": "Python"}
    - seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"course": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}	
	- slot{"date-period": null}
	
## book seminar only city given
* book_seminar{"location": "Leipzig"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- slot{"categories":"[x,y,z]"}
	- utter_ask_course_book
* inform{"course": "Python"}
	- action_query_date
	- slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Python for beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## Generated Story 6619672501531644928
* book_seminar{"date-period": "April"}
    - slot{"date-period": "next April"}
	- utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- utter_ask_course_book
* inform{"course": "Python"}
    - seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"course": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}	
	- slot{"date-period": null}
	
## Zwischenfrage bei Seminarbuchung: Description
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
	- utter_ask_course_book
* get_dates OR get_location
    - action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
	- utter_ask_course_book
* book_seminar{"date": "May 15", "location": "Berlin"}
    - slot{"date": "May 15"}
    - slot{"location": "Berlin"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": "Berlin"}
    - slot{"date": "May 15"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
	
## Zwischenfrage bei Seminarbuchung: Level
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_level{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_query_level
	- utter_ask_course_book
* inform{"course":"Excel"}
	- action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": "Berlin"}
    - slot{"date": "May 15"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
	- slot{"time": null}
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
	
## Zwischenfrage bei Seminarbuchung	prqs, duration und dates
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_prerequisites{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_prerequisites
	- utter_ask_course_book
* get_duration
	- action_query_duration
	- utter_ask_course_book
* get_dates OR get_location
    - action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
	- utter_ask_course_book
* book_seminar{"date": "May 15", "location": "Berlin"}
    - slot{"date": "May 15"}
    - slot{"location": "Berlin"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": "Berlin"}
    - slot{"date": "May 15"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}

## Generated Story - book 2 seminars one without course specified
* book_seminar{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Frankfurt", "Leipzig", "Munich"]}
    - slot{"title": "Machine Learning"}
    - slot{"seminar_id": 1}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Leipzig"}
    - slot{"location": "Leipzig"}
    - form: seminar_form
    - slot{"location": "Leipzig"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "05/05/19"}
    - slot{"date": "05/05/19"}
    - form: seminar_form
    - slot{"date": "05/05/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* book_seminar
    - action_course_offering
    - utter_ask_course_book
* inform{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_display_seminar
    - slot{"locations": ["Cologne", "Frankfurt", "Leipzig", "Stuttgart"]}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - form: seminar_form
    - slot{"location": "Cologne"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "20/05/19"}
    - slot{"date": "20/05/19"}
    - form: seminar_form
    - slot{"date": "20/05/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* thank
    - utter_no_worries

## Zwischenfrage bei Seminarbuchung date-period
* book_seminar{"date-period": "spring"}
    - slot{"date-period": "spring"}
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 9}
    - action_display_seminar
	- slot{"categories": "[x,y,z]"}
    - utter_ask_course_book
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
    - utter_ask_course_book
* get_dates
    - action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
    - utter_ask_course_book
* inform{"course": "Excel"}
    - slot{"course": "Excel"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Hamburg"}
    - slot{"location": "Hamburg"}
    - form: seminar_form
    - slot{"location": "Hamburg"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "07/05/19"}
    - slot{"date": "07/05/19"}
    - form: seminar_form
    - slot{"date": "07/05/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
	
## Generated Story -1725494851407634482
* book_seminar{"date-period": "May"}
    - slot{"date-period": "May"}
    - utter_ask_name
* inform{"given-name": "Mary", "last-name": "Grey"}
    - slot{"given-name": "Mary"}
    - slot{"last-name": "Grey"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 6}
    - action_display_seminar
	- slot{"categories": "[x,y,z]"}
    - utter_ask_course_book
* inform{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Frankfurt", "Leipzig", "Munich"]}
    - slot{"title": "Machine Learning"}
    - slot{"seminar_id": 1}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Leipzig"}
    - slot{"location": "Leipzig"}
    - form: seminar_form
    - slot{"location": "Leipzig"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "05/05/19"}
    - slot{"date": "05/05/19"}
    - form: seminar_form
    - slot{"date": "05/05/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* insult
    - utter_no_insult
* show_bookings{"date-period": "May"}
    - slot{"date-period": "May"}
    - action_show_bookings
    - slot{"date": null}
    - slot{"location": null}
    - slot{"date-period": null}
    - slot{"time": null}
	- slot{"display-option": null}
	- slot{"booking-type": null}
* thank
    - utter_no_worries
	
## Generated Story: book in date-period no course specified
* book_seminar{"date-period": "spring", "time": {"from": "2019-03-20T00:00:00.000+01:00", "to": "2019-06-22T00:00:00.000+02:00"}}
    - slot{"date-period": "spring"}
    - slot{"time": {"from": "2019-03-20T00:00:00.000+01:00", "to": "2019-06-22T00:00:00.000+02:00"}}
    - utter_ask_name
* inform{"given-name": "Hugo", "last-name": "Garcia"}
    - slot{"given-name": "Hugo"}
    - slot{"last-name": "Garcia"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 9}
    - action_display_seminar
	- slot{"categories": "[x,y,z]"}
    - utter_ask_course_book
* inform{"course": "Machine Learning", "location": "Frankfurt"}
    - slot{"course": "Machine Learning"}
    - slot{"location": "Frankfurt"}
    - action_query_date
    - slot{"dates": "24/04/19, 02/05/19, 10/05/19"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "24/04/19"}
    - slot{"date": "24/04/19"}
    - form: seminar_form
    - slot{"date": "24/04/19"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}

## Generated Story: book in date-period course specified
* book_seminar{"course": "rhetoric", "date-period": "May", "time": "2019-05-01T00:00:00.000+02:00"}
    - slot{"course": "rhetoric"}
    - slot{"date-period": "May"}
    - slot{"time": "2019-05-01T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
    - slot{"locations": ["Berlin", "Cologne", "Frankfurt", "Munich"]}
    - slot{"title": "Persuasion and Influence"}
    - slot{"seminar_id": 0}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Munich"}
    - slot{"location": "Munich"}
    - form: seminar_form
    - slot{"location": "Munich"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
* insult
    - utter_no_insult
	
## Trying to book seminar in date-period in which no seminars available
* book_seminar{"course": "rhetoric", "date-period": "May", "time": "2019-05-01T00:00:00.000+02:00"}
    - slot{"course": "rhetoric"}
    - slot{"date-period": "May"}
    - slot{"time": "2019-05-01T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
	- slot{"date-period": null}
	- slot{"time": null}
	- utter_do_something_else
* bad
	- utter_i''m sorry
	- utter_do_something_else
	
## Trying to book seminar in date-period in which no seminars available
* book_seminar{"course": "rhetoric", "date-period": "May", "time": "2019-05-01T00:00:00.000+02:00"}
    - slot{"course": "rhetoric"}
    - slot{"date-period": "May"}
    - slot{"time": "2019-05-01T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
	- slot{"date-period": null}
	- slot{"time": null}
	- utter_do_something_else
* get_dates
	- action_display_seminar
    - slot{"locations": ["Berlin", "Cologne", "Frankfurt", "Munich"]}
    - slot{"title": "Persuasion and Influence"}
    - slot{"seminar_id": 0}
	- slot{"time": null}
* book_seminar{"location":"Berlin", "date":"13/04/19"}
    - seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
    - slot{"course": null}
		
## Trying to book seminar at location at which no seminars available
* book_seminar{"location": "Paris"}
    - slot{"location": "Paris"}
    - utter_ask_name
* inform{"given-name": "Judith", "last-name": "Anderson"}
    - slot{"given-name": "Judith"}
    - slot{"last-name": "Anderson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 8}
    - action_display_seminar
    - slot{"location": null}
    - utter_do_something_else
* get_location
    - action_course_offering
* get_course_offering{"location":"Munich"}
	- action_display_seminar
	- slot{"categories":"[a,b,c]"}
* get_dates{"course": "rhetoric"}
    - slot{"course": "rhetoric"}
    - action_query_date
    - slot{"dates": "30/04/19, 10/05/19, 30/05/19"}
    - slot{"title": "Persuasion and Influence"}
* book_seminar{"date":"30/04/19"}
    - seminar_form
    - form{"name": "seminar_form"}
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
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* insult
    - utter_no_insult
	
## Trying to book seminar at location at which no seminars available
* book_seminar{"location": "Paris"}
    - slot{"location": "Paris"}
    - utter_ask_name
* inform{"given-name": "Judith", "last-name": "Anderson"}
    - slot{"given-name": "Judith"}
    - slot{"last-name": "Anderson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 8}
    - action_display_seminar
    - slot{"location": null}
    - utter_do_something_else
	
## Trying to book seminar in date-period in which no seminars available
* book_seminar{"course": "rhetoric", "date-period": "May", "time": "2019-05-01T00:00:00.000+02:00"}
    - slot{"course": "rhetoric"}
    - slot{"date-period": "May"}
    - slot{"time": "2019-05-01T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
	- slot{"date-period": null}
	- slot{"time": null}
	- utter_do_something_else

## Trying to book seminar at location at which no seminars available
* book_seminar{"location": "Paris"}
    - slot{"location": "Paris"}
    - utter_ask_name
* inform{"given-name": "Judith", "last-name": "Anderson"}
    - slot{"given-name": "Judith"}
    - slot{"last-name": "Anderson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 8}
    - action_display_seminar
    - slot{"location": null}
    - utter_do_something_else
* book_seminar{"location": "Frankfurt"}
	- action_display_seminar
	- slot{"categories": "[x,y,z]"}
	- utter_ask_course_book
* inform{"course": "Python"}
	- action_query_date
	- slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Python for beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
	
## Trying to book seminar in date-period in which no seminars available
* book_seminar{"course": "rhetoric", "date-period": "May", "time": "2019-05-01T00:00:00.000+02:00"}
    - slot{"course": "rhetoric"}
    - slot{"date-period": "May"}
    - slot{"time": "2019-05-01T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
	- slot{"date-period": null}
	- slot{"time": null}
	- utter_do_something_else
* get_dates
	- action_display_seminar
    - slot{"locations": ["Berlin", "Cologne", "Frankfurt", "Munich"]}
    - slot{"title": "Persuasion and Influence"}
    - slot{"seminar_id": 0}
	- slot{"time": null}
* book_seminar{"location":"Berlin", "date":"18/09/19"}
	- seminar_form
	- form{"name": "seminar_form"} 
	- form{"name": null}
	- action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* praise
	- utter_thanks
	
## book 2 seminars with course offering in between
* book_seminar{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- slot{"categories": "[x,y,z]"}
	- utter_ask_course_book
* inform{"course": "Python"}
	- action_query_date
	- slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Python for beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}	
	- slot{"date-period": null}
* book_seminar
	- action_course_offering
	- utter_ask_course_book
* get_description{"course": "Python"}
	- action_provide_description
	- utter_ask_course_book
* get_description{"course": "Excel"}
	- action_provide_description
	- utter_ask_course_book
* get_prerequisites
	- action_provide_prerequisites
	- utter_ask_course_book
* inform{"course":"Python"}
	- action_display_seminar
	- slot{"seminar_id":"7"}
	- slot{"locations":"[Munich, Berlin, Frankfurt]"}
	- slot{"title": "Python for beginners"}
	- slot{"time": null}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null}
	- action_book_seminar 
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
* praise
	- utter_thanks
	
## Trying to book seminar in date-period in which no seminars available
* book_seminar{"course": "rhetoric", "date-period": "May", "time": "2019-05-01T00:00:00.000+02:00"}
    - slot{"course": "rhetoric"}
    - slot{"date-period": "May"}
    - slot{"time": "2019-05-01T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
	- slot{"time": null}
	- slot{"date-period": null}
	- utter_do_something_else
* get_location
	- action_display_seminar
    - slot{"locations": ["Berlin", "Cologne", "Frankfurt", "Munich"]}
    - slot{"title": "Persuasion and Influence"}
    - slot{"seminar_id": 0}
	- slot{"time": null}
* get_course_offering
	- action_course_offering
* thank
	- utter_no_worries
* bye
	- utter_bye
    - action_restart
	
## Trying to book course that is not available
* book_seminar{"course": "rhetoric", "date-period": "May", "time": "2019-05-01T00:00:00.000+02:00"}
    - slot{"course": "rhetoric"}
    - slot{"date-period": "May"}
    - slot{"time": "2019-05-01T00:00:00.000+02:00"}
    - utter_ask_name
* inform{"given-name": "Sam", "last-name": "Brown"}
    - slot{"given-name": "Sam"}
    - slot{"last-name": "Brown"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 0}
    - action_display_seminar
	- slot{"course": null}
	- slot{"date": null}
	- slot{"time": null}
	- slot{"location": null}
	- slot{"date-period": null}
	- utter_do_something_else
* get_course_offering
	- action_course_offering
* get_description{"course": "Python"}
	- action_provide_description
* get_dates{"location":"Munich"}
	- action_query_date
	- slot{"seminar_id":"7"}
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "Python for Beginners"}
* thank
	- utter_no_worries
	
## booking in Berlin
* book_seminar{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- slot{"categories": "[x,y,z]"}
	- utter_ask_course_book
* get_description{"course": "Python"}
	- action_provide_description
	- utter_ask_course_book
* inform{"course": "Excel"}
    - action_display_seminar
	- slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
    - seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - action_book_seminar 
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* book_seminar{"course": "leadership", "location": "Cologne"}
    - slot{"course": "leadership"}
    - slot{"location": "Cologne"}
    - action_query_date
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "blabla"}
    - seminar_form   
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
    - slot{"date": "Feb 24"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* thank+bye
	- utter_thanks_bye
	- action_restart
	
## book seminar what's possible
* ask_whatspossible
	- utter_whatspossible
* book_seminar{"course":"programming"}
	- utter_ask_name
* inform{"given-name":"John","last-name":"Doe"}
	- action_verify_user
	- slot{"user_verified":"True"}
	- slot{"employee_id":"53"}
	- action_display_seminar
	- slot{"seminar_id":"7"}
	- slot{"locations":"Munich, Berlin, Frankfurt"}
	- slot{"title": "Python for beginners"}
	- seminar_form
	- form{"name":"seminar_form"}
	- form{"name":null} 
	- action_book_seminar
	- slot{"booking_confirmed":"True"}
	- slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course": null}
	- slot{"date-period": null}
	
## Zwischenfrage bei Seminarbuchung: Description
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_description{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_provide_description
	- utter_ask_course_book
* get_dates OR get_location
    - action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
	- utter_ask_course_book
* book_seminar{"date": "May 15", "location": "Berlin"}
    - slot{"date": "May 15"}
    - slot{"location": "Berlin"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": "Berlin"}
    - slot{"date": "May 15"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
	
## Zwischenfrage bei Seminarbuchung: Level
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_level{"course": "Excel"}
    - slot{"course": "Excel"}
    - action_query_level
	- utter_ask_course_book
* inform{"course":"Excel"}
	- action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": "Berlin"}
    - slot{"date": "May 15"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
	- slot{"time": null}
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
	
## Zwischenfrage bei Seminarbuchung	get_location
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_location
	- action_course_offering
	- utter_ask_course_book
* get_dates{"course":"Python"}
	- action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
* book_seminar{"date": "May 15", "location": "Berlin"}
    - slot{"date": "May 15"}
    - slot{"location": "Berlin"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": "Berlin"}
    - slot{"date": "May 15"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
	
## Zwischenfrage bei Seminarbuchung	ask_whatspossible
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* ask_whatspossible
	- utter_whatspossible
	- utter_ask_course_book
* inform{"course":"Excel"} OR book_seminar{"course":"Excel"}
	- action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"location": "Berlin"}
    - slot{"date": "May 15"}
    - form: followup{"name": "action_book_seminar"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* praise	
	- utter_thanks
	
## Zwischenfrage bei Seminarbuchung	get_occupancy
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_occupancy{"course":"rhetoric"}
	- action_query_occupancy
	- utter_ask_course_book
* get_dates{"course":"Excel"} OR get_location{"course":"Excel"}
	- action_display_seminar
    - slot{"locations": ["Berlin", "Erfurt", "Hamburg", "Stuttgart"]}
    - slot{"title": "Advanced Excel functions and formulas"}
    - slot{"seminar_id": 3}
	- utter_ask_course_book
* inform{"course":"Excel"} OR book_seminar{"location":"Hamburg"} OR book_seminar{"location":"Munich", "date":"18/05/19"} 
    - seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* praise	
	- utter_thanks
	
## Zwischenfrage bei Seminarbuchung	get_location
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_location
	- action_course_offering
	- utter_ask_course_book
* book_seminar{"course":"programming","location":"Frankfurt"}
	- action_query_date
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "blabla"}
	- seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
	- action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
	- utter_do_something_else
* show_bookings
	- action_show_bookings
* get_course_offering
	- action_course_offering
* get_location{"course":"programming","location":"Frankfurt"}
	- action_query_date
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "blabla"}
* book_seminar{"date":"26th April"}
	- seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
	- action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* thank+bye
	- utter_thanks_bye
	- action_restart

## Zwischenfrage bei Seminarbuchung	get_location not available at given location
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_location
	- action_course_offering
	- utter_ask_course_book
* book_seminar{"course":"Machine Learning","location":"Erfurt"}
	- action_query_date
    - slot{"location":"Erfurt"}
* negative
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Erfurt, Berlin, Stuttgart"}
    - slot{"title": "Advanced Excel functions and formulas"}
	- utter_book_somewhere_else
* inform{"location":"Berlin"} OR affirm
	- seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
	- action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
	- utter_do_something_else
* show_bookings
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}	
	- slot{"display-option": null}
	- slot{"booking-type": null}
* get_course_offering
	- action_course_offering
* get_location{"course":"programming","location":"Frankfurt"}
	- action_query_date
    - slot{"dates": "24/03/19, 02/04/19"}
    - slot{"title": "blabla"}
* book_seminar{"date":"26th April"}
	- seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
	- action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
* praise
	- utter_thanks
	
## Zwischenfrage bei Seminarbuchung	get_offering(date-period)
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_course_offering{"date-period":"May"}
	- action_display_seminar
	- slot{"categories":"[x,y,z]"}
	- utter_ask_course_book	
* get_description{"course":"Excel"}
	- action_provide_description
	- utter_ask_course_book
* get_occupancy{"location":"Stuttgart"}
	- action_query_occupancy
	- utter_ask_course_book
* book_seminar{"date":"18th May"}
	- seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
	- action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
	- utter_do_something_else
* show_bookings
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}	
	- slot{"display-option": null}
	- slot{"booking-type": null}
* cancel_seminar{"course":"Python"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
	
## Zwischenfrage bei Seminarbuchung	get_offering(location)
* book_seminar
    - utter_ask_name
* inform{"given-name": "David", "last-name": "Wagner"}
    - slot{"given-name": "David"}
    - slot{"last-name": "Wagner"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 1}
    - action_course_offering
    - utter_ask_course_book
* get_course_offering{"location":"Munich"}
	- action_display_seminar
	- slot{"categories":"[x,y,z]"}
	- utter_ask_course_book	
* get_description{"course":"Excel"}
	- action_provide_description
	- utter_ask_course_book
* get_prerequisites
	- action_provide_prerequisites
	- utter_ask_course_book
* get_occupancy
	- action_query_occupancy
	- utter_ask_course_book
* book_seminar{"date":"18th May"}
	- seminar_form
    - form{"name": "seminar_form"}
    - form{"name": null}
	- action_book_seminar
    - slot{"booking_confirmed": "False"}
    - slot{"date": null}
	- slot{"time": null}
    - slot{"location": null}
    - slot{"course": null}
	- slot{"date-period": null}
	- utter_do_something_else
* negative
	- utter_bye
	- action_restart	
	
## book seminar without course specified at other loc or date
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
* inform{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* other_loc_date{"other_location":"True"}
	- action_show_all_buttons
* stop
	- action_deactivate_form
	- utter_do_something_else
	
## book seminar without course specified at other loc or date
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
* inform{"course": "Machine Learning"}
    - slot{"course": "Machine Learning"}
    - action_display_seminar
	- slot{"seminar_id":"7"}
    - slot{"locations": "Berlin, Frankfurt, Munich"}
    - slot{"title": "Machine Learning"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* other_loc_date{"other_date":"True"}
	- action_show_all_buttons
* stop
	- action_deactivate_form
	- utter_do_something_else
	
## book seminar date clash - cancel seminar yes
* book_seminar{"location": "Frankfurt"}
    - utter_ask_name
* inform{"given-name": "Teresa", "last-name": "Williams"}
    - slot{"given-name": "Teresa"}
    - slot{"last-name": "Williams"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 10}
	- action_display_seminar
	- slot{"categories":"[x,y,z]"}
	- utter_ask_course_book
* inform{"course": "Python"}
	- action_query_date
	- slot{"dates": "07/03/19, 21/03/19"}
    - slot{"title": "Python for beginners"}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 21", "time": "2019-03-21T00:00:00.000-07:00"}
    - slot{"date": "March 21"}
    - slot{"time": "2019-03-21T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 21"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"course": null}
	- slot{"time": null}
    - slot{"location": null}
	- slot{"course" : null}
	- slot{"date-period": null}
* cancel_seminar
	- utter_ask_course_cancel
	- action_show_bookings
	- slot{"date": null}
    - slot{"location": null}
	- slot{"date-period": null}
	- slot{"time": null}	
	- slot{"display-option": null}
	- slot{"booking-type": null}
* inform{"course": "Excel"} OR inform{"course":"Excel","date":"18/09/19"} OR inform{"course": "Excel", "location":"Munich"}
	- utter_are_you_sure
* affirm
	- action_cancel_seminar
	- slot{"cancellation_confirmed": "True"}
	- slot{"course": null}		
	- slot{"location": null}		
	- slot{"date": null}
	- slot{"time": null}
	
	
	
	

	
	
	
