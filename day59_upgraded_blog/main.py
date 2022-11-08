import requests
from flask import Flask, render_template
NPOINT_ENDPOINT = "https://api.npoint.io/247654de63813210b18c"
posts = requests.get(url=NPOINT_ENDPOINT).json()
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', all_posts=posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/post/<int:id>')
def blog_post(id):
  for post in posts:
    if post["id"] == id:
      return render_template('post.html', blog_post = post)

if __name__ == "__main__":
  app.run(debug=True)