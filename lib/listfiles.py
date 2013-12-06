import os, shutil

def listfiles(src):

	print "src:",src

	if os.path.isdir(src):
		print src, "is directory"
	else:
		print src, "is NOT directory"

	for root, dirs, files in os.walk(src):

		print "root:",root
		print "dirs:",dirs
		print "files:",files

listfiles("/Users/steves/Dropbox/dev/RaspberryPi/projects/Dropbox/dev/camera")