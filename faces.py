import cv2
import cv2.cv as cv
import sys

def detect(img, cascade):
	rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10), flags = cv.CV_HAAR_SCALE_IMAGE)
	if len(rects) == 0:
		return []
	rects[:,2:] += rects[:,:2]
	return rects

if __name__ == '__main__':
	if len(sys.argv) != 2:                                         
		print "Usage : python faces.py <image_file>"

	else:
		img = cv2.imread(sys.argv[1],cv2.CV_LOAD_IMAGE_COLOR)  
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
			cv2.imwrite('cropped_'+sys.argv[1], cropped)
		
