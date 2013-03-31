from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from flask import render_template
from flask import request
#import sendgrid

#s = sendgrid.Sendgrid('ace6598','aiser12',secure=True)
app = Flask(__name__)

@app.route("/email",methods=["POST"])
def email():
	f = open("/var/www/ruhunt/data/%s"%request.form['text'].splitlines()[0],"w")
	f.write("%s\n%s"%(request.form['subject'],'\n'.join(request.form['text'].splitlines())))
	f.close()
	request.files.get(request.form['attachment1']['name']).save("/var/www/ruhunt/templates/thumbs/%s.png"%hashlib.md5().update(request.form['text'].splitlines()[0]).hexdigest())
	return "",200

@app.route("/hello")
def hello():
  return "hello world"


@app.route("/user/<username>")
def create_user_page(username):
  return 'User: %s' % username

@app.route("/home")
@app.route("/")
def homepage():
	return render_template("home.html")
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/about")
def about():
	return render_template("about.html")
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
  app.run()
