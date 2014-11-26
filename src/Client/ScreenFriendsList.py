from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
class ScreenFriendsList(Screen):
    def on_pre_enter(self): 
        self.ids.list.adapter.data = {'Joan', 'Hugo', 'Silas', 'SpaceTrold', 'Troels' ,'Bedstemor', 'Pelle'}
      
    def userConverter(self,index, name):
       return {"text": name}

    def chat(self):
        print "Initializing chat with" + str(self.ids.list.adapter.selection[0].text)
        App.get_running_app().ccommunication.connect(App.get_running_app().username, self.ids.list.adapter.selection[0].text)
        App.get_running_app().chatBox="You are now chatting with "+self.ids.list.adapter.selection[0].text

    def update(self):
        pass
    '''     
    def userConverter(self, index, name):
        result = {
        "name": name}
#         "status_message": "funky msg",
#         "online_status": "Cool status"}
        return result
    '''    
        
#         list_view = ListView(item_strings=[str(index) for index in range(100)])

#         self.ids.bx_layout.add_widget(list_view)
#         self.list_view = self.ids.list_view
#         self.list_view.adapter.data = ["Joan","Hugo","Silas"]
#         self.list_view.adapter.bind(on_selected_item=self.callback)
#         
#         names = {'a', 'b', 'c', 'd', 'e' ,'f', 'g'}
#         if names != None :          
#             list_adapter = ListAdapter(data = names, 
#                                        selection_mode = 'single',
#                                        allow_empty_selection = True,
#                                        cls = ListItemButton,
#                                        sorted_keys=[])
# 
#         self.list_view.adapter = list_adapter