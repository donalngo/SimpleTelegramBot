# SimpleTelegramBot

Have initially built this for a stock bot project. I have made this bot modular so that it is easy for users to add, edit utterances and slots based on their own requirements.

This bot complies and trains on itself upon initialization.

Detection of Intent and Slots uses SVM and CRF respectively.

Building of the bot is still in progress. 


Installation
-------------
1) Creating Environment
	- conda create -n venv python=3.7 scikit-learn pandas numpy pickle nltk itertools spacy
2) Activating Environment
	- conda activate venv
3) Installing other packages
	- pip install python-telegram-bot pycrfsuite 
	- python -m spacy download en_core_web_sm
	
	### USE THE FOLLOWING ONLY IF YOU NEED TO EDIT TRAINING PHRASES 
	- pip install snips-nlu 


Running the Bot
---------------
1) Edit run.py
	- Change TokenKey = "your own token key"
2) Use cmd and execute python run.py


Editing the Training Utterance/Slots
------------------------------------
1) Make sure that snips-nlu is installed
2) Go to Dataset/YAML folder
3) Create YAML File with the format provided (use smalltalk.yaml, intent should be groupname_intent)
4) Converting YAML to JSON
	Command line: 
<pre><code>snips-nlu generate-dataset en dataset.yaml > dataset.json</pre></code>
5) Cut Json file to Dataset/Converted
6) Go to Training/Training.py
7) Find and edit:
<pre><code>
	def train():
            trainingfile = "Dataset\\Converted\\yourfile.json"
	    intentdataset(trainingfile)
	    slotdetection(trainingfile)
	    </pre></code>
8) Training will automatically run when run.py is initiated


Editing Response based on Intent
---------------------------------
1) Response is Grouped by groupname in different py files, for smalltalk, smalltalk.py etc.
	Refer to utils\utterance.py getreply function for reference
2) Function names should be the same as intent



Files and Folders Orientation
-------------------------------
1) Folders
	- conversation
		Where all the responses are stored
	- Dataset
		Where all training data YAML/JSON files are stored
	- models
		Where all the trained models are deposited
	- Slotsfill ( In progress )
		Intended for slot request and replies
	- Training
		Script to train models
	- utils
		Script which handles Conversations

2) Files
	- Conversation/smalltalk.py
		- Handles all smalltalk replies
	- Conversation/fallback.py
		- Handles all fallback replies
	- Training/Training.py
		- Trains models for an intelligent chatbot
	- Utils/slots.py
		- Slots detection script ( In Progress )
	- Utils/utterance.py
		- Intent detection script( In Progress )
		- Handles Intent to Responses and slot filling
	- ./run.py
		- Trains Model on initialization
		- Stores Global Variables
		- Interface with Telegram
		- Interface with utterance.py


