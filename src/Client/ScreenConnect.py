from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
class ScreenConnect(Screen):
    def btn_connect_pressed(self, user):
        print "Initializing chat with" + user
        App.get_running_app().ccommunication.connect(App.get_running_app().username, user)
        App.get_running_app().sm.get_screen("chat").ids.chatBox.text="You are now chatting with "+user