from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

class ScreenChat(Screen):
    def on_pre_enter(self):
        App.get_running_app().chatBox=self.ids.chatBox.text
    def sendMessage(self,text):
        App.get_running_app().ccommunication.sendmsg(App.get_running_app().username, text)
        self.ids.chatBox.text += "\n"+App.get_running_app().username+": "+text
    pass