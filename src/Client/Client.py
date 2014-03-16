from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import kivy
from ClientCommunication import ClientCommunication
from Receive import Receive
kivy.require('1.0.6') # replace with your current kivy version !


class LoginScreen(Screen):
    def btn_login_pressed(self, username, password):
        print "login pressed, beginning login operation"
        print "Opening popup"
        #This should be moved to .kv file
        self.whilelogin = Popup(title='Logging in',content=Label(text='Please wait'),auto_dismiss=False,size_hint=(0.5, 0.5))
        self.whilelogin.open()
        App.get_running_app().ccommunication.login(username, password)
        print username
        print password
        print self.te_username.text #this is another way - it can be used to access widget 
        
        App.get_running_app().sm.current = "friends" #use App.get_running_app() to access current ap
        
    
    pass

class SelectFriendsScreen(Screen):
    def build(self):
        self.list_friends.data = ["Joan","Hugo","Silas"]

class ChatScreen(Screen):
    pass


# Create the screen manager


class BitChatApp(App):
    HOST, PORT = "78.156.118.38", 5006
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(ChatScreen(name='chat'))
        self.sm.add_widget(SelectFriendsScreen(name='friends'))
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