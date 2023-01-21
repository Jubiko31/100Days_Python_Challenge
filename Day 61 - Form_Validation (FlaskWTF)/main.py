from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
import email_validator
import os

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345679":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)