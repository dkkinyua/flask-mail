from flask import Flask
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
mail = Mail()

app.config["MAIL_SERVER"] = 'smtp.fastmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.getenv("EMAIL_USER")
app.config["MAIL_PASSWORD"] = os.getenv('EMAIL_PASS')

mail.init_app(app)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    msg = Message("Hello", sender="deecodes@fastmail.com", recipients=["denzelkinyua11@gmail.com"])
    msg.body = "This is a test email, ignore"
    mail.send(msg)
    return "Email sent successfully!"

if __name__ == "__main__":
    app.run(debug=True)

