import scenes
import things
import rooms # not finished

import thesaurus
from random import randint
import pickle
import pdb

death = scenes.Death()
you = scenes.Player()

objectlist = things.make_things()
phonebook = rooms.make_rooms()


phonebook["Quidditch Pitch"].add_invent(objectlist['broom'])
phonebook["Quidditch Pitch"].add_invent(objectlist['bludger'])
phonebook["The Quad"].add_invent(objectlist['wand'])
phonebook["Flying"].add_invent(objectlist['snitch'])
phonebook["Disused Room"].add_invent(objectlist['mirror'])
phonebook["Kitchen"].add_invent(objectlist['food'])
phonebook["NWGreatHall"].add_invent(objectlist['candy'])
phonebook["Chamber of Secrets"].add_invent(objectlist['bones'])

you.location = 'The Quad'
print phonebook[you.location].name	
phonebook[you.location].look()
phonebook["Stair Hall"].shuffle_stairs()
	
while True:
	input = raw_input("> ")
	next = thesaurus.process(input, you)
	