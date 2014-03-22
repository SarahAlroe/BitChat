from kivy.uix.screenmanager import ScreenManager, Screen
import kivy
kivy.require('1.8.0') # replace with your current kivy version !
class ScreenLogin(Screen):
    def btn_login_pressed(self, username, password):
        print "login pressed, beginning login operation"
        print "Opening popup"
        #This should be moved to .kv file
        self.whilelogin = Popup(title='Logging in',content=Label(text='Please wait'),auto_dismiss=False,size_hint=(0.5, 0.5))
        self.whilelogin.open()
        App.get_running_app().ccommunication.login(username, password)
        loginsuccess=False
        for x in range(12):
            print "Trying to reach server. Fail in: "+str(12-x)
            if (App.get_running_app().receiver.loggedin):
                loginsuccess=True
                break
            sleep(0.5)
        self.whilelogin.dismiss()
        if (loginsuccess):
            print "Successfully logged in as" +username
            App.get_running_app().sm.current = "friends" #use App.get_running_app() to access current app
        else:
            loginfailbutton = Button(text='Please:\nCheck your connection\nCheck your login details\nTry again')
            self.loginfail = Popup(title='Login failed',content=loginfailbutton,auto_dismiss=False,size_hint=(0.5, 0.5))
            loginfailbutton.bind(on_press=self.loginfail.dismiss)
            self.loginfail.open()
    pass