from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create a mixin class to pass the same method to multiple database classes
class TableToDictMixin:
    def as_dict(self):
        # Use getattr to get the object's class attribute as the value for the dictionary
        # self.__table__ references the database table ar
        # columns will return in the format myTable.col1 (ie table name is included)
        # To just get the column name, use .keys()
        # returns: for each column name in table, return column name: associated class attribute value pair.
        return {item: getattr(self, item) for item in self.__table__.columns.keys()}


##Cafe TABLE Configuration
class Cafe(db.Model, TableToDictMixin):
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


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")  # GET is default on all routes
def random_cafe():
    cafes = db.session.query(Cafe).all()
    cafe = random.choice(cafes)  # Cafe database object
    cafe_dict = cafe.as_dict()  # convert to dictionary
    return jsonify(cafe=cafe_dict)


@app.route("/all")
def all_cafes():
    cafes = Cafe.query.all()
    # all_cafes = [cafe.as_dict() for cafe in cafes]  # returns list of dictionaries
    all_cafes = {c.name: c.as_dict() for c in cafes}  # returns dictionary with names of cafes as keys
    return jsonify(cafes=all_cafes)


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc").title()
    cafe = Cafe.query.filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.as_dict())
    else:
        error_message = {"Not Found": "Sorry, we don't have a location at that location"}
        return jsonify(error=error_message)

## HTTP POST - Create Record
@app.route("/add", methods=['GET', 'POST'])
def add_cafe():
    add_cafe = request.args.get("add")


## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
