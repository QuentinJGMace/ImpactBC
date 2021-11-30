import kivy
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from utils.custom_widgets import *

Builder.load_file("kv/com.kv")


class Affiches(AnchorLayout):
    pass


class add_Affiches_Btn(Button):
    def __init__(self, **kwargs):
        super(add_Affiches_Btn, self).__init__(**kwargs)

    def ajouter_ligne(self, _layout):
        _layout.add_widget(Affiches())


class rm_Affiches_Btn(Button):
    def __init__(self, **kwargs):
        super(rm_Affiches_Btn, self).__init__(**kwargs)

    def rm_affiches(self, _layout):
        _layout.remove_widget(_layout.children[0])


class Com(Screen):
    pass
