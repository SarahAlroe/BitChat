class Dictionary():
    def setUser(self, username, ip, port, localIp, status):
        self.ip[username] = ip
        self.port[username] = port
        self.localIp[username] = localIp
        self.status[username] = status
    
    def getIp(self, username):
        return self.ip[username]
    
    def getPort(self, username):
        return self.port[username]
    
    def getLocalIp(self,username):
        return self.localIp[username]
    
    def __init__(self):
        self.ip={}
        self.localIp={}
        self.port={}
        self.status={}
        self.currentPartner=""