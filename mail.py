from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
mail = Mail(app)

app.config["MAIL_SERVER"] = 'smtp.office365.com'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.getenv("EMAIL_USER")
app.config["MAIL_PASSWORD"] = os.getenv('EMAIL_PASS')


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        msg = Message("Hello", sender="demo@no-reply.com", recipients=['denzoooo@outlook.com'])
        msg.body = "Hello, this is a test email."
        mail.send(msg)
        return "Email sent successfully!"
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
