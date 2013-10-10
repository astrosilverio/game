import scenes

from rooms import *
from things import *
from spells import *
from riddles import *
from thesaurus import *
from random import randint
import pickle
import pdb

inventory = scenes.Inventory()
death = scenes.Death()
you = scenes.Player()


quidditch.add_invent(broom)
quidditch.add_invent(bludger)
start.add_invent(wand)
flying.add_invent(snitch)
disusedroom.add_invent(mirror)
kitchens.add_invent(food)
nwgreathall.add_invent(candy)
chamber.add_invent(bones)

broom.location = quidditch
bludger.location = quidditch
wand.location = start
snitch.location = flying
mirror.location = disusedroom
food.location = kitchens
candy.location = nwgreathall
bones.location = chamber



						
you.location = 'The Quad'
print phonebook[you.location].name	
phonebook[you.location].look()
stair_hall.initialize()
	
while True:
	input = raw_input("> ")
	next = process(input)
	