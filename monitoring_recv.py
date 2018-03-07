#!/usr/bin/python2

#  loading socket  module 

import  socket,time,commands

#   module.funtion(ip_version4,socket_type)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  only recevier will do bind part 
s.bind(("192.168.10.200",9090))

ip_list={}
while 4 > 2 :
	d=s.recvfrom(100)
	ip=d[1][0]
        data=d[0]
	fdata=data.split('\n')
	if  ip  in ip_list:
		continue 
	else :
		ip_list[ip]=fdata

	print  ip_list	








'''
def   recv():

	while  5 > 3 :
		d=s.recvfrom(10)
		print  d[1][0]



if  __name__  ==  "__main__" :
	recv()
'''


