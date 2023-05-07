# langchain_dj_gpt
Created a langchain dj gpt agent thanks to lablabai workshops guided by Hai Nghiem
<<<<<<< HEAD

Technologies used: Langchain React Agent, Spotipy and spotify api

## REACT AGENT
RE- Reasoning
ACT - Act after reasoning

# Pre-Requisites
## Setup your Spotify App
Go to developer.spotify.com
Create new app and obtain the clientID and client secret from the basic information tab
Other fields include redirect url

## Obtain the Open API key
Go to the openai official page and obtain an API key

# File structure
## consts.py
Stores all the constants needed in your app e.g The llm model to be used 

## ai_agents.py
Here we build functions to initialize our langchain agent

## spotify.py
We connect to our spotify and create helper functions that will be used in our tools

## ai_tools.py
Utilize our helper functions to create tools to be used by our AGENT

## main.py
Used to run our langchain dj gpt agent

# How to run it
clone the repo
create a virtual environment
pip install -r requirements.txt
create a .env folder to store all your api keys and secretive information that you don't wanna share 
then run the main.py
=======
>>>>>>> d10752875ae091645fe49003dfc9e8d2d291fa8b
