from canonwords import *

def process(user_input):
	
	if user_input.count('s') >= 11:
		command = 'sssssssssss'
		args = []
		nargs = 0
		
	else:
		words = user_input.split()
		words = [word if (word in canons.keys() or word in canonwords) else noncanonicals.get(word, None) for word in words]
		words = [word for word in words if word is not None]
		
		if words:
			command = words[0]
			args = words[1:]
			nargs = len(words) - 1	
	
			if command in directions:
				args = command
				command = 'go'
		
			if command in spells:
				args = []
				args.append(command)
				command = 'cast'
		
			if args == []:
				args = ['nothing']
	
			if nargs > 1:
				print "I don't do very well with long instructions. Try typing 'help' to learn how to talk to me."
		
			else:	
				if command in canons.keys():
					return canons[command](*args)
			
				else:
					print "What do you want me to do with %s?" % command
					
		else:
			print "I didn't understand any of that."


	
	
	