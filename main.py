from tokens import telegram_token
import requests
from flask import Flask, request, Response
import json
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

def write_JSON(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 4, ensure_ascii = False)

def parse_message(msg):
    chat_id = msg['message']['chat']['id']
    message_text = msg['message']['text']
    print(message_text)
    return message_text, chat_id

def send_message(text, chat_id):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={text}'
    requests.post(url)


@app.route('/', methods = ['POST','GET'])
def Index():
    if request.method == 'POST':
        try:
            msg = request.get_json()
            message_text, chat_id = parse_message(msg)
            send_message('hello', chat_id)
            return Response('ok', status=200)
        except:
            return Response('ok', status=200)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)
