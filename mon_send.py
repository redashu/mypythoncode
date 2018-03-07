#!/usr/bin/python2

#  loading socket  module 

import  socket,time,commands

#   module.funtion(ip_version4,socket_type)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  only recevier will do bind part 

def   send():

	while  5 > 3 :
		mem=commands.getoutput('cat /proc/meminfo   |  head -3')
		s.sendto(mem,("192.168.10.200",9090))
		time.sleep(5)	



if  __name__  ==  "__main__" :
	send()



