from kivy.properties import ListProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput

# Ce fichier sers à stocker les widgets personalisés récurrents


# Crée un menu déroulant à partir d'une liste de mots possibles fournis en argument
class Menu_deroulant(TextInput):
    choicesfile = StringProperty("liste_random.txt")
    choiceslist = ListProperty([])

    def __init__(self, **kwargs):
        # each line of file is one possible choice
        self.choicesfile = kwargs.pop('choicesfile', '')
        self.choiceslist = kwargs.pop('choiceslist', [])  # list of choices
        super(Menu_deroulant, self).__init__(**kwargs)
        self.multiline = False
        self.halign = 'left'
        self.bind(choicesfile=self.load_choices)
        self.bind(text=self.on_text)
        self.load_choices()
        self.dropdown = None

    def open_dropdown(self, *args):
        if self.dropdown:
            self.dropdown.open(self)

    def load_choices(self):
        if self.choicesfile:
            with open(self.choicesfile) as fd:
                for line in fd:
                    self.choiceslist.append(line.strip('\n'))
        self.values = []

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        # enter selects current suggestion
        if self.suggestion_text and keycode[0] == ord('\r'):
            self.suggestion_text = ' '  # setting suggestion_text to '' screws everything
            if(self.values):
                self.text = self.values[0]
            if self.dropdown:
                self.dropdown.dismiss()
                self.dropdown = None
        else:
            super(Menu_deroulant, self).keyboard_on_key_down(
                window, keycode, text, modifiers)

    def on_text(self, Menu_deroulant, text):
        if self.dropdown:
            self.dropdown.dismiss()
            self.dropdown = None
        if text == '':
            return
        values = []
        for addr in self.choiceslist:
            # On compare les trucs en lowercase pour être plus permissif
            if addr.lower().startswith(text.lower()):
                values.append(addr)
        self.values = values
        if len(values) > 0:
            if len(self.text) < len(self.values[0]):
                self.suggestion_text = self.values[0][len(self.text):]
            else:
                self.suggestion_text = ' '  # setting suggestion_text to '' screws everything
            self.dropdown = DropDown()
            for val in self.values:
                self.dropdown.add_widget(
                    Button(text=val, size_hint_y=None, height=48, on_release=self.do_choose))
            self.dropdown.open(self)

    def do_choose(self, butt):
        self.text = butt.text
        if self.dropdown:
            self.dropdown.dismiss()
            self.dropdown = None
