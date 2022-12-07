from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from movie_search import MovieSearch
import pickle

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(200), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


class EditForm(FlaskForm):
    rating = StringField('Your Rating out of 10', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


def write_to_file(d: list) -> bool:
    try:
        with open("movies.pkl", "wb") as file:
            pickle.dump(d, file)
        return True
    except OSError:
        print("Could not open file movies.pcl")
        return False


def read_from_file() -> list:
    try:
        with open("movies.pkl", "rb") as file:
            movies_list = pickle.load(file)
        return movies_list
    except OSError:
        print("Could not open file movies.pcl")


### This is needed to initialize the database.  Add to the /home route if the database has not been created.
# def add_default_movie():
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, "
#                     "pinned down by an extortionist's sniper rifle. Unable to leave or "
#                     "receive outside help, Stuart's negotiation with the caller leads "
#                     "to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favorite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/")
def home():
    # all_movies = db.session.query(Movie).all()
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    edit_form = EditForm()  # FlaskForm object
    movie_id = request.args.get('id')  # Get 'id' parameter passed to url_for
    print(movie_id)
    if edit_form.validate_on_submit():
        movie = Movie.query.get(movie_id)
        movie.rating = float(edit_form.rating.data)
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        # print(add_form.title.data)
        movie_search = MovieSearch()
        movies = movie_search.search_movie(add_form.title.data)
        write_to_file(movies)
        movie_titles = []
        movie_index = 1
        for movie in movies:
            movie_titles.append((movie_index, movie['original_title']))
            movie_index += 1
        print(movie_titles)
        return render_template("add.html", form=add_form, movies=movie_titles)
    return render_template("add.html", form=add_form, movies=[])


@app.route("/add_movie")
def add_movie():
    indexed_movie = request.args.get('new_movie')
    print(indexed_movie)
    movie_list = read_from_file()
    movie = movie_list[int(indexed_movie) - 1]
    new_movie = Movie(
        title=movie["original_title"],
        year=int(movie['release_date'][:4]),
        description=movie["overview"],
        rating=movie['vote_average'],
        img_url=f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit'))


if __name__ == '__main__':
    app.run(debug=True)
