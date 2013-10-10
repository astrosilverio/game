from collections import defaultdict
from bin.dictionary import *
from canoncommands import *

canonwords = []
[canonwords.append(direction) for direction in directions]
[canonwords.append(noun) for noun in nouns]
[canonwords.append(person) for person in people]
[canonwords.append(spell) for spell in spells]

noncanonicals = dict()

noncanons = {'north': 'n', 'south': 's', 'west': 'w', 'east': 'e', 'northwest': 'nw',
			'northeast': 'ne', 'southwest': 'sw', 'southeast': 'se', 'up': 'u', 'down': 'd',
	'move': 'go', 'get': 'take', 'put': 'drop', 'examine': 'x', 'ride': 'fly', 'exit': 'quit', 'inventory': 'invent',
			'nimbus': 'broom', 'erised': 'mirror', 'cup': 'tea', 'tree': 'willow', 'whizbees': 'candy', 'skeleton': 'bones'}
			
for key in noncanons:
	noncanonicals[key] = noncanons[key]
			
canons = {'go': go, 'fly': fly, 'where': where, 'invent': invent, 'look': look, 'sort': sort, 'help': help, 'quit': quit, 'save': save, 'load': load, 'sssssssssss': speak_parseltongue, 'info': info, 'take': take, 'drop': drop, 'eat': eat, 'cast': cast, 'accio': accio, 'x': x}

