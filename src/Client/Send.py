import json
import random
import threading
import time

class Send (threading.Thread):
    def __init__(self,sock,confirmed,data,target):
        threading.Thread.__init__(self)
        self.sock = sock
        self.data = data
        self.target = target
        self.confirmed = confirmed
    def run(self):
        ident=random.randint(1, 1000000000)
        for x in range(15):
            success=False
            print "Trying to send message with id: "+str(ident)
            udata=json.loads(self.data)
            udata["id"]=ident
            self.data=json.dumps(udata)
            self.sock.sendto(self.data,self.target)
            print "Sent message with id: "+str(ident)
            time.sleep(2)
            for i in self.confirmed:
                if i==ident:
                    success=True
                    self.confirmed.remove(ident)
            if success:
                print "Sending of: "+str(ident)+" confirmed by remote computer"
                break
        if not success:
            print "Sending of: "+str(ident)+ ' has failed!'
