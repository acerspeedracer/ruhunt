from flask import Flask
from flask import render_template
import sendgrid

s = sendgrid.Sendgrid('ace6598','aiser12',secure=True)
app = Flask(__name__)

@app.route("/")
def index():
  return "index"

@app.route("/hello")
def hello():
  return "hello world"

@app.route("/user/<username>")
def create_user_page(username):
  return 'User: %s' % username

@app.route("/home")
def homepage():
	return render_template("home.html")

if __name__ == "__main__":
  app.run()
