from flask import Flask
app = Flask(__name__)  # run flask from current script, ie __name__ == __main__

@app.route('/')  # trigger decorator only if user is attempting to access URL home
def hello_world():
    return 'Hello World!'

@app.route('/bye')  # trigger decorator only if user accesses URL /bye
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()   # equivalent to 'flask run' in terminal