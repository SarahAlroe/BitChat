import json
import socket
import sys
import threading
import os, time, random
from select import select
from PySide.QtCore import *
from PySide.QtGui import *
import time

#HOST, PORT = "78.156.118.38", 62344
HOST, PORT = "78.156.118.38", 5006

#Init
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("",0))
sock.setblocking(0)
sock.settimeout(20) 
loggedin=False
confirmed=[]
lrec=[]
app = QApplication(sys.argv)
username=""
def login():
    username=loginuserbox.text()
    data={'type':"register", 'username': username, 'lanIP': socket.gethostbyname(socket.gethostname())}
    jdata=json.dumps(data)
    send(sock,jdata,(HOST, PORT)).start()
    print "Sent:     {}".format(data)
    
#class loginwindowwait (threading.Thread):
#    def __init__(self):
#        #Init threading:
#        threading.Thread.__init__(self)
#        global loggedin
#    def run(self):
#        while True:
#            time.sleep(1)
#            if loggedin==True:
#                break
#            print "waitin for ze login"
#        print "login haz happen, changing to target"
        
        
    
def connect():
    data={'type':"connect", 'username': username, 'lanIP': socket.gethostbyname(socket.gethostname()), "targetuser": targetentrybox.text()}
    jdata=json.dumps(data)
    send(sock,jdata,(HOST, PORT)).start()
    print "Sent:     {}".format(data)
    time.sleep(1)

def nsconnect():
    print "1"
    data={'type':"connect", 'username': "Silas", 'lanIP': socket.gethostbyname(socket.gethostname()), "targetuser": "Silas"}
    print "2"
    jdata=json.dumps(data)
    print "3"
    send(sock,jdata,(HOST, PORT)).start()
    print "Sent:     {}".format(data)
    
def loginwindow():
    #Main part of login window:
    
    loginwindow=QWidget()
    loginlayout=QHBoxLayout()
    #Entry line for username:
    loginuserbox=QLineEdit(loginwindow)
    global loginuserbox
    loginuserbox.setPlaceholderText("Username")
    loginuserbox.returnPressed.connect(login)
    #Login button
    loginbutton = QPushButton("Login",loginwindow)
    loginbutton.clicked.connect(login)
    #Display window
    loginlayout.addWidget(loginuserbox)
    loginlayout.addWidget(loginbutton)
    loginwindow.setWindowTitle("Let's Chat - Login")
    loginwindow.setLayout(loginlayout)
    global loginwindow

def targetwindow():
#Main part of target window:
    targetwindow=QWidget()
    targetlayout=QHBoxLayout()
    #Entry line for username:
    targetentrybox=QLineEdit(targetwindow)
    global targetentrybox
    targetentrybox.setPlaceholderText("Target")
    targetentrybox.returnPressed.connect(connect)
    #Connect button
    connectbutton = QPushButton("Connect",loginwindow)
    connectbutton.clicked.connect(connect)
    #Display window
    targetlayout.addWidget(targetentrybox)
    targetlayout.addWidget(connectbutton)
    targetwindow.setWindowTitle("Let's Chat - Connect")
    targetwindow.setLayout(targetlayout)
    global targetwindow

class chat (threading.Thread):
    def __init__(self):
        #Init threading:
        threading.Thread.__init__(self)
    def run(self):
        print "1"
        def chatwindow():
            print "2"
            chatwindow=QWidget()
            #Set up the layout
            chatlayout = QVBoxLayout()
            chatsub_layout = QHBoxLayout()
            #Create and set up the button
            sendbutton = QPushButton("Send",chatwindow)
            #sendbutton.clicked.connect(Sendmsg)
            sendbutton.setDefault(True)
            #Create and set up the message writing box thingy
            outbox = QLineEdit(chatwindow)
            outbox.setPlaceholderText("Text here:")
            outbox.setMinimumWidth(200)
            #outbox.returnPressed.connect(Sendmsg)
            #Create and set up the message reading box 
            inbox = QTextEdit("",chatwindow)
            inbox.setReadOnly(True)
            chatwindow.setWindowTitle("Chat client!")
            chatlayout.addWidget(inbox)
            chatsub_layout.addWidget(outbox)
            chatsub_layout.addWidget(sendbutton)
            chatlayout.addLayout(chatsub_layout)
            # Run the main Qt loop
            chatwindow.setLayout(chatlayout)
            return chatwindow
        print "3"
        chatwindow=chatwindow()
        print "4"
        print "done"
        app.exec_()
        chatwindow.show()



    
def puncher(remote_host, port, sock):
 
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

def confirm(cid,target):
    global sock
    confirm={"type": "confirm", "id": cid}
    jconfirm=json.dumps(confirm)
    sock.sendto(jconfirm,target)
    print "Sent confirmation for message with id: "+cid

class send (threading.Thread):
    def __init__(self,sock,data,target):
        threading.Thread.__init__(self)
        self.sock = sock
        self.data = data
        self.target = target
        global confirmed
    def run(self):
        ident=random.randint(1, 1000000000)
        while True:
            success=False
            print "Trying to send message with id: "+str(ident)
            udata=json.loads(self.data)
            udata["id"]=ident
            self.data=json.dumps(udata)
            self.sock.sendto(self.data,self.target)
            print "Sent message with id: "+str(ident)
            time.sleep(2)
            for i in confirmed:
                if i==ident:
                    success=True
                    confirmed.remove(ident)
            if success:
                print "Sending of: "+str(ident)+" confirmed by remote computer"
                break


class rec (threading.Thread):
    def __init__(self,sock):
        #Init threading:
        threading.Thread.__init__(self)
        #Take sock in as a variable
        self.sock = sock
        #Define global variables
        global out
        global msglist
        global confirmed
        global connected
        global lrec
        global loggedin
        global targetwindow
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
                    if puncher(out['target'][0],out['target'][1],sock):
                        print "Connection sucessful!"
                        connected=True
                        print "0"
                    else:
                        print "Connection failed!"
                    cw=chat().start()
                    cw.chatwindow.show()
                if out["type"] == 'register':
                    print "Registered! var loggedin is now: ",
                    loggedin=True
                    print loggedin
                    loginwindow.hide()
                    print "Gonna show ze targetwindow"
                    nsconnect()
                    print "Well there we go"
                    
                    
            except:
                pass
        print "Exiting " + self.name

#Start the receiver:
rec(sock).start()

#Open the windows:
loginwindow()
targetwindow()
#chatwindow()
loginwindow.show()
sys.exit(app.exec_())


target=raw_input("Please input target: ")

while True:
    pass
