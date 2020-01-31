
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
 
