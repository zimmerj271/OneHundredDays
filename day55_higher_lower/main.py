from flask import Flask
from random import randint
app = Flask(__name__)  # run flask from current script, ie __name__ == __main__

CORRECT_NUMBER = randint(1, 9)

@app.route('/')  # trigger decorator only if user is attempting to access URL home
def hello_world():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<img style="display: block; margin: 0 auto;" ' \
           'src=https://media1.giphy.com/media/l378khQxt68syiWJy/giphy.gif?cid=ecf05e47b42mamlw4mefxfz7w1s58fi5yxohuh4rbtstv6j4&rid=giphy.gif&ct=g>'

@app.route("/<int:number>")
def greet(number):
    if number > CORRECT_NUMBER:
        message = "<h2 style='color: red'>Too high, try again!</h2>"
        gif_url = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    elif number < CORRECT_NUMBER:
        message = "<h2 style='color: green'>Too low, try again!</h2>"
        gif_url = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    else:
        message = "<h2 style='color: orange'>You found me!</h2>"
        gif_url = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
    return f"{message}<img src={gif_url}>"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)