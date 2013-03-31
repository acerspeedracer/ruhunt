from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from flask import render_template
from flask import request
import hashlib
import json
import cv
#import sendgrid

def detect(img, cascade):
	rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10), flags = cv.CV_HAAR_SCALE_IMAGE)
	if len(rects) == 0:
		return []
	rects[:,2:] += rects[:,:2]
	return rects

def resize(imgpath) :
	try:
		img = cv2.imread(imgpath,cv2.CV_LOAD_IMAGE_COLOR)  
		if (img == None):                                      
			print "Could not open or find the image"
		else:
			cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
			gray = cv2.cvtColor(img, cv.CV_BGR2GRAY)
			gray = cv2.equalizeHist(gray)

			rects = detect(gray, cascade)
		
			x1 = rects[0][1]
			y1 = rects[0][0]
			x2 = rects[0][3]
			y2 = rects[0][2]
			cropped = img[x1:x2, y1:y2]
			cv2.imwrite(imgpath+"dd", cropped)
	except Exception as inst:
		f = open("~/test","w")
		f.write(str(type(inst)))
		f.close()

#s = sendgrid.Sendgrid('ace6598','aiser12',secure=True)
app = Flask(__name__)

@app.route("/email",methods=["POST"])
def email():
	f = open("/var/www/ruhunt/data/%s"%request.form['text'].splitlines()[0],"w")
	f.write("%s\n%s"%(request.form['subject'],'\n'.join(request.form['text'].splitlines())))
	nm = "/var/www/ruhunt/templates/thumbs/%s.png"%request.form['text'].splitlines()[0]
	f.close()
	f = open("/var/www/ruhunt/data/namepairs","wa")
	f.write("%s\t%s\n"%(request.form['subject'],request.form['text'].splitlines()[0]))
	f.close()
	request.files['attachment1'].save(nm)
	resize(nm)
	return "",200

@app.route("/hello")
def hello():
  return "hello world"


@app.route("/user/<username>")
def create_user_page(username):
  return 'User: %s' % username


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
  app.run(debug=True)
