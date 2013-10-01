from dictionary import *

def find_parseltongue(s):
	if s.count('s') >= 11:
		return ('parsel', 'parseltongue')
	else:
		pass

def find_directions(s):
	if s in directions:	
		return ('direction', directions[s])
	else:
		return None
		
def convert_number(s):
	try:
		return ('number',int(s))
	except ValueError:
		return None
		
def find_spells(s):
	if s in spells:
		return ('spell', s)
	else:
		return None

def find_verbs(s):
	if s in verbs:
		return ('verb', verbs[s])
	else:
		return None

def find_nouns(s):
	if s in nouns:
		return ('noun', s)
	else:
		return None
		
def find_people(s):
	if s in people:
		return ('person', s)
	else:
		return None
		
def find_stops(s):
	if s in stops:
		return ('stop', s)
	else:
		return None

		
def scan(directive):
	directive = directive.lower()
	words = directive.split()
	sentence = []
	for word in words:
		d = find_directions(word)
		v = find_verbs(word)
		n = find_nouns(word)
		p = find_people(word)
		s = find_stops(word)
		sp = find_spells(word)
		num = convert_number(word)
		parsel = find_parseltongue(word)
		if d != None:
			sentence.append(d)
		elif v != None:
			sentence.append(v)
		elif n != None:
			sentence.append(n)
		elif p != None:
			sentence.append(p)
		elif s != None:
			sentence.append(s)
		elif sp != None:
			sentence.append(sp)
		elif num != None:
			sentence.append(num)
		elif parsel != None:
			sentence.append(parsel)
		else:
			sentence.append(('error', word))
	return sentence
		
		
		
		
		
		
		
		
		
		