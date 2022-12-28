from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


# Initialize the flask_login manager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    logged_in=False
    if current_user.is_authenticated:
        logged_in = True
    return render_template("index.html", logged_in=logged_in)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User()
        user.name = request.form.get('name')
        user.email = request.form.get('email')
        user.password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8)
        db.session.add(user)
        db.session.commit()
        # return redirect(url_for('secrets', name=user.name))
        return redirect(url_for('login'))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        # check of the user exists, if not redirect to register route
        if user is None:
            flash("User does not exist.")
        # check if password is valid
        elif check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash('Please check your login credentials and try again.')

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    logged_in=False
    if current_user.is_authenticated:
        logged_in = True
    return render_template("secrets.html", name=current_user.name, logged_in=logged_in)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
