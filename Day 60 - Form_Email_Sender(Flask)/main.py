from flask import Flask, render_template, request
import os
import smtplib
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

app = Flask(__name__)

@app.route('/')
def get_contact_form():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)


def send_email(name, email, phone, message):
    msg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(EMAIL, PASSWORD)
        conn.sendmail(EMAIL, EMAIL, msg)


if __name__ == "__main__":
    app.run(debug=True)