class Person(object):

	def __init__(self, name):
		self.name = name
		self.dialogue = []
		
	def add_dialogue(self, lines):
		self.dialogue.append(lines)
	
	def talk(self):
		print "%s says %s" (self.name, self.dialogue[randint(0,len(self.dialogue)-1)])
		
