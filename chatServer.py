import socket
import sys
import os
import cPickle

HOST = ''
PORT = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print'Server Initialized...'
dict = {}
while(True):
        try:
                data = sock.recvfrom(1024)
        except socket.timeout, e:
                raise RuntimeError('Server Down')
        if(data[0] == 'list'):
                list = cPickle.dumps(dict)#Serializes Data i.e. username and Port + IP Address.
                unlist = cPickle.loads(list)
                sock.sendto(list, data[1])
        else:
                dict[data[0]] = data[1]

sock.close()

