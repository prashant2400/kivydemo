import kivy
kivy.require('1.0.9')
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
#om kivy.uix.

class pre(App):
	b1 = None
	time = 20
	
	def build(self):
		self.base = BoxLayout()
		return self.base

	def b_press(self, but):
		self.b1 = but
		#but.text = "Pressed !"
		but.background_normal = "./1.png"
		Clock.schedule_interval(self.cdown,1)
		
		sound = SoundLoader.load('pre.wav')
		if sound:
	
			print("Sound found at %s" % sound.source)
			print("Sound is %.3f seconds" % sound.length)
			sound.play()


			
	def cdown(self, dt):
		self.b1.background_normal = "./" + str(self.time % 10) + ".png"
		self.time -= 1
		if self.time == 0:
			return False


a = pre()
a.run()


		
		
		
