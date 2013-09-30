class Sentence(object):

	def __init__(self, subject, verb, object, error):
		self.subject = subject
		self.verb = verb
		self.object = object
		self.error = error
	

def split_parts_of_speech(lexwords):
	parts, specs = [], []
	for word in lexwords:
		part = word[0]
		spec = word[1]
		if part != 'stop':
			parts.append(part)
			specs.append(spec)
		else:
			pass
	return parts, specs	


def process_verb(parts, specs):
	if specs[0] == 'go':
		if parts[1] == 'direction':
			if len(specs) == 2:
				subject = 'player'
				verb = 'go'
				object = specs[1]
				error = ''
			else:
				subject = ''
				verb = ''
				object = ''
				error = "Where do you want me to go?"
		else:
			subject = ''
			verb = ''
			object = ''
			error = "What are you saying?"
	elif specs[0] == 'invent' or specs[0] == 'inventory' or specs[0] == 'look' or specs[0] == 'where':
		subject = ''
		verb = ''
		object = ''
		error = "Those verbs don't take objects, what's up?"
	elif specs[0] == 'talk':
		if parts[1] == 'person':
			subject = 'player'
			verb = 'talk'
			object = specs[1]
			error = ''
		else:
			subject = ''
			verb = ''
			object = ''
			error = "You can't talk to that!"
	elif specs[0] == 'cast':
		if parts[1] == 'spell':
			subject = 'player'
			verb = 'cast'
			object = specs[1]
			error = ''
		else:
			subject = ''
			verb = ''
			object = ''
			error = "I haven't learned that spell..."
	elif specs[0] == 'accio':
		if parts[1] == 'noun':
			subject = 'player'
			verb = 'accio'
			object = specs[1]
			error = ''
		else:
			subject = ''
			verb = ''
			object = ''
			error = "You can't accio that."		
	else:
		if parts[1] == 'noun':
			subject = 'player'
			verb = specs[0]
			object = specs[1]
			error = ''
		else:
			subject = ''
			verb = ''
			object = ''
			error = "You need an object."
	return subject, verb, object, error



def single_word(parts, specs):
	
	if parts[0] == 'direction':
		subject = 'player'
		verb = 'go'
		object = specs[0]
		error = ''
	elif parts[0] == 'verb':
		if specs[0] == 'get' or specs[0] == 'sort' or specs[0] == 'take' or specs[0] == 'drop' or specs[0] == 'put' or specs[0] == 'look' or specs[0] == 'invent' or specs[0] == 'inventory' or specs[0] == 'eat' or specs[0] == 'where':
			subject = 'player'
			verb = specs[0]
			object = ''
			error = ''
		elif specs[0] == 'fly':
			subject = 'player'
			verb = 'fly'
			object = 'broom'
			error=''
		else:
			subject = ''
			verb = ''
			object = ''
			error = 'What are you trying to do?!?'
	elif parts[0] == 'noun':
		subject = ''
		verb = ''
		object = ''
		error = "I don't know what you want me to do with that."
	elif parts[0] == 'spell':
		subject = 'player'
		verb = 'cast'
		object = specs[0]
		error = ''
	elif parts[0] == 'parsel':
		subject = ''
		verb = 'parseltongue'
		object = ''
		error = ''
	else:
		subject = ''
		verb = ''
		object = ''
		error = "I'm sorry, I don't understand."
		
	return subject, verb, object, error



def double_words(parts, specs):
	if parts[0] == 'noun':
		subject = ''
		verb = ''
		object = ''
		error = "I don't know what you want me to do with that."
	elif parts[0] == 'direction':
		subject = ''
		verb = ''
		object = ''
		error = "That's not a sentence."
	elif parts[0] == 'verb':
		subject, verb, object, error = process_verb(parts, specs)
	elif parts[0] == 'parsel':
		subject = ''
		verb = 'parseltongue'
		object = ''
		error = ''
	else:
		subject = ''
		verb = ''
		object = ''
		error = "I'm sorry, I don't understand."
	return subject, verb, object, error
	
	
	
	
def parse_sentence(lexwords):

	parts, specs = split_parts_of_speech(lexwords)
	
	if len(parts) == 0:
		subject = ''
		verb = ''
		object = ''
		error = "I need some input..."
		sentence = Sentence(subject, verb, object, error)
		return sentence
	elif len(parts) == 1:
		subject, verb, object, error = single_word(parts, specs)
		sentence = Sentence(subject, verb, object, error)
		return sentence
	elif len(parts) == 2:
		subject, verb, object, error = double_words(parts, specs)
		sentence = Sentence(subject, verb, object, error)
		return sentence
	else:
		subject = ''
		verb = ''
		object = ''
		error = "I can't process that much, sorry!"
		sentence = Sentence(subject, verb, object, error)
		return sentence
	

	