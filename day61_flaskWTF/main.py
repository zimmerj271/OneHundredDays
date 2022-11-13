from flask import Flask, render_template
from forms import LoginForm
from flask_bootstrap import Bootstrap


user_credentials = {
    'email': 'admin@email.com',
    'password': 'easy'
}
app = Flask(__name__)
app.config['SECRET_KEY'] = '2c3eee956c6c17196352e3015e6c96d3'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == user_credentials['email'] and form.password.data == user_credentials['password']:
            return render_template('success.html', title='Logged In')
        else:
            return render_template('denied.html', title='Rick Rolled!')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
