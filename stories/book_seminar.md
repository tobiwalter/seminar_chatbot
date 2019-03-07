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
    - slot{"location": null}
	
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
    - slot{"location": null}
	
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
    - slot{"location": null}
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
    - slot{"location": null}
	
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
    - slot{"location": null}
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
    - slot{"location": null}
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
    - slot{"location": null}
	
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
    - slot{"location": null}
	
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
    - slot{"location": null}

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
    - slot{"location": null}

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
    - slot{"location": null}
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
    - slot{"location": null}
	
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
    - slot{"location": null}
	
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
    - slot{"location": null}		

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
    - slot{"location": null}
	
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
    - slot{"location": null}
	
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
    - slot{"location": null}

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
	
## requesting location in the middle
* book_seminar
    - utter_ask_name
* inform{"given-name": "Max", "last-name": "Thompson"}
    - slot{"given-name": "Max"}
    - slot{"last-name": "Thompson"}
    - action_verify_user
    - slot{"user_verified": "True"}
    - slot{"employee_id": 3}
    - action_course_offering
    - utter_ask_course_book
* inform{"course": "leadership"}
    - slot{"course": "leadership"}
    - action_display_seminar
    - slot{"locations": "Cologne, Frankfurt, Stuttgart"}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
    - seminar_form
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Berlin"}
    - slot{"location": "Berlin"}
    - form: seminar_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* get_location
    - action_display_seminar
    - action_listen
    - slot{"locations": "Cologne, Frankfurt, Stuttgart"}
    - slot{"title": "Leadership Behaviour"}
    - slot{"seminar_id": 4}
* form: inform{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - seminar_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Cologne"}
    - slot{"location": "Cologne"}
    - form: seminar_form
    - slot{"location": "Cologne"}
    - slot{"requested_slot": "date"}
* form: inform{"date": "March 24", "time": "2019-03-24T00:00:00.000-07:00"}
    - slot{"date": "March 24"}
    - slot{"time": "2019-03-24T00:00:00.000-07:00"}
    - form: seminar_form
    - slot{"date": "March 24"}
    - form{"name": null}
    - slot{"requested_slot": null}
	- action_book_seminar
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}

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
    - slot{"course": "machine learning"}
    - slot{"location": "Berlin"}
    - utter_ask_name
* inform{"given-name": "Jane", "last-name": "Love"}
    - slot{"given-name": "Jane"}
    - slot{"last-name": "Love"}
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
    - slot{"location": null}
* book_seminar{"course": "leadership", "location": "Cologne"}
    - slot{"course": "leadership"}
    - slot{"location": "Cologne"}
    - slot{"course": "leadership"}
    - slot{"location": "Cologne"}
	- action_query_date
    - slot{"dates": "18/03/19, 26/03/19"}
    - slot{"title": "Leadership Behaviour"}
    - seminar_form   
    - form{"name": "seminar_form"}
    - slot{"requested_slot": "date"}
    - slot{"date": "Feb 24"}
    - slot{"date": "Feb 24"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_book_seminar   <!-- predicted: action_listen -->
    - slot{"booking_confirmed": "True"}
    - slot{"date": null}
    - slot{"location": null}
	
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
    - slot{"location": null}
	
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
    - slot{"date": null}
    - slot{"location": null}
	
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
    - slot{"location": null}

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
    - slot{"location": null}
	
## book seminar verification fails	
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
    - slot{"location": null}
	
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