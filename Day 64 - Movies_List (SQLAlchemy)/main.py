from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import requests

MOVIE_DB_SEARCH_URL = os.getenv('MOVIE_DB_SEARCH_URL')
MOVIE_DB_API_KEY = os.getenv('MOVIE_DB_API_KEY')
MOVIE_DB_URL = os.getenv('MOVIE_DB_URL')
MOVIE_DB_IMAGE = os.getenv('MOVIE_DB_IMAGE')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
                        
    def __repr__(self):
        return f'<Movie {self.title}'
    
class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("ADD")

class RateForm(FlaskForm):
    rating = StringField("Rating out of 10")
    review = StringField("Review")
    submit = SubmitField("Done")

db.create_all()

@app.route("/")
def home():
    movies = Movies.query.all()
    for idx in range(len(movies)):
        movies[idx].ranking = len(movies) - idx
    db.session.commit()
    return render_template("index.html", movie=movies)

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        res = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = res.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = RateForm()
    mid = request.args.get("id")
    movie = Movies.query.get(mid)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete():
    mid = request.args.get("id")
    movie = Movies.query.get(mid)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        api = f"{MOVIE_DB_URL}/{movie_api_id}"
        res = requests.get(api, params = { "api_key": MOVIE_DB_API_KEY })
        data = res.json()
        new_movie = Movies(
            title = data["title"],
            year = data["release_date"].split("-")[0],
            img_url = f"{MOVIE_DB_IMAGE}{data['poster_path']}",
            description = data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    
if __name__ == '__main__':
    app.run(debug=True)

