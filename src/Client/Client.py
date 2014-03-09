from Client import Receive, ClientCommunication
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy
kivy.require('1.0.6') # replace with your current kivy version !


class LoginScreen(Screen):
    pass

class ChatScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(ChatScreen(name='chat'))

class BitChatApp(App):
    HOST, PORT = "78.156.118.38", 5006
    def __init__(self):
        ccommunication = ClientCommunication() 
        ccommunication.initializeConnection(self.HOST, self.PORT)
        sock = ccommunication.getSock()
        receiver = Receive(sock,self)
        
    
    def holePunched(self,status, target):
        print "hole has been punched"
        pass
    def registeredOnServer(self):
        print "has registered on server"
        pass
        
    pass
    
    


if __name__ == '__main__':
    BitChatApp().run()