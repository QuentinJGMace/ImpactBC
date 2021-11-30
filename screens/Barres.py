from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("kv/Barres.kv")


class MenuBar(GridLayout):

    def menu_button(self, screen_id):
        self.parent.ids.screen_manager.current = screen_id

    pass


class QuitBar(BoxLayout):
    pass


class Menu_bar_btn(Button):
    def __init__(self, **kwargs):
        super(Menu_bar_btn, self).__init__(**kwargs)
        self.color = (1, 1, 1, 1)
        self.background_normal = ""
        self.background_color = (100/256, 100/256, 100/256, 1)

    # Change l'écran du milieu et la couleur des boutons en haut
    def change_screen(self, nv_screen):
        # Change l'écran du milieu
        screen_m = self.parent.parent.ids.screen_manager.current = nv_screen

        # Change la couleur du bouton (et réinitialise celle des autres)
        for child in self.parent.children:
            child.background_color = (100/256, 100/256, 100/256, 1)
            child.color = self.color = (1, 1, 1, 1)
        self.color = (12/256, 69/256, 166/256, 1)
        self.background_color = (150/256, 196/256, 239/256, 1)


# Exemple de comment on peut utiliser des fonctions à partir du fichier .kv
# Une fois ça d'écris on a juste a utilisé un custombtn dans le fichier .kv et écrire "on_press = id.dosmth"
# class CustomBtn(Button):
#     def __init__(self, **kwargs):
#         super(CustomBtn, self).__init__(**kwargs)

#     def dosmth(self):
#         self.parent.parent.ids.screen_manager.current = "home"
#         print("Bravo t'as fais une fonction custom")
