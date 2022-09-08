from crypt import methods
from importlib.resources import path
from flask import Flask, redirect, url_for, request, render_template, session
from dotenv import load_dotenv
import requests, os, uuid, json

# Load values from the .env config file into os.environ dictionary
load_dotenv()
# Initializes the Flask app
app = Flask(__name__)

# Assign the index method to answer GET requests to the / endpoint 
# The method returns the index.html template located inside the templates folder 
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Assign the index_post method to answer POST requests to the / endpoint 
@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']

    # Load the values from .env
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    # Indicate that we want to translate
    path = '/translate'
    # Create the full URL
    constructed_url = endpoint + path

    # Indicate the api version and the target language
    params = {
        'api-version': '3.0',
        'to': target_language
    }

    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Create the body of the request with the text to be translated
    body = [{
        'text': original_text
    }]

    # Make the call using POST
    translator_request = requests.post(constructed_url, params=params, headers=headers, json=body)
    # Retrieve the JSON response
    translator_response = translator_request.json()
    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    # Call render template, passing the translated text, 
    # original text, and target language to the template
    return render_template(
        'results.html',
        translated_text = translated_text,
        original_text = original_text,
        target_language = target_language
    )
    