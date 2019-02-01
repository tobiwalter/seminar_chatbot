# seminar_chatbot

#intents
  - get_descripiton: Get information about the contents of a course (e.g. What are the contents of Machine Learning?)
  - get_general_info: Get general info about the offering (e.g. Do you offer Machine Learning courses?)
  - inform: user reply to a question concerning name, date, loc etc.
  - bad: user expresses dissatisfaction
  - book_seminar
  - get_help
  - show_bookings
  - bye
  - welcome
  - cancel_seminar
  - affirm
  - get_dates: get dates of a seminar
  - introduction: user wants to do smalltalk with the bot 
  - age: smalltalk
 
#actions
- action_show_bookings
- utter_get_help
- utter_ask_course
- action_provide_prerequisites: Queries prerequisites of a course in database and presents to user
- utter_bye
- action_course_offering: Retrieves and presents all categories in which seminars are available to user  
- utter_welcome:
- utter_are_you_sure: Ask for confirmation from user before cancelling a seminar
- utter_submit: part of seminar_form
- utter_chitchat: reply if user wants to do smalltalk/chitchat
- utter_i''m sorry: reply to bad intent 
- action_select_date: 
- action_cancel_seminar
- action_display_seminar: displays all locations and dates of a specific seminar
- utter_ask_name: asks for full name
- utter_ask_date: part of seminar_form
- action_book_seminar
- utter_ask_location: part of seminar_form
- utter_try_again: prompts user to try again if user verification fails
- action_provide_description: Retrieves a seminar's description 
- action_verify_user: verifies user - looks up provided name and surname and fills a slot employee_id if successful 
- utter_no_worries: answer to thank intent 
  
