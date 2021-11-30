import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from sftp_manager import SFTPConnector

Builder.load_file("kv/homepage.kv")


class HomeScreen(Screen):
    pass


class HomeLayout(BoxLayout):

    def refresh(self):
        print("Refreshing !")

        conn = SFTPConnector()
        conn.connect()
        conn.upload("README.md")
        conn.close()
    pass
