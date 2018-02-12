import telnetlib
import urllib2
import socket
from urllib2 import HTTPHandler

def identify_port(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	try:
		result = sock.connect_ex((host,port))
		response = sock.recv(2048)
		if "SSH" in str(response):
			return "ssh"
		elif "FTP" in str(response):
			return "ftp"
		#telnet = telnetlib.Telnet()
		#result = telnet.open(host, port)
		#if result == 0:
		#	return "telnet"
		url = 'http://' + host
		response = requests.get(url)
		print str(response)
		if response != "":
			return "http"
	except:
		url = 'http://' + host + '/'
		req = urllib2.Request(url)
		response = HTTPHandler.http_open(req)
		print str(response)
		if response != "":
			return "http"
		print "something went wrong"
		#if port == 22:
		#	return "ssh"
		#elif port == 80:
		#	return "http"
		#elif port == 23:
		#	return "telnet"
		#elif port == 7:
		#	return "echo"
		#elif port in [21,20]:
		#	return "ftp"
		#elif port in [25, 465, 587]:
		#	return "smtp"
		#return "other"


print identify_port('52.192.197.200', 80)
