Simple Port Scanner

A simple port scanner with basic features implemented in python. Anyone can scan range of IPs or a single IP for single or multiple ports at one go.

Usage

To scan a particular port of the host/hosts, simply use -p(port number). Suppose, one wants to scan the host for port number 22, then this command can be used:
Ex:
port_scanner -p22 172.31.104.24

To scan all the ports of the host/hosts, simply use -pA.
Ex:
port_scanner -pA 172.31.104.24

One can specify range of IPs by simply giving the range: 172.31.104.24-172.31.104.70
Ex:
port_scanner -pA 172.31.104.24-172.31.104.70
port_scanner -p22 172.31.104.24-172.31.104.70



 
