import smtplib
import requests
from flask import Flask, render_template, request
NPOINT_ENDPOINT = "https://api.npoint.io/247654de63813210b18c"
posts = requests.get(url=NPOINT_ENDPOINT).json()

def send_email(data):
    my_email = "vikingsmash@yahoo.com"
    password = "qgyxtfldhrwczwiw"
    smtp_server = "smtp.mail.yahoo.com"
    msg = f"Subject:Blog Message\n\nFrom: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage:\n{data['message']}"
    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', all_posts=posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
  if request.method == "POST":
    data = request.form
    send_email(data)
    return render_template('contact.html', msg_sent = True)
  else:
    return render_template('contact.html', msg_sent = False)

@app.route('/post/<int:id>')
def blog_post(id):
  for post in posts:
    if post["id"] == id:
      return render_template('post.html', blog_post = post)

if __name__ == "__main__":
  app.run(debug=True)