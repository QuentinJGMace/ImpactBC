from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import NoTransition, ScreenManager, Screen

# On charge le fichier qui donne la disposition des layouts
Builder.load_file("kv/Welcome_layout.kv")


# C'est l'écran qui permet de se connecter
class Welcome_Layout(GridLayout):
    pass


# Sert juste à contenir le Welcome_Layout
class Welcome_Screen(Screen):
    pass


class Register_Button(Button):
    def __init__(self, **kwargs):
        super(Register_Button, self).__init__(**kwargs)

    def register(self):
        # zone de texte correpsondant au nom d'utilisateur
        user = self.parent.parent.children[2].children[0].children[0]

        # zone de texte correspondant au MDP
        passw = self.parent.parent.children[1].children[0].children[0]

        if (user.text == "Test" and passw.text == "Test2"):
            # screen_manager qui permet de rentrer dans l'appli à proprement parler
            screen_m = self.parent.parent.parent.manager
            screen_m.current = "main_screen"
            user.text = ""

        else:
            print("Bien essayé")
