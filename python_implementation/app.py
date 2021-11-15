import os
from dotenv import load_dotenv
load_dotenv()

import requests
from flask import Flask, request, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def health_check():
    return {'msg': 'Application is running'}


@app.route('/webhook', methods=['GET'])
@cross_origin()
def verify_token():
    VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode and token:

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            print('WEBHOOK_VERIFIED')
            return challenge
    
    abort(403)


@app.route('/webhook', methods=['POST'])
@cross_origin()
def handle_message():
    try:
        body = request.json
    
        if body['object'] == 'page':

            for entry in body['entry']:
                webhook_event = entry['messaging'][0]
                message = webhook_event['message']['text']
                recipient = webhook_event['sender']['id']
                send_message(message, recipient)
            
            return 'EVENT_RECEIVED'
        return 'EVENT_RECEIVED'
        
    except:
        return 'EVENT_RECEIVED'

def send_message(message, recipient):
    PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN')

    body = {
        "messaging_type": "RESPONSE",
        "recipient": {
        "id": recipient,
        },
        "message": {
        "text": message,
        },
    }
    url = f'https://graph.facebook.com/v12.0/me/messages?access_token={PAGE_ACCESS_TOKEN}'

    response = requests.post(url, json = body)
    print(response.text)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3456, debug=True)
