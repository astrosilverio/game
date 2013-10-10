import scenes
import things
import rooms # not finished

import thesaurus
from random import randint
import pickle
import pdb

death = scenes.Death()
you = scenes.Player()

object_list = things.make_things()
phonebook = rooms.make_rooms()
rooms.make_paths()

quidditch.add_invent(objectlist['broom'])
quidditch.add_invent(objectlist['bludger'])
start.add_invent(objectlist['wand'])
flying.add_invent(objectlist['snitch'])
disusedroom.add_invent(objectlist['mirror'])
kitchens.add_invent(objectlist['food'])
nwgreathall.add_invent(objectlist['candy'])
chamber.add_invent(objectlist['bones'])

you.location = 'The Quad'
print phonebook[you.location].name	
phonebook[you.location].look()
stair_hall.initialize()
	
while True:
	input = raw_input("> ")
	next = thesaurus.process(input)
	