class ParserError(Exception):
	pass
	
	
class Sentence(object):

	def __init__(self, subject, verb, object):
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]
		
		
def peek(words):
	if words:
		word = words[0]
		return word[0]
	else:
		return None
		
		
def match(words, expecting):
	if words:
		word = words.pop(0)
		
		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None
		
		
		
def skip(words, word_type):
	while peek(words) == word_type:
		match(words, word_type)
		
		
def parse_verb(words):
	skip(words, 'stop')
	
	if peek(words) == 'verb':
		return match(words, 'verb')
	else:
		raise ParserError("Expected a verb next.")
		
		
def parse_object(words):
	skip(words, 'stop')
	next = peek(words)
	
	if next == 'noun':
		return match(words, 'noun')
	if next == 'direction':
		return match(words, 'direction')
	else:
		raise ParserError("Expected a noun or direction here.")
		
		
def parse_subject(words, subj):
	verb = parse_verb(words)
	obj = parse_object(words)
	
	return Sentence(subj, verb, obj)
	
	
def parse_sentence(words):
	skip(words, 'stop')
	
	start = peek(words)
	
	if start == 'noun':
		subj = match(words, 'noun')
		return parse_subject(words, subj)
	elif start == 'verb':
		return parse_subject(words, ('noun','player'))
	else:
		raise ParserError("Don't understand starting with %s" % start)	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		