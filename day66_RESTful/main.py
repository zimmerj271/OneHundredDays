from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random

# API documentation found at https://documenter.getpostman.com/view/24993269/2s8YzZRf28
api_documentation = "https://documenter.getpostman.com/view/24993269/2s8YzZRf28"

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
# This route will be tested in Postman by creating a POST submission
# Be sure to select "Body" under the URL route, then the radio button
# "x-www-form-urlencoded".  Then enter the key/value pairs for all the
# entries to add a new cafe to the database.
@app.route("/add", methods=['POST'])
def add_cafe():
    # Create a new Cafe object
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)  # add the Cafe object to the session
    db.session.commit()  # commit the changes to the database
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
# Example API route: /update-price/22?new_price=$5
@app.route("/update-price/<int:id>", methods=['PATCH'])
def update_price(id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.get(id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        # return success json and HTTP code 200
        return jsonify(response={"success": f"Price of cafe {id} updated successfully."}), 200
    else:
        # return error json and HTTP code 404
        return jsonify(error={"Not found": f"Cafe {id} was not found."}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>", methods=['DELETE'])
def remove_cafe(id):
    api_key = request.args.get("api-key")
    cafe = Cafe.query.get(id)
    if not cafe:
        return jsonify(error={"Not found": f"Cafe {id} was not found."}), 404
    if api_key == "YourBaseBelongToUs":
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"succes": f"Cafe {id} successfully removed."}), 200
    else:
        return jsonify(forbidden={"forbidden": "You do not have access."}), 403

## DOCUMENTATION
@app.route("/docs")
def get_docs():
    return redirect(api_documentation)

if __name__ == '__main__':
    app.run(debug=True)
