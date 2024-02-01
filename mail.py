from flask import Flask
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os


app = Flask(__name__)
mail = Mail(app)

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True


load_dotenv()

@app.route('/', methods=['POST', 'GET'])
def send_mail():
    msg = Message('Hello, this is a test program to send out emails', sender='demo@company.com', recipients=[os.getenv('RECIPIENT_EMAIL')])
    mail.send(msg)



if __name__ == '__main__':
        app.run(debug=True)