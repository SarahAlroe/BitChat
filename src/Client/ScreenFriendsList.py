from kivy.uix.screenmanager import ScreenManager, Screen
class ScreenFriendsList(Screen):
    def on_pre_enter(self): 
        self.ids.list.item_strings = {'Joan', 'Hugo', 'Silas', 'SpaceTrold', 'Troels' ,'Bedstemor', 'Pelle'}
        
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