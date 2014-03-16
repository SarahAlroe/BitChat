'''
Created on 09/03/2014

@author: tobalr
'''
import Send
import json
import socket
import time
class ClientCommunication():
    '''
    classdocs
        '''
    #connects this client to server
    def connect(self, username, targetUser):
        data = {'type':"connect", 'username': username, 'lanIP': socket.gethostbyname(socket.gethostname()), "targetuser": targetUser}
        jdata = json.dumps(data)
        Send(self.sock, jdata, (self.server, self.serverPort)).start()
        print "Sent:     {}".format(data)
        time.sleep(1)
    
    
    #todo - remove this at some point
    def nsconnect(self):
        print "1"
        data = {'type':"connect", 'username': "Silas", 'lanIP': socket.gethostbyname(socket.gethostname()), "targetuser": "Silas"}
        print "2"
        jdata = json.dumps(data)
        print "3"
        Send(self.sock, jdata, (self.serverAdr, self.serverPort)).start()
        print "Sent:     {}".format(data)
        
    
    
    def confirm(self,cid,target):
        global sock
        confirm={"type": "confirm", "id": cid}
        jconfirm=json.dumps(confirm)
        sock.sendto(jconfirm,target)
        print "Sent confirmation for message with id: "+cid
        
    def initializeConnection(self, serverAdress, serverPort):
        self.serverAdr = serverAdress
        self.serverPort = serverPort
        # set sock
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", 0))
        self.sock.setblocking(0)
        self.sock.settimeout(20) 
        
    def getSock(self):
        return self.sock
        
    
    
    
    def __init__(self):
        pass
            
