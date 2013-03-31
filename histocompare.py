import cv, sys

def histogram(image, h_bins = 30, s_bins = 32, scale = 10):
	hsv = cv.CreateImage(cv.GetSize(image),8,3)
	hplane = cv.CreateImage(cv.GetSize(image),8,1)
	splane = cv.CreateImage(cv.GetSize(image), 8, 1)
	vplane = cv.CreateImage(cv.GetSize(image),8,1)
	planes = [hplane, splane]
	cv.CvtColor(image, hsv, cv.CV_BGR2HSV)
	cv.CvtPixToPlane(hsv, hplane, splane, vplane, None)
	hist = cv.CreateHist((h_bins, s_bins), cv.CV_HIST_ARRAY, ranges = ((0,180),(0,255)), uniform = True)
	cv.CalcHist(planes, hist)
	cv.NormalizeHist(hist, 1.0)
	return hist
if __name__ == '__main__':
	if len(sys.argv)!= 3:
		print "Usage: python histo.py <image_file1> <image_file2>"
	else:
		image1 = cv.LoadImage(sys.argv[1], cv.CV_LOAD_IMAGE_COLOR)
		image2 = cv.LoadImage(sys.argv[2], cv.CV_LOAD_IMAGE_COLOR)
		hist1 = histogram(image1)
		hist2 = histogram(image2)
		sc = cv.CompareHist(hist1, hist2, cv.CV_COMP_BHATTACHARYYA)
		if sc > .9 :
			print 1
		else:
			print 0
