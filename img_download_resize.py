#!usr/bin/python

import os;
import numpy as np;
import cv2;
import urllib2;
from PIL import Image;

def img_read() :
	url=urllib2.urlopen('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04971313');
	st=url.read();
	x=1;
	y=st.split('\n');
	for i in y:
		
		st='wget --output-document ex/'+str(x)+'.jpg '
		os.system(st+i)
		
    		try:	
			img=Image.open("ex/"+str(x)+".jpg")
			rsz_img=img.resize((500,500))
			rsz_img.save("rsz/"+str(x)+".jpg")
		except:
			x=x+1
			continue
		x=x+1
		if(x>50) :
			break 

img_read()



