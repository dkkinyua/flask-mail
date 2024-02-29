from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
mail = Mail(app)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "denzelkinyua11@gmail.com"
app.config["MAIL_PASSWORD"] = os.getenv('EMAIL_PASS')


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        msg = Message("Hello", sender="demo@no-reply.com", recipients=['denzelkinyua11@gmail.com'])
        msg.body = "Hello, this is a test email."
        mail.send(msg)
        return "Email sent successfully!"
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
