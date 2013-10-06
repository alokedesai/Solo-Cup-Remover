from flask import (
    Flask,
    render_template,
    session,
    redirect,
    request,
    url_for
)
import urllib
import glob, time
from SimpleCV import Image, Color, Font

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")
@app.route("/arrays", methods=["POST"])
def array():
	x = request.form.getlist('values[]')
	images =  x[0].split(",")
	

	results = []
	for file in images:
	    try:
			file = file.split("SPLIT")
			files = file[1]
			identifier = file[0]
			img = Image(files)
			area = img.area()
	        
	        # minimum and maximum areas for a cup relative to the image
	        # proportions estimated and slightly expanded from real samples
			minsize = 0.0015 * area
			maxsize = 0.03 * area
	    
	        # super saturate pixels that most closely approximate red and invert image for blob detection
			im2 = img.hueDistance(color=(212,36,42), minsaturation=200, minvalue=70).invert()
	        # extract blobs within the specified size range
			blobs = im2.findBlobs(minsize=minsize, maxsize=maxsize)
	    
	    
	        # if blob (i.e. cup) detected, draw blue rectangle according to its bounding box.
			if blobs:
	            # for blob in blobs:
	            #     box = blob.mBoundingBox
	            #     img.drawRectangle(box[0],box[1],box[2],box[3], color=Color.BLUE, width=5)

				results.append({"id" : identifier, "src" : files})
				
			# else:
	  #           # determine a reasonable location for text
	  #           # y = img.height / 2
	  #           # x = img.width / 2.5
	  #           # img.drawText('Nothing detected!', x=x, y=y, color=Color.WHITE, fontsize=45)

			# 	results.append({"result" : "not found", "src" : file})
	    
	        
	
	        
	    except Exception as e:
	        print "File : %s, Error : %s" % (files, e)   
	return render_template("results.html" , results = results)   
@app.route('/test')
def test():
	results = []
	for file in files:
	    try:
			img = Image(file)
			area = img.area()
	        
	        # minimum and maximum areas for a cup relative to the image
	        # proportions estimated and slightly expanded from real samples
			minsize = 0.0015 * area
			maxsize = 0.03 * area
	    
	        # super saturate pixels that most closely approximate red and invert image for blob detection
			im2 = img.hueDistance(color=Color.RED, minsaturation=200, minvalue=70).invert()
	        # extract blobs within the specified size range
			blobs = im2.findBlobs(minsize=minsize, maxsize=maxsize)
	    
	    
	        # if blob (i.e. cup) detected, draw blue rectangle according to its bounding box.
			if blobs:
	            # for blob in blobs:
	            #     box = blob.mBoundingBox
	            #     img.drawRectangle(box[0],box[1],box[2],box[3], color=Color.BLUE, width=5)

				results.append({"result" : "found", "src" : file})
				
			# else:
	  #           # determine a reasonable location for text
	  #           # y = img.height / 2
	  #           # x = img.width / 2.5
	  #           # img.drawText('Nothing detected!', x=x, y=y, color=Color.WHITE, fontsize=45)

			# 	results.append({"result" : "not found", "src" : file})
	    
	        
	
	        
	    except Exception as e:
	        print "File : %s, Error : %s" % (file, e)   
	return render_template("results.html" , results = results)    


                            

if __name__ == '__main__':
    app.run(debug=True)

