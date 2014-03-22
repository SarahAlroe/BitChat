from ClientCommunication import ClientCommunication
from Receive import Receive
from ScreenLogin import ScreenLogin
from ScreenFriendsList import ScreenFriendsList
from ScreenChat import ScreenChat
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListView
from time import sleep
import kivy
kivy.require('1.8.0') # replace with your current kivy version !







# Create the screen manager


class BitChatApp(App):
    HOST, PORT = "78.156.118.38", 5006
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(ScreenLogin(name='login'))
        self.sm.add_widget(ScreenChat(name='chat'))
        self.sm.add_widget(ScreenFriendsList(name='friends'))
        return self.sm
    
    def on_start(self):
        self.sm.current = "chat"
        self.ccommunication = ClientCommunication() 
        self.ccommunication.initializeConnection(self, self.HOST, self.PORT)
        sock = self.ccommunication.getSock()
        self.receiver = Receive(sock,self)
        self.receiver.start()
        pass
    
    def getccommunication(self):
        return self.ccommunication
    
    def holePunched(self,status, target):
        print "hole has been punched"
        pass
    
    def registeredOnServer(self):
        print "has registered on server"
        pass
        
    pass
    
    

if __name__ == '__main__':
    BitChatApp().run()