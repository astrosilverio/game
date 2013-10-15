class Person(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.dialogue = []
		
	def add_dialogue(self, lines):
		self.dialogue.append(lines)
	
	def talk(self):
		print "%s says %s" (self.name, self.dialogue[randint(0,len(self.dialogue)-1)])
		
def make_people():

	moaning_myrtle = Person("Myrtle", "Myrtle is amusing herself by sobbing in between dives into the U-bend.")
	mermaid = Person("A Mermaid", "This mermaid's teeth are displayed in a fearsome grin.")
	
	moaning_myrtle.add_dialogue("'Leave me alone!', and dives back into the toilet.", "You're just here to throw a book at me!")
	mermaid.add_dialogue("something unintelligible that sounds like nails on a chalkboard.")
	
npclist = make_people()	
