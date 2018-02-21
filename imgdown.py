#!/usr/bin/python

import urllib2,os,time
def  imgdown():
	x=raw_input("directory name : ")
	os.mkdir(x)
	url=urllib2.urlopen('http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04557648')
	strimg=url.read()
	y=strimg.split('\n')
	for  i  in  y:
		
		os.system('wget   '+i)
	



imgdown()
