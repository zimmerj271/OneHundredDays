from flask import Flask, render_template
from random import randint
from datetime import date
import requests

GENDERIZE_ENDPOINT = "https://api.genderize.io"
AGIFY_ENDPOINT = "https://api.agify.io"

app = Flask(__name__)

@app.route('/')
def home():
    random_number = randint(1, 100)
    return render_template('index.html', random_number=random_number, year=date.today().year, name="Justin Zimmerman")

@app.route("/guess/<name>")
def guess(name: str):
    _name = name.title()
    genderize_response = requests.get(url=GENDERIZE_ENDPOINT, params={"name": _name})
    agify_response = requests.get(url=AGIFY_ENDPOINT, params={"name": _name})
    gender_data = genderize_response.json()
    age_data = agify_response.json()
    gender = gender_data["gender"]
    age = age_data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(all_posts)
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


