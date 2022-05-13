#!/usr/bin/python

import socket
import time
import sys
import datetime


if len(sys.argv) > 2:
    result = True
else:
    result = False

if result == False:
    print("Usage:  python " + __file__ + " <host> <port>")
    exit(0)

ip = sys.argv[1]
port = sys.argv[2]
retry = 1
delay = 1
timeout = 5

def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()

def checkHost(ip, port):

        ipup = False
        for i in range(retry):
                if isOpen(ip, port):
                        ipup = True
                        break
                else:
                        time.sleep(delay)
        return ipup


a = datetime.datetime.now()
if checkHost(ip, port):
        b = datetime.datetime.now()
        delta = b - a
        ms = int(delta.total_seconds() * 1000)
        print (str(b) +"; INFO; " + ip + ":" + port + " is up; " + str(ms) + " ms")
else:
        b = datetime.datetime.now()
        delta = b - a
        ms = int(delta.total_seconds() * 1000)
        addr1 = socket.gethostbyname(ip)
        print (str(b) +"; ERROR; " + ip + ":" + port + " is not up ("+ addr1 +"); " + str(ms) +" ms" )
