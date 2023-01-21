from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import os
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
Bootstrap(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a") as file:
            file.write(f"\n{form.cafe.data},"
                        f"{form.location.data},"
                        f"{form.open.data},"
                        f"{form.close.data},"
                        f"{form.coffee_rating.data},"
                        f"{form.wifi_rating.data},"
                        f"{form.power_rating.data}"
                        )
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as file:
        data = csv.reader(file, delimiter=',')
        print(data)
        cafe_list = []
        for row in data:
            cafe_list.append(row)
    return render_template('cafes.html', cafes=cafe_list)

if __name__ == '__main__':
    app.run(debug=True)
