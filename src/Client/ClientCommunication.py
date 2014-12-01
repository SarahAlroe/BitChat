'''
Created on 09/03/2014

@author: tobalr
'''
from Send import Send
import json
import socket
import time
class ClientCommunication():
    '''
    classdocs
<<<<<<< HEAD
        '''
    #Login function
    def login(self, username, password):
        data={'type':"register", 'username': username, 'lanIP': socket.gethostbyname(socket.gethostname())}
        jdata=json.dumps(data)
        Send(self.sock, self.client.receiver.confirmed ,jdata, (self.serverAdr, self.serverPort)).start()
        print "Sent:     {}".format(data)
    
    #connects this client to server
    def connect(self, username, targetUser):
        data = {'type':"connect", 'username': username, 'lanIP': socket.gethostbyname(socket.gethostname()), "targetuser": targetUser}
        jdata = json.dumps(data)
        Send(self.sock, self.client.receiver.confirmed, jdata, (self.serverAdr, self.serverPort)).start()
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

    #Sends confirm message to specified target
    def confirm(self,cid,target):
        global sock
        confirm={"type": "confirm", "id": cid}
        jconfirm=json.dumps(confirm)
        sock.sendto(jconfirm,target)
        print "Sent confirmation for message with id: "+cid
        
    def getaddress(self, username):
        print "Getting ip & port of " + username
        if (self.ap.dict.getIp(username)==self.ap.ip):
            ip=self.ap.dict.getLocalIp(username)
        else:
            ip=self.ap.dict.getIp(username)
        port=self.ap.dict.getPort(username)
        addresslist=(ip,port)
        return addresslist

    def getUsers(self):
        print "Getting user list."
        data={'type':"getusers"}
        jdata=json.dumps(data)
        Send(self.sock, self.client.receiver.confirmed ,jdata, (self.serverAdr, self.serverPort)).start()

    def sendmsg(self, username, msg):
        print "Sending message \"" + msg + "\" to user " + username
        data = {'type':"msg", 'username':self.ap.username, 'msg':msg}
        jdata = json.dumps(data)
        Send(self.sock, self.client.receiver.confirmed, jdata, (self.getaddress(username))).start() #Replace vars with new function
        print "The message to "+username+"was queued for sending!"

    def initializeConnection(self, client, serverAdress, serverPort):
        self.client = client
        self.serverAdr = serverAdress
        self.serverPort = serverPort
        # set sock
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", 5007))
        self.sock.setblocking(0)
        self.sock.settimeout(20) 
        
    def getSock(self):
        return self.sock
    
    
    def __init__(self, client):
        self.ap=client;
        pass
            
