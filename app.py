from flask import Flask
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

if __name__ == "__main__":
  app.run()
