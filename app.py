from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from flask import render_template
from flask import request
#import sendgrid

#s = sendgrid.Sendgrid('ace6598','aiser12',secure=True)
app = Flask(__name__)

@app.route("/")
def index():
  return "index"

@app.route("/email",methods=["POST"])
def email():
	return "",200

@app.route("/hello")
def hello():
  return "hello world"

@app.route("/user/<username>")
def create_user_page(username):
  return 'User: %s' % username

@app.route("/home")
def homepage():
	return render_template("home.html")
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/about")
def about():
	return render_template("about.html")
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
  app.run()
