from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import kivy
from ClientCommunication import ClientCommunication
from Receive import Receive
from time import sleep
kivy.require('1.0.6') # replace with your current kivy version !


class LoginScreen(Screen):
    def btn_login_pressed(self, username, password):
        print "login pressed, beginning login operation"
        print "Opening popup"
        #This should be moved to .kv file
        self.whilelogin = Popup(title='Logging in',content=Label(text='Please wait'),auto_dismiss=False,size_hint=(0.5, 0.5))
        self.whilelogin.open()
        App.get_running_app().ccommunication.login(username, password)
        timeoutcountdown=12
        while (timeoutcountdown > 0):
            print "Trying to reach server. Fail in: "+str(timeoutcountdown)
            if (App.get_running_app().receiver.loggedin):
                loginsuccess=True
                break
            sleep(0.5)
            timeoutcountdown-=1
        else:
            loginsuccess=False
        if (loginsuccess):
            print "Successfully logged in as" +username
            App.get_running_app().sm.current = "friends" #use App.get_running_app() to access current app
            self.whilelogin.dismiss()
        else:
            self.whilelogin.dismiss()
            loginfailbutton = Button(text='Please:\nCheck your connection\nCheck your login details\nTry again')
            self.loginfail = Popup(title='Login failed',content=loginfailbutton,auto_dismiss=False,size_hint=(0.5, 0.5))
            loginfailbutton.bind(on_press=self.loginfail.dismiss)
            self.loginfail.open()
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