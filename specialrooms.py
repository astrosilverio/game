from scenes import *
from rooms import *
from things import *

stairrooms = [westsecondewcorr, westlibrary, southsecondnscorr]
						
class StairHall(Room):

	def look(self):
		self.initialize()
		print self.description + '\n'
		for name, thing in self.invent.items():
			print thing.description

	def initialize(self):
		number = randint(0,2)
		self.add_paths({'up': stairrooms[number], 'u': stairrooms[number]})



			
class Password(Room):

	def __init__(self, name, description, password):
		self.name = name
		self.description = description
		self.paths = {}
		self.invent = {}
		self.people = {}
		self.password = password

	def try_to_enter(self):
	
		input = raw_input("Password? ")
		input = input.lower()
		if input == self.password:
			you.location = self
			you.location.look()	
		else:
			print "Wrong password."
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
		
		if self.count == 0 and you.house == '':
			you.location = self.otherplace
			you.location.look()
		else:
			self.look()


