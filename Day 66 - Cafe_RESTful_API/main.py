from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dictionary(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")
   
@app.route("/all")
def get_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes = [cafe.to_dictionary() for cafe in cafes]) 
    
@app.route("/random-cafe")
def random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe = random_cafe.to_dictionary()), 200

@app.route("/search")
def search_cafe():
    query_loc = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_loc).first()
    if cafe:
        return jsonify(cafe = cafe.to_dictionary()), 200
    else:
        return jsonify(error={"Not Found": "Cafe not found at that location."}), 404

@app.route("/add", methods=["POST"])
def add_new_cafe():
    cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("loc"),
        has_sockets = bool(request.form.get("sockets")),
        has_toilet = bool(request.form.get("toilet")),
        has_wifi = bool(request.form.get("wifi")),
        can_take_calls = bool(request.form.get("calls")),
        seats = request.form.get("seats"),
        coffee_price = request.form.get("coffee_price"),
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 201

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = price
        db.session.commit()
        return jsonify(response={"success": "Cafe price was updated successfully"}), 200
    else:
        return jsonify(error={"Not Found": "Invalid cafe id."}), 404

@app.route("/close/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "GiveMeCoffee":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Cafe deleted successfully."}), 200
        else:
            return jsonify(error={"Not Found": "Invalid cafe if."}), 404
    else:
        return jsonify(error={"Forbidden": "Invalid api key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
