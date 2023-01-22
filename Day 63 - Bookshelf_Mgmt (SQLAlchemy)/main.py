from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Book {self.title}'

db.create_all()

@app.route('/')
def home():
    books = db.session.query(Book).all()
    return render_template('index.html', books=books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title = request.form["title"],
            author = request.form["author"],
            rating = request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        bid = request.form["id"]
        book = Book.query.get(bid)
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    bid = request.args.get('id')
    selected = Book.query.get(bid)
    return render_template("edit-rating.html", book=selected)

@app.route("/delete")
def delete():
    bid = request.args.get('id')
    book = Book.query.get(bid)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
    