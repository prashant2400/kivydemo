from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from random import randint
import random
class gtn(App):
	
	def build(self):
		self.pad = BoxLayout()
		self.number = random.randrange(0,100)
		
		#but = Button(text="Hello")
		#pad.add_widget(but)
		return self.pad

	def btn_p(self, labelid, fo):
		#print "Hello world"
		#self.exit()
		#fo.text = labelid.text 
		#abelid.text = "Aloha"
		#self.pad.ids.t1.text = "A ha 1" + str(self.number)
	
		#self.pad.ids.t1.text = "" + randint(0,100) 

		print randint(0,2)

		pad = self.pad
		pad.ids.l1.text = str(self.number)
		if ( int(pad.ids.t1.text) == self.number ):
			result = "You won !"
		elif ( self.number < int(pad.ids.t1.text)) : 
			result = "Lower !"
		else : 
			result = "Higher !"
		

		pad.ids.l1.text = result 

a=gtn()
a.run()
