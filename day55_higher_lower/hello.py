from flask import Flask
app = Flask(__name__)  # run flask from current script, ie __name__ == __main__

def make_bold(function):
    def wrapper():
        string = function()
        return f"<em><b>{string}</b></em>"
    return wrapper

@app.route('/')  # trigger decorator only if user is attempting to access URL home
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<iframe src="https://giphy.com/embed/W0crByKlXhLlC" width="480" height="360" frameBorder="0"' \
           ' class="giphy-embed" allowFullScreen></iframe>' \
           '<p><a href="https://giphy.com/gifs/star-trek-picard-W0crByKlXhLlC">via GIPHY</a></p>'

# Different routes usingthe app.route decorator
@app.route('/bye')
@make_bold
def say_bye():
    return "Bye"

# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, welcome to page {number}!"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)