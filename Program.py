import kivy
from kivy.app import App
from kivy.uix.label import Label

class Myapp(App):
        def build(self):
                return Label(text='SreeRam created this app')

Myapp().run()        
