from clarifai import rest
from clarifai.rest import ClarifaiApp

# Import os to get list of files in directory
from os import listdir
import os
from os.path import isfile, join

# Folder containing our images
images_dir = '/home/ubuntu/images/nonoffensive'
images_old_dir = '/home/ubuntu/images/nonoffensive_old'

# Create an 'app' object based off our Clarifai API Key
# This gives us access to the API
app = ClarifaiApp("", "")

files = [f for f in listdir(images_dir) if isfile(join(images_dir, f))]

for path in files:
	# Prepend the folder path
	img_path = images_dir +'/' + path
	old_img_path = images_old_dir +'/' + path

	# Print out the file we're uploading
	print ('Uploading ' + path)

	# Upload image with a concept
	try:
		app.inputs.create_image_from_filename(filename=img_path, concepts=['nonoffensive']) 
	except:
		pass
	# Move the file once we're done with uploading it
	print ('Moving ' + path)
	os.rename(img_path, old_img_path)

