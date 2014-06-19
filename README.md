# Simple Port Scanner

A simple port scanner with basic features implemented in python. Anyone can scan range of IPs or a single IP for single or multiple ports at one go.

## Dependencies

Port Scanner depends on the following:

	* Python, version 2.7 or above
	* python-dateutil

## Running

To run Port Scanner, execute it directly from the source folder:
	
	$ cd project/
	$ ./port_scanner

## Usage

To scan a particular port of the host/hosts, simply use -p(port number). Suppose, one wants to scan the host for port number 22, then this command can be used:

	$ port_scanner -p22 172.31.104.24

To scan all the ports of the host/hosts, simply use -pA.

	$ port_scanner -pA 172.31.104.24

One can specify range of IPs by simply giving the range: 172.31.104.24-172.31.104.70

	$ port_scanner -pA 172.31.104.24-172.31.104.70
	$ port_scanner -p22 172.31.104.24-172.31.104.70


Feel free to contribute to the project. Thanks for using Port Scanner!
 
