We conceptualized and implemented a chatbot that serves employees in booking seminars, managing seminar bookings and retrieving information about the seminar catalogue. 

The core of our architecture is the Rasa Stack consisting of the two components Rasa NLU and Rasa Core. Rasa NLU takes on the task of classifying user intents and extracting relevant entities from the user input. The NLU unit passes the intent and extracted entities to Rasa Core which is responsible for managing the dialogue, i.e. predicting the bot’s next action. 

With the aid of Rasa Core SDK an action server is built up that allows the bot to perform actions beyond outputting a simple text utterance. Custom actions that require some form of calculation, read/write access to a database or the like can be written with this Python SDK and are accessible by providing an action endpoint, that will be called by Rasa Core whenever a custom action is predicted. For storing and manipulating data, we establish a connection between our Firebase Realtime Database instance and the action server. On the frontend side, we use the chat platform Slack. It provides an API that sends user input from Slack to the Rasa server and vice versa. We run the Rasa server locally on our machine and set up a tunnel with ngrok to route all incoming HTTP requests to the specified port.

In graphic form: 
![alt text](https://github.com/tobiwalter/seminar_chatbot/blob/master/architecture.png "Architecture")

## Sam - The seminar chatbot

To train the Rasa NLU model: 
```
python -m rasa_nlu.train -c config_tf.yml --data data\nlu_data -o models\current --fixed_model_name seminarnlu --project nlu --verbose
```

To train the Rasa Core model:
```
python -m rasa_core.train -d domain.yml -s stories -o models\dialogue_final -c policies_core.yml --augmentation 0
```

To load both Rasa NLU and Rasa Core models and launch assistant in the console to chat:
```
python -m rasa_core.run -d models\dialogue_final --nlu models\nlu_final\seminarnlu --endpoints endpoints.yml
```

To start custom actions server:
```
python -m rasa_core_sdk.endpoint --actions actions
```

Run duckling server in Docker:
```
docker run -p 8000:8000 rasa/duckling
```

To run bot in Slack:

1) Start actions and Duckling servers

2) Load bot agent and create Slack input channel by running this app:
```
python run_app.py
```
2) Create local webhook with ngrok e.g. on port 5002
```
ngrok http 5004
```
3) https://api.slack.com/apps --> Event subscriptions: Insert http adress as request URL that receives POST requests when events on Slack occur (e.g. https://ff6af049.ngrok.io/webhooks/slack/webhook) 

4) https://api.slack.com/apps --> Interactive Components: Insert the same adress as request URL here, so button interactions etc. are tracked

5) Start chatting with Sam


## Overview of the files

`stories` - contains stories for Rasa Core

`data/nlu_data/` - contains example NLU training data

`models` - contains final dialogue and NLU model

`domain.yml` - the Core config file 

`config_tf.yml` - the NLU config file

`policies_core.yml` - the Core config file

`endpoints.yml` - endpoint for action server

`service_account_key.json` - credentials for Firebase 

`actions.py` - code for custom actions

`helpers.py` - helper functions 
 
`run_app.py` - app that initiates bot agent and slack channel
 
