class Person(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.dialogue = []
		self.count = 0
		
	def add_dialogue(self, lines):
		self.dialogue.extend(lines)
	
	def talk(self):
		if self.count < len(self.dialogue):
			print "%s says %s" % (self.name, self.dialogue[self.count])
			self.count += 1
		else:
			self.count = 0
			print "%s says %s" % (self.name, self.dialogue[self.count])
			self.count += 1
		
def make_people():

	myrtle = Person("Myrtle", "Myrtle is amusing herself by sobbing in between dives into the U-bend.")
	mermaid = Person("A Mermaid", "Behind the glass is a mermaid, whose teeth are displayed in a fearsome grin.")
	
	myrtle.add_dialogue(["'You're just here to throw a book at me!'", "'Leave me alone!', and dives back into the toilet."])
	mermaid.add_dialogue(["something unintelligible that sounds like nails on a chalkboard.", "something that is clearly not friendly.", "-- why are you still here? She obviously wants to eat you, leave her alone!"])
	
	npc = {'myrtle': myrtle, 'mermaid': mermaid}
	
	return npc
	
npc = make_people()	
