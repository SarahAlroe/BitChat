class User():

    def __init__(self, name, ip, port, localip, status):
        self._name = name
        self._ip = ip
        self._port = port
        self._localIp = localip
        self._status = status
    
    def getName (self):
        return self._name
    def setName (self,newName):
        self._name=newName
    def getIp (self):
        return self._ip
    def setIp (self, newIp):
        self._ip=newIp
    def getPort (self):
        return self._port
    def setPort (self, newPort):
        self._port=newPort
    def getLocalIp (self):
        return self._localIp
    def setLocalIp (self, newLocalIp):
        self._localIp=newLocalIp
    def getStatus (self):
        return self._status
    def setStatus (self, newStatus):
        self._status=newStatus
    def getUser(self):
        returnlist=[self._name, self._ip, self._port, self._localIp, self._status]
        return returnlist
    def setUser(self,newName,newIp,newPort,newLocalIp,newStatus):
        self._name=newName
        self._ip=newIp
        self._ip=newPort
        self._localIp=newLocalIp
        self._status=newStatus