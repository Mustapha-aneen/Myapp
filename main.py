from kivy.app import App
from kivy.uix.button import Button

class Taste(App):
	def build(self):
		return Button(text="my app")
Taste().run()
