from flask import Flask, request

import requests

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def hello_world():

    f = request.get_json(force=True)

    name = f['name']
    email = f['email']
    message = f['message']

    requests.get(
        f"https://api.telegram.org/bot6664967345:AAHNTpkk9xUYFzz-oOoUWXHwZZGMIHFcBG4/sendMessage?chat_id=5501736457&text={name}+{email}+{message}")

    return 'Hello from Flask!'


    app.run(debug=True)
