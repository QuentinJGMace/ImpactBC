import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import NoTransition, ScreenManager, Screen
from kivy.uix.button import Button
from kivy.lang import Builder
# On import screens, et le __init__.py de screens importe toutes les classes
from screens import *

Builder.load_file("kv/BC.kv")

# Le fichier .kv associé au main est BC.kv
# (car le nom de l'application est BCApp et kivy lit le truc tout seul comme ca)
# Donne le layout principal qui sera contenu dans Main_Screen


class Main_kv(GridLayout):
    pass


# Ecran principal, sers pas à grand chose à part à contenir Main_kv
class Main_Screen(Screen):
    pass


# Notre application, c'est un screen manager (on peut faicilement naviguer entre les écran)
class BCApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())

        # L'écran de base est le Welcome_Screen (voir fichier welcome_layout)
        # C'est l'écran pour se connecter
        sm.add_widget(Welcome_Screen(name="welcome"))

        # Écran principal qui reste tout le temps dès qu'on s'est connecté
        sm.add_widget(Main_Screen(name="main_screen"))

        return sm


# Sers juste à dire "lance l'appli"
if __name__ == "__main__":
    BCApp().run()
