from scenes import * 
from random import choice

class Spells(object):

	def __init__(self, player):
		self.you = player

	def patronus(self):
		patronuses = ["octopus", "cup of tea", "chameleon", "bear", "stag", "badger", "fox", "elephant", "mosquito"]
		self.you.patronus = choice(patronuses)
		if self.you.patronus:	
			print "A silvery " + self.you.patronus + " jumps from the end of self.your wand and scurries around before disappearing!"
		else:
			print "You can't cast that yet!"

	def lumos(self):
		if self.you.light == False:
			print "The tip of self.your wand glows bright blue!"
			self.you.light = True
		else:
			pass

	def nox(self):
		if self.you.light == True:
			print "The glowing point of light at the tip of self.your wand winks out."
			self.you.light = False
		else:
			pass		
