from scenes import * 
from random import randint

class Spell(object):

	def __init__(self, name):
		self.name = name
		
class Patronus(Spell):

	def cast(self):
		if 'wand' in inventory.invent.keys():
			patronuses = ["octopus", "cup of tea", "chameleon", "bear", "stag", "badger", "fox", "elephant", "mosquito"]
			temp = randint(0, len(patronuses)-1)
			you.patronus = patronuses[temp]
			if you.patronus:	
				print "A silvery " + you.patronus + " jumps from the end of your wand and scurries around before disappearing!"
			else:
				print "You can't cast that yet!"
		else:
			print "You need your wand to cast spells!"	
			
class Lumos(Spell):

	def cast(self):
		if 'wand' in inventory.invent.keys():
			if you.light == False:
				print "The tip of your wand glows bright blue!"
				you.light = True
			else:
				pass
		else:
			print "You need your wand to cast spells!"
			
class Nox(Spell):

	def cast(self):
		if 'wand' in inventory.invent.keys():
			if you.light == True:
				print "The glowing point of light at the tip of your wand winks out."
				you.light = False
			else:
				pass
		else:
			print "You need your wand to cast spells!"	


			
expectopatronum = Patronus('patronum')
lumos = Lumos('lumos')
nox = Nox('nox')

spellbook = {'patronum': expectopatronum, 'lumos': lumos, 'nox': nox}


