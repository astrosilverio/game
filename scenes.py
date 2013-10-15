from random import randint


quips = ["""You are knocked out. When you come to, you are a silvery misty version of yourself looking down at your own limp body. You are a ghost.""",
			"""Too bad you're not a cat. GAME OVER.""",
			"""You are dead. Sucks to be you.""",
			"""You are sent to Smeltings. Sorry."""]
					

class Scene(object):

	def __init__(self):
		self.invent = {}
		
	def add_invent(self, stuff):
		self.invent.update({stuff.name: stuff})
		
	def remove_invent(self, stuff):
		del self.invent[stuff.name]
			
	def move(self, thing, destination):
		if thing in self.invent.keys():
			if thing not in destination.invent.keys():
				item = self.invent[thing]
				destination.add_invent(item)
				self.remove_invent(item)
				item.location = destination
			else:
				print "You're already carrying it!"
		else:
			print "I don't see that here."

class Player(Scene):

	def __init__(self):
		self.name = ''
		self.house = ''
		self.patronus = ''
		self.flying = False
		self.light = False
		self.invent = {}

	def look(self):
		print "You are carrying:"
		for name, thing in self.invent.items():
			print thing.name
	
	def info(self):
		if self.name:
			print "Your name is %s." % self.name
		if self.house:
			print "You are in %s House!" % self.house
		if self.patronus:
			print "Your patronus is a %s." % self.patronus
			
	def drop(self, thing):
		self.move(thing, phonebook[self.location])
		
	def take(self, thing):
		if objectlist[thing].grabbable == True:
			phonebook[self.location].move(thing, self)
		else:
			print "You can't take that."
			
	def eat(self, thing):
		if objectlist[thing].edible == True:	
			if thing in self.invent:
				print objectlist[thing].taste
				return self.move(thing, phonebook[objectlist[thing].home])
			elif thing in phonebook[self.location].invent:
				print objectlist[thing].taste
				if self.location != objectlist[thing].home:
					return phonebook[self.location].move(thing, phonebook[objectlist[thing].home])
				else:
					pass
			else:
				print "I don't see what you want me to eat."	
		else:
			print "I can't eat that!"
			
	def go(self, direction):
		#	if direction not in directions
		next = phonebook.get(self.location, None).paths.get(direction, None)
		if direction == 'd' and self.flying == True:
			if self.location == 'Flying':
				self.flying = False
				print "You have successfully dismounted.\n"
				self.location = 'Quidditch Pitch'
				return phonebook[self.location].look()
			else:
				self.flying = False
				print "You have successfully dismounted.\n"
				print self.location
				return phonebook[self.location].look()
		if next:
			if hasattr(next, 'try_to_enter'):
				next.try_to_enter()
			else:
				self.location = next.name
				print self.location
				phonebook[self.location].look()
		else:
			print "You can't go that way!"
					
	def fly(self):
		self.flying = True

		if "broom" in self.invent:
			print "You are flying! Everything looks different up here."
		else:
			print "You're not He-Who-Must-Not-Be-Named. Broom is necessary."
		if self.location == "Quidditch Pitch":
			self.location = "Flying"
			return phonebook["Flying"].look()
		else:
			pass
		if "bludger" in phonebook[self.location].invent:
			print "An unsecured bludger clocks you in the head. You come to your senses painfully and your vision clears slowly.\n"
			self.flying = False
			self.location = "Hospital"
			print self.location
			return phonebook[self.location].look()
						
											
class Death(object):
	
	def look(self):
		print quips[randint(0,len(quips)-1)]		
		exit(1)

		
