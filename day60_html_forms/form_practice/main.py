from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
  username = request.form['username']
  password = request.form['password']
  return f"<h1>Username: {username}, password: {password}"

if __name__ == "__main__":
  app.run(debug=True)