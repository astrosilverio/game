from collections import defaultdict
from bin.dictionary import *
from canoncommands import *

canonwords = []
canonwords.extend(direction)
canonwords.extend(noun)
canonwords.extend(person)
canonwords.extend(spell)

noncanonicals = dict()

noncanons = {'north': 'n', 'south': 's', 'west': 'w', 'east': 'e', 'northwest': 'nw',
			'northeast': 'ne', 'southwest': 'sw', 'southeast': 'se', 'up': 'u', 'down': 'd',
	'move': 'go', 'get': 'take', 'put': 'drop', 'examine': 'x', 'ride': 'fly', 'exit': 'quit', 'inventory': 'invent',
			'nimbus': 'broom', 'erised': 'mirror', 'cup': 'tea', 'tree': 'willow', 'whizbees': 'candy', 'skeleton': 'bones'}
			
for key in noncanons:
	noncanonicals[key] = noncanons[key]
			


