from flask import Flask, render_template, request
from twilio.rest import Client
import csv
import os


app = Flask(__name__)

# Your Account SID from twilio.com/console
account_sid = os.environ.get('SID')
# Your Auth Token from twilio.com/console
auth_token = os.environ.get('TOKEN')
client = Client(account_sid, auth_token)


@app.route('/')
def hello_world():
    return '404'


@app.route('/sms')
def sms_sender():
    return render_template('index.html')

@app.route('/mms')
def mms_sender():
    return render_template('index2.html')

@app.route('/sendsms', methods=['GET', 'POST'])
def send_sms():
    if request.method == 'POST':
        t = request.form["smsInput"].encode('utf-8')
        f = request.files["fileUpload"]
        file_data = f.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            try:
                field = line.split(",")
                client.api.account.messages.create(
                    from_="+16782646688",
                    to=field[0],
                    body=t)
            except Exception:
                pass
    return 'sent'

@app.route('/sendmms', methods=['GET', 'POST'])
def send_mms():
    if request.method == 'POST':
        m = request.form["mediaURL"].encode('utf-8')
        f = request.files["fileUpload"]
        file_data = f.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            try:
                field = line.split(",")
                client.api.account.messages.create(
                    from_="+16782646688",
                    to=field[0],
                    body='',
                    media_url=m)
            except Exception:
                pass
    return 'sent'

if __name__ == '__main__':
    app.run()
