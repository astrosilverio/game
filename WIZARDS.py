import scenes

from rooms import *
import things
from spells import *
from riddles import *
from thesaurus import *
from random import randint
import pickle
import pdb

inventory = scenes.Inventory()
death = scenes.Death()
you = scenes.Player()

object_list = things.create_things()

quidditch.add_invent(broom)
quidditch.add_invent(bludger)
start.add_invent(wand)
flying.add_invent(snitch)
disusedroom.add_invent(mirror)
kitchens.add_invent(food)
nwgreathall.add_invent(candy)
chamber.add_invent(bones)

you.location = 'The Quad'
print phonebook[you.location].name	
phonebook[you.location].look()
stair_hall.initialize()
	
while True:
	input = raw_input("> ")
	next = process(input)
	