import kivy
from kivy.logger import RESET_SEQ
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
import utils.custom_widgets

from datetime import date

# On charge le fichier .kv correspondant à un écran pour une commande pépin
Builder.load_file("kv/commande_pepin.kv")

# Classe qui désigne l'écran pour ajouter une émission correspondant à une commande pépin


class Commande_pepin(Screen):

    instance = None

    def __init__(self, **kwargs):
        super(Commande_pepin, self).__init__(**kwargs)
        Commande_pepin.instance = self

    def on_leave(self, *args):
        output = super().on_leave(*args)
        Lignes_commande.instance.reset()

        return output

    pass


class CommandeDateTextInput(TextInput):

    def __init__(self, **kwargs):
        super(CommandeDateTextInput, self).__init__(**kwargs)
        self.reset_date()

    def reset_date(self):
        self.text = date.today().strftime('%d/%m/%Y')

    pass


class Lignes_commande(GridLayout):

    instance = None

    def add_ligne(self):
        wid = Ligne_commande(self.lenght() + 1)
        self.add_widget(wid)
        self.lignes.append(wid)

    def del_ligne(self):
        if self.lenght() > 1:
            wid = self.lignes.pop()
            self.remove_widget(wid)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lignes = []
        self.add_ligne()
        Lignes_commande.instance = self  # instance est une variable static

    def lenght(self):
        return len(self.lignes)

    def reset(self):
        while self.lenght() > 1:
            self.del_ligne()

        # On force la destruction de la ligne restante
        wid = self.lignes.pop()
        self.remove_widget(wid)
        wid = Ligne_commande(1)
        self.add_widget(wid)
        self.lignes.append(wid)

    pass

# Classe qui représente une ligne de commande (voir fichier .kv pour les détails)


class Ligne_commande(AnchorLayout):

    def __init__(self, _numero=1, **kwargs):
        self.numero = _numero
        super(Ligne_commande, self).__init__(**kwargs)


# Bouton qui permet d'ajouter des lignes pour une commande pépin
class Btn_nv_ligne(Button):

    # Pas sur que la définition de __init__ serve encore (relique d'ancien code)
    # Mais a priori ça ne fait pas de mal de la mettre
    def __init__(self, **kwargs):
        super(Btn_nv_ligne, self).__init__(**kwargs)

    # Sers à ajouter la ligne et à update le compteur de lignes
    def ajouter_ligne(self):
        Lignes_commande.instance.add_ligne()


# Bouton qui sert à enlever une ligne
class Btn_del_ligne(Button):

    # Pas sur que la définition de __init__ serve encore (relique d'ancien code)
    # Mais a priori ça ne fait pas de mal de la mettre
    def __init__(self, **kwargs):
        super(Btn_del_ligne, self).__init__(**kwargs)

    # Sers à enlever la ligne et à update le compteur de lignes
    def enlever_ligne(self):
        Lignes_commande.instance.del_ligne()
