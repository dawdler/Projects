#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime


def get_host():
	try:
		host_end = None
		host_beg = sys.argv[2]
		temp, port =sys.argv[1].split('p')
		if (sys.argv[2]).find('-') is not -1:
			host_beg, host_end = (sys.argv[2]).split('-')
	
	except IndexError:
		print "Insufficient Argument"
		sys.exit()
		
	return host_beg, host_end, port


def single_host_scan(host_beg, port):
	'''Takes single IP and scans the host for open and close ports'''
	remoteServerIP  = socket.gethostbyname(host_beg)
	print "The host name is:", socket.gethostname()

	#nice banner with information
	print "-" * 60
	print "Please wait, scanning remote host", remoteServerIP
	print "-" * 60

	# Check what time the scan started
	t1 = datetime.now()

	try:
	    for port1 in range(1,1025): 
	    	if port is not 'A':
	    		port1 = int(port)
	    	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	        result = sock.connect_ex((remoteServerIP, port1))
	        if result == 0:
	            print "Port {}: \t Open".format(port1)
	        else:
	        	 print "Port {}: \t close".format(port1)

	        sock.close()
	        if port is not 'A':
	        	break;

	except KeyboardInterrupt:
	    print "You pressed Ctrl+C"
	    sys.exit()

	except socket.gaierror:
	    print 'Hostname could not be resolved. Exiting'
	    sys.exit()

	except socket.error:
	    print "Couldn't connect to server"
	    sys.exit()

	# Checking the time again
	t2 = datetime.now()

	# Calculates the difference of time, to see how long it took to scan a particular host
	total =  t2 - t1

	# Printing the information to screen
	print 'Scanning Completed in: ', total
	print



def multiple_host_scan(host_beg, host_end, port):

	'''Gets range of IPs and determines open and close ports'''
	beg_first, beg_second, beg_third, beg_fourth = host_beg.split('.')	
	last_first, last_second, last_third, last_fourth = host_end.split('.')
	bforth = int(beg_fourth)
	lforth = int(last_fourth)
	bthird = int(beg_third)
	lthird = int(last_third)
	
	if bthird == lthird:
		for num in range(bforth, lforth+1):
			new_ip = beg_first + "." + beg_second + "." + beg_third + "." + str(num)
			single_host_scan(new_ip, port)
	else:
		count = 0
		ccount = 0
		for num in range(bthird, lthird+1):
			if count == 0:
				beg = bforth
			else:
				beg = 0

			if num == lthird:
				last = lforth
			else:
				last = 255

			for nnum in range(beg, last+1):
				count = 1
				new_ip = beg_first + "." + beg_second + "." + str(num) + "." + str(nnum)
				single_host_scan(new_ip, port)


def main():
	# Clear the screen
	subprocess.call('clear', shell=True)

	host_beg, host_end, port = get_host()
	if host_end == None:
		single_host_scan(host_beg, port)
  	else:
  		multiple_host_scan(host_beg, host_end, port)


if __name__=='__main__':
	main()