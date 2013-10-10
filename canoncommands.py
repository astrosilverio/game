from bin.dictionary import *
from rooms import *
from bin.help import *
from spells import *
import pickle

def go(direction):
#	if direction not in directions
	next = phonebook.get(you.location, None).paths.get(direction, None)
	if direction == 'd' and you.flying == True:
		if you.location == 'Flying':
			you.flying = False
			print "You have successfully dismounted.\n"
			you.location = 'Quidditch Pitch'
			return phonebook[you.location].look()
		else:
			you.flying = False
			print "You have successfully dismounted.\n"
			print you.location
			return phonebook[you.location].look()
	if next:
		if hasattr(next, 'try_to_enter'):
			next.try_to_enter()
		else:
			you.location = next.name
			print you.location
			return phonebook[you.location].look()
	else:
		print "You can't go that way!"
		
def fly(args):

	you.flying = True

	if "broom" in you.invent.keys():
		print "You are flying! Everything looks different up here."
	else:
		print "You're not He-Who-Must-Not-Be-Named. Broom is necessary."
	if you.location == "Quidditch Pitch":
		you.location = "Flying"
		return flying.look()
	else:
		pass
	if "bludger" in phonebook[you.location].invent.keys():
		print "An unsecured bludger clocks you in the head. You come to your senses painfully and your vision clears slowly.\n"
		you.flying = False
		you.location = "Hospital"
		print you.location
		return phonebook[you.location].look()
		
		
def where(args):
	print "You are in " + you.location
	
	
def invent(args):
	return you.look()
		
def look(args):
	return phonebook[you.location].look()
	
def sort(args):
	return sortingquiz.try_to_enter()

def help(args):
	print helpstatement

def quit(args):
	save = raw_input("Leave without saving? (y/n)"  )
	if save == 'y':
		exit(0)
	else:
		pass	

def save(args):
	if you.name:
		confirm = raw_input("Save as " + you.name + "? (y/n)  ")
		confirm = confirm.lower()
		if confirm == 'y':
			file = open(you.name.lower()+"_save.py", 'w')
		else:
			savename = raw_input("Save under what name? ")
			file = open(savename.lower()+"_save.py", 'w')
		file.truncate
		pickle.dump(you, file)
		file.close
	else:
		you.name = raw_input("Save under what name? ")
		file = open(you.name.lower()+"_save.py", 'w')
		file.truncate
		pickle.dump(you, file)
		file.close
		
def load(args):		
		
	namefile = raw_input("What name did you save under? ")
	file = open(namefile.lower()+"_save.py", 'rb')
	player = pickle.load(file)
	you.name = player.name
	you.location = player.location
	you.house = player.house
	you.patronus = player.patronus
	you.light = player.light
	you.flying = player.flying
	you.invent = player.invent
	
def speak_parseltongue(args):
	if you.location == "Myrtle's Bathroom":
		print "The sinks creakily move upward and outward, and the floor tile swings up to reveal a dark chute."
		myrtle.description = myrtle.description + "\nThe sink circle has opened to reveal a dark chute."
		myrtle.add_paths({'d': chute})
	if you.location == "Slytherin":
		print "The eyes on the many carved snake decorations glow green."
	else:
		print "Nothing happens."	
		
def info(args):
	return you.info()
		
	
def drop(thing):
	return you.move(thing, phonebook[you.location])
	
def take(thing):
	if objectlist[thing].grabbable == True:
		return phonebook[you.location].move(thing, you)
	else:
		print "You can't take that."
		
def eat(thing):
	if objectlist[thing].edible == True:	
		if thing in you.invent.keys():
			print objectlist[thing].taste
			return you.move(thing, phonebook[objectlist[thing].home])
		elif thing in phonebook[you.location].invent.keys():		
			print objectlist[thing].taste
			if you.location != objectlist[thing].home:
				return phonebook[you.location].move(thing, phonebook[objectlist[thing].home])
			else:
				pass
		else:
			print "I don't see what you want me to eat."	
	else:
		print "I can't eat that!"
		
def cast(incantation):
	if "wand" in you.invent.keys():
		spell = spellbook[incantation].cast()
		return spell
	else:
		print "You need your wand to cast spells!"

def find_distance(room, object):
	dist = 0
	linked = set([room])
	accessible_things = set(room.invent.values())
	while object not in accessible_things:
		dist += 1
		temp = set()
		for chamber in linked:
			temp.update(chamber.paths.values())
		linked = linked.union(temp)
		for chamber in linked:
			accessible_things.update(chamber.invent.values())
	return dist
	
def locate_object(thing):
	location = []
	while len(location) < 1:
		for room in phonebook:
			if thing in phonebook[room].invent.values():
				location.append(phonebook[room])
	return location	
	
	
def accio(thing):
	if 'wand' in you.invent.keys():
		if objectlist[thing].grabbable == True:
			if thing in you.invent.values():
				print "You already have that!"
			else:
				dist = find_distance(phonebook[you.location], objectlist[thing])
				if dist <= 3:
					thing_location = locate_object(objectlist[thing])[0]
					print "The %s flies toward you alarmingly quickly." % thing
					return thing_location.move(thing, you)
				else:
					print "You try and try, but are not strong enough to summon the %s." % thing
		else:
			print "You're not strong enough to move that."
	else:
		print "You can't cast spells without your wand!"


def x(thing):
	if thing in you.invent.keys() or thing in phonebook[you.location].invent.keys():
		return objectlist[thing].examine()
	else:
		print "I don't see that here."		

