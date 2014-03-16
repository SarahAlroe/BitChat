import json
import random
import select
import threading
import time
class Receive (threading.Thread):
    def __init__(self,sock,client):
        #Init threading:
        threading.Thread.__init__(self)
        
        #instance of client for callback
        self.client = client
        
        #Take sock in as a variable
        self.sock = sock
        #Define global variables
        global out
        global msglist
        global confirmed
        global connected
        connected = False
        global lrec
        global loggedin
        global targetwindow
        
    #punch to another client
    def puncher(self,remote_host, port, sock):
     
        my_token = str(random.random())
        remote_token = "_"
    
        remote_knows_our_token = False
     
        for i in range(2):
            print "Connecting: "+str(i)
            r,w,x = select([sock], [sock], [], 0)
     
            if remote_token != "_" and remote_knows_our_token:
                break
     
            if r:
                data, addr = sock.recvfrom(1024)
                if remote_token == "_":
                    remote_token = data.split()[0]
                if len(data.split()) == 3:
                    remote_knows_our_token = True
     
            if w:
                data = "%s %s" % (my_token, remote_token)
                if remote_token != "_": data += " ok"
                sock.sendto(data, (remote_host, port))
            time.sleep(0.5)
     
        return remote_token != "_"        
        
    def run(self):
        print "Starting receiving thread"
        while True:
            try:
                #Get new message:
                rec = self.sock.recvfrom(1024)
                
                #Extract data from rec:
                jout = rec[0]          
                #print "Rec: "+jout
                
                #Extract sender address from rec:
                sender=rec[1]
                
                #Turn Json to Dict:
                out = json.loads(jout)
                print "New rec, type: "+out["type"]+", Id: ",

                #Get id from dict:
                id = out["id"]
                print id
                
                #If the message is not of type 'confirm':
                if out["type"]!="confirm":
                    #Confirm that the message has been received
                    #This is done now, before removal of duped msgs,
                    #to avoid continious sending of the same message,
                    #if the first confirm from a message did not arrive!
                    #confirm(id,sender)
                    #Make sure the message has not already been received: 
                    if lrec.count(id)!=0:
                        continue
                    else:
                        lrec.append(id)
                    
                #Keep the lrec list at 20 items max:
                if len(lrec)>20:
                    del lrec[0]
                print "lrec: "+str(lrec)
                print "Finding action"
                #What does this message contain?
                    #If it's a confirmation that a message has been received
                if out["type"] == "confirm":
                    #Add the confirmed id to the list of confirm
                    confirmed.append(id)
                    print "Confirmed: "+str(confirmed)
                    #If it's userdata, initialise a connection with target:
                if out["type"] == 'userdata':
                    print "Trying to connect..."
                    #Run hole puncher:
                    if self.puncher(out['target'][0],out['target'][1],self.sock):
                        print "Connection sucessful!"
                        connected=True
                        print "0"
                    else:
                        print "Connection failed!"
                    self.client.holePunched(connected, (out['target'][0],out['target'][1]))
                if out["type"] == 'register':
                    print "Registered! var loggedin is now: ",
                    loggedin=True
                    self.client.registeredOnServer();
                    print loggedin
                    print "Gonna show ze targetwindow"
                    
#                     nsconnect()
                    print "Well there we go"
                    
                    
            except:
                pass
        print "Exiting " + self.name
