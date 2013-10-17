import bin.help as help
import spells
import pickle
import things
from rooms import phonebook
from things import objectlist
from quiz import sortingquiz
from people import npc

class Commands(object):

	def go(self, direction, player):
		return player.go(direction)
		
	def fly(self, player):
		return player.fly()
		
	def where(self, player):
		print "You are in " + player.location	
	
	def invent(self, player):
		return player.look()
		
	def look(self, player):
		return phonebook[player.location].look(player)
		
	def talk(self, person, player):
		if person in phonebook[player.location].people:
			return npc[person].talk(player, phonebook[player.location])
		else:
			print "I don't see %s here." % person.capitalize()
	
	def sort(self, player):
		return sortingquiz.try_to_enter(player)

	def help(self, args):
		print help.helpstatement

	def quit(self, args):
		save_or_not = raw_input("Leave without saving? (y/n)"  )
		if save_or_not == 'y':
			exit(0)
		else:
			pass	

	def save(self, player):
		if player.name:
			confirm = raw_input("Save as " + player.name + "? (y/n)  ")
			confirm = confirm.lower()
			if confirm == 'y':
				save_game = open(player.name.lower()+"_save.py", 'w')
			else:
				savename = raw_input("Save under what name? ")
				save_game = open(savename.lower()+"_save.py", 'w')
			save_game.truncate
			pickle.dump(player, save_game)
			save_game.close
		else:
			player.name = raw_input("Save under what name? ")
			save_game = open(player.name.lower()+"_save.py", 'w')
			save_game.truncate
			pickle.dump(player, save_game)
			save_game.close
		
	def load(self, args):		
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
	
	def speak_parseltongue(self, player):
		if player.location == "Myrtle's Bathroom":
			print "The sinks creakily move upward and outward, and the floor tile swings up to reveal a dark chute."
			phonebook["Myrtle's Bathroom"].description = phonebook["Myrtle's Bathroom"].description + "\nThe sink circle has opened to reveal a dark chute."
			phonebook["Myrtle's Bathroom"].add_paths({'d': phonebook["Chute"]})
		if player.location == "Slytherin Common Room":
			print "The eyes on the many carved snake decorations glow green."
		else:
			print "Nothing happens."	
		
	def info(self, player):
		player.info()
			
	def drop(self, thing, player):
		player.drop(thing)
	
	def take(self, thing, player):
		if thing not in objectlist:
			print "You can't take %s!" % thing
			return			
		player.take(thing)
	
	def eat(self, thing, player):
		if thing not in objectlist:
			print "You can't eat %s!" % thing
			return
		player.eat(thing)
		
	def cast(self, incantation, player):
		if "wand" in player.invent:
			spellbook = spells.Spells(player, phonebook[player.location])
			spell = getattr(spellbook, incantation)
			spell()
		else:
			print "You need your wand to cast spells!"

	def accio(self, thing, player):
		if thing not in objectlist:
			print "You can't accio %s!" % thing
			return
	
		def find_distance(room, object):
			dist = 0
			location = None
			linked = set([room])
			accessible_things = set(room.invent)
			while object not in accessible_things and dist <= 4:
				dist += 1
				temp = set()
				for chamber in linked:
					tempstrings = chamber.paths.values()
					tempobjects = [phonebook[string] for string in tempstrings]
					temp.update(tempobjects)
				linked = linked.union(temp)
				for chamber in linked:
					if object in chamber.invent:
						location = chamber
					accessible_things.update(chamber.invent)
			return dist, location
	
		if 'wand' in player.invent:
			if objectlist[thing].grabbable == True:
				if thing in player.invent:
					print "You already have that!"
				else:
					dist, thing_location = find_distance(phonebook[player.location], thing)
					if dist <= 3:
						print "The %s flies toward you alarmingly quickly." % thing
						return thing_location.move(thing, player)
					else:
						print "You try and try, but are not strong enough to summon the %s." % thing
			else:
				print "You're not strong enough to move that."
		else:
			print "You can't cast spells without your wand!"


	def x(self, thing, player):
		if thing in player.invent or thing in phonebook[player.location].invent:
			return objectlist[thing].examine()
		else:
			print "I don't see that here."		

