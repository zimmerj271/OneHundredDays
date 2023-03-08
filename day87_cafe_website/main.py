from flask import Flask, jsonify, render_template, url_for, flash, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_bootstrap import Bootstrap
from forms import AddCafeForm, RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import random
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

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


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)


# ##WTForm
# class CreatePostForm(FlaskForm):
#     title = StringField("Blog Post Title", validators=[DataRequired()])
#     subtitle = StringField("Subtitle", validators=[DataRequired()])
#     author = StringField("Your Name", validators=[DataRequired()])
#     img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
#     submit = SubmitField("Submit Post")


with app.app_context():
    db.create_all()

# Initialize the flask_login manager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)  # return route function if admin
    return decorated_function


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    registration_form = RegisterForm()
    if registration_form.validate_on_submit():
        encrypted_password = generate_password_hash(
            registration_form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            name=registration_form.name.data,
            email=registration_form.email.data,
            password=encrypted_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('get_cafes'))
    return render_template("register.html", form=registration_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()
        if user is None:
            flash("User does not exist.")
        elif check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('get_cafes'))
        else:
            flash("Please check your login credentials and try again.")
    return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

# HTTP GET - Read Record
@app.route("/random")  # GET is default on all routes
def random_cafe():
    cafes = db.session.query(Cafe).all()
    cafe = random.choice(cafes)  # Cafe database object
    cafe_dict = cafe.as_dict()  # convert to dictionary
    return jsonify(cafe=cafe_dict)


@app.route("/cafes")
def get_cafes():
    cafes = Cafe.query.all()
    all_coffee_shops = [cafe.as_dict() for cafe in cafes]  # returns list of dictionaries
    print(all_coffee_shops)
    return render_template("cafes.html", cafes=all_coffee_shops)


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc").title()
    cafe = Cafe.query.filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.as_dict())
    else:
        error_message = {"Not Found": "Sorry, we don't have a location at that location"}
        return jsonify(error=error_message)


## HTTP POST
@app.route("/cafe/<int:cafe_id>", methods=['GET', 'POST'])
def get_store(cafe_id):
    requested_cafe = Cafe.query.get(cafe_id)
    return render_template("store.html", cafe=requested_cafe, current_user=current_user)

# This route will be tested in Postman by creating a POST submission
# Be sure to select "Body" under the URL route, then the radio button
# "x-www-form-urlencoded".  Then enter the key/value pairs for all the
# entries to add a new cafe to the database.
@app.route("/add", methods=['GET', 'POST'])
def add_cafe():
    # Create a new Cafe object
    form = AddCafeForm()
    if form.validate_on_submit():
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
        return redirect(url_for('get_store', cafe_id=new_cafe.id))
    return render_template("add_cafe.html", form=form, edit_cafe=False)


@app.route("/edit-cafe/<int:id>", methods=['GET', 'POST'])
def edit_cafe(id):
    cafe = Cafe.query.get(id)
    form = AddCafeForm(
        name=cafe.name,
        map_url=cafe.map_url,
        img_url=cafe.img_url,
        location=cafe.location,
        has_sockets=cafe.has_sockets,
        has_toilet=cafe.has_toilet,
        has_wifi=cafe.has_wifi,
        can_take_calls=cafe.can_take_calls,
        seats=cafe.seats,
        coffee_price=cafe.coffee_price
    )
    if form.validate_on_submit():
        cafe.name = form.name.data
        cafe.map_url = form.map_url.data
        cafe.img_url = form.img_url.data
        cafe.location = form.location.data
        cafe.has_sockets = bool(form.has_sockets.data)
        cafe.has_toilet = bool(form.has_toilet.data)
        cafe.has_wifi = bool(form.has_wifi.data)
        cafe.can_take_calls = bool(form.can_take_calls.data)
        cafe.seats = form.seats.data
        cafe.coffee_price = form.coffee_price.data
        db.session.commit()
        return redirect(url_for('get_store', cafe_id=id))
    return render_template("add_cafe.html", form=form, edit_cafe=True)


@app.route("/report-closed/<int:id>")
def remove_cafe(id):
    cafe = Cafe.query.get(id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for("get_cafes"))


if __name__ == '__main__':
    app.run(debug=True)
