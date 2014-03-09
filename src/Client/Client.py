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


class BitChatApp(App):
    HOST, PORT = "78.156.118.38", 5006
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(ChatScreen(name='chat'))
        return self.sm
    
    def on_start(self):
        self.sm.current = "chat"
        pass
      
#         ccommunication = ClientCommunication() 
#         ccommunication.initializeConnection(self.HOST, self.PORT)
#         sock = ccommunication.getSock()
#         receiver = Receive(sock,self)
        
    
    def holePunched(self,status, target):
        print "hole has been punched"
        pass
    def registeredOnServer(self):
        print "has registered on server"
        pass
        
    pass
    
    

if __name__ == '__main__':
    BitChatApp().run()