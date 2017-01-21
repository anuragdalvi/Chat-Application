import socket
import sys
import os
import cPickle
from threading import Thread


username = sys.argv[2]
sip = sys.argv[4]
sport = int(sys.argv[6])

try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, msg :
        print 'Socket Failed. Error Code:' + str(msg[0]) + 'Message' + msg[1]


sock.sendto(username, (sip, sport))
dict = {}

def recv_msg():
        while True:
                data, addr = sock.recvfrom(65507)
                if addr == (sip, sport):
                        unpickle = cPickle.loads(data)
                        dict.update(unpickle)
                        users = dict.keys()
                        inv_dict = {v: k for k, v in dict.iteritems()}
                        print 'Signed In Users: ' + ', '.join(users)
                else:
                        print '<From ' + addr[0] +':'+ str(addr[1]) + ':' + inv_dict[addr] + '>: ' + data

Thread(target=recv_msg).start()

while True:
        input = raw_input()
        if(input == 'list'):
                sock.sendto('list', (sip, sport))
        else:
                input2 = input.split(" ", 2)
                sock.sendto(input2[2], dict[input2[1]])
