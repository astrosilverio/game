from scenes import *
from random import randint

class Room(Scene):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		self.invent = {}
		self.people = []
		self.stairrooms = []
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
	def look(self):
		output = self.description + '\n'
		for name, thing in self.invent.items():
			output = output + '\n' + thing.description + '\n'
		print output
				
	def accio(self, thing):
		if 'wand' in inventory.invent.keys():
			return self.move(thing, inventory)
		else:
			print "You need your wand to do that!"
		
class Dark(Room):

	def __init__(self, name, description, out):
		self.name = name
		self.description = description
		self.paths = {}
		self.invent = {}
		self.people = []
		self.out = out

	def look(self):
		print self.description + '\n'
		
		if you.light == True:
			print "You can see by the faint blue light of your wand."
			for name, thing in self.invent.items():
				print thing.description
		else:
			print "You can't see a thing. You might fall in a hole."
			num = randint(0,1)
			if num == 0:
				print "\nYou seem to have been bitten by a bowtruckle. You pass out and wake up in the hospital wing."
				you.location = self.out
				you.location.look()
			else:
				pass		
		
					
class StairHall(Room):

	def __init__(self, name, description, stairrooms):
		self.name = name
		self.description = description
		self.paths = {}
		self.invent = {}
		self.people = []
		self.stairrooms = stairrooms

	def look(self):
		self.initialize()
		print self.description + '\n'
		for name, thing in self.invent.items():
			print thing.description

	def initialize(self):
		number = randint(0,len(self.stairrooms)-1)
		self.add_paths({'up': self.stairrooms[number], 'u': self.stairrooms[number]})


		
class Password(Room):

	def __init__(self, name, description, prompt, password, denial):
		self.name = name
		self.description = description
		self.paths = {}
		self.invent = {}
		self.people = {}
		self.prompt = prompt
		self.password = password
		self.denial = denial


	def try_to_enter(self):
	
		input = raw_input(self.prompt)
		input = input.lower()
		if input == self.password:
			you.location = self
			you.location.look()	
		else:
			print self.denial
			you.location.look()
			

			
class GreatHall(Room):

	def __init__(self, name, description, otherplace):
		self.name = name
		self.description = description
		self.paths = {}
		self.invent = {}
		self.people = {}
		self.count = -1
		self.otherplace = otherplace
		
	def look(self):
		
		self.count = self.count + 1
		
		if you.house == '':
			self.otherplace.try_to_enter()
		else:
			print self.description + '\n'
			for name, thing in self.invent.items():
				print thing.description
				
		

