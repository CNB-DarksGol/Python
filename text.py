from kivy.app import App
from kivy.uix.burron import Button

class TestApp(App):
    def build(self):
       return Button(text='Hello')

TesteApp().run()
