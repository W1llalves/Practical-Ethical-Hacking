#!/bin/python3

import sys
import socket
from datetime import datetime

#define our target
if  len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) #transltate hostname to ipv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 Port_Scanner.py <ip>")

#add a pretty banner
print("_" * 50)
print("Scanning target "+target)
print("time started: "+str(datetime.now()))
print("_" * 50)

try:
        for port in range(50,85):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port)) #returns an error indicator
            #print("checking port {}".format(port))   #printar checagem porta a porta
            if result == 0:
                print("port {} is open".format(port))
            s.close()
except KeyboardInterrupt:
    print("\nExiting program")

except socket.gaierror:
    print("hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("couldn't connect to server.")
    sys.exit()

