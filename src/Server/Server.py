import SocketServer
import string
import time
import threading
import json
import random
ret="Not set"
_users={}
class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass
class Handler(SocketServer.BaseRequestHandler):
    def handle(self):
        global _users
        retmsg={}
        self.data = self.request[0].strip()
        #Open new thread
        cur_thread = threading.current_thread()
        socket = self.request[1]
        print "{} wrote: {}".format(self.client_address[0]+":"+str(self.client_address[1]), self.data)
        inn = json.loads(self.data)

        print "Sending confirm: ",
        confirm={"type": "confirm", "id": inn["id"]}
        print "Generated response, ",
        jconfirm=json.dumps(confirm)
        print "Json dumped it, ",
        socket.sendto(jconfirm,self.client_address)
        print "Confirm sent with confirmid "+str(inn["id"])+" !"

        doretmsg=False
        retmsg["id"] = random.randint(1, 1000000000)
        if inn["type"]=="register":
            _users[inn["username"]] = (self.client_address[0], self.client_address[1], inn["lanIP"], time.time(), inn["username"])#[User]= (ip, port, internal ip)
            retmsg["type"] = "register"
            retmsg["username"] = inn["username"]
            retmsg["ip"] = self.client_address[0]
            retmsg["port"] = self.client_address[1]
            retmsg["localip"] = inn["lanIP"]
            print "The users var now looks like this:"
            print _users
            doretmsg = True

        elif inn["type"]=="getusers":
            retmsg["type"]="users"
            retmsg["users"]=_users.keys()
            doretmsg=True

        elif inn["type"]=="connect":
            targetmsg={"type": "userdata", "target": _users[inn["username"]], "id": retmsg["id"]}
            jtargetmsg=json.dumps(targetmsg)
            socket.sendto(jtargetmsg,_users[inn["targetuser"]][0:2])#Send a message to target containing connection info
            print "Sent to "+_users[inn["targetuser"]][0]+":"+str(_users[inn["targetuser"]][1])+": "+str(targetmsg)
            retmsg["type"]="userdata"
            retmsg["target"]=_users[inn["targetuser"]]
            doretmsg=True
        
        elif inn["type"]=="getuserinfo":
            retmsg["type"] = "userinfo"
            retmsg["username"] = inn["username"]
            retmsg["ip"] = _users[inn["username"]][0]
            retmsg["port"] = _users[inn["username"]][1]
            retmsg["localip"] = _users[inn["username"]][2]
            retmsg["status"] = "Online" #Change this to something else in the future...
        
        #If an extra message is needed:
        if doretmsg:
            retmsg["id"]=random.randint(1, 1000000000)
            response=json.dumps(retmsg)
            print "Sent to "+self.client_address[0]+":"+str(self.client_address[1])+": "+response
            socket.sendto(response,self.client_address)

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "192.168.0.24", 5006

    server = ThreadedUDPServer((HOST, PORT), Handler)
    ip, port = server.server_address
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name
print "Server started!"
while True:
    pass
