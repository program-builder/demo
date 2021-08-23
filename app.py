import kivy
from kivy.app import App
from kivy.uix.label import Label
class Myapp(App):
  def builds(self):
    return Label(text='Hello world')
Myapp().run()  
  
