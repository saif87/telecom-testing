#!/bin/usr/python3 
import socket 

def ServerStart():
    Server = socket.socket() 
    Server.bind(('127.0.0.1', 54321))
    Server.listen(10)

if __name__ == '__main__': 
    ServerStart()

