import scenes
import things
from rooms import *

from spells import *
from riddles import *
from thesaurus import *
from random import randint
import pickle
import pdb

inventory = scenes.Inventory()
death = scenes.Death()
you = scenes.Player()

object_list = things.make_things()

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
	next = process(input)
	