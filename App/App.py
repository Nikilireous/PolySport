from kivy.app import App
from kivy.uix.button import Button
from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from datetime import datetime
import os
import ast
import time

Builder.load_file("pos.kv")
class Container(BoxLayout):
    pass

class registration_screen(App):
    def build(self):

        return Container()


if __name__ == "__main__":
    registration_screen().run()
