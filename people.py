class Person(object):

	def __init__(self, name, description, quest_item=None, quest_complete=None, reward=()):
		self.name = name
		self.description = description
		self.dialogue = []
		self.quest_item = quest_item
		self.quest_complete = quest_complete
		self.reward = reward
		self.count = 0
		
	def add_dialogue(self, lines):
		self.dialogue.extend(lines)
	
	def talk(self, player, room_object):
		if self.quest_item:
			if self.quest_item in player.invent:
				player.remove_invent(self.quest_item)
				print "%s says %s" % (self.name, self.quest_complete)
				print self.reward[0] + '\n'
				room_object.add_invent(self.reward[1])
				del self.dialogue[0]
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
	neville = Person("Neville", "Neville Longbottom is pacing around.", quest_item='trevor', quest_complete="'Thanks! I don't know how he keeps getting away...'", reward=("In his excitement over reuniting with Trevor, Neville has dropped a small piece of paper.", 'scrap of paper'))
	
	myrtle.add_dialogue(["'You're just here to throw a book at me!'", "'Leave me alone!', and dives back into the toilet."])
	mermaid.add_dialogue(["something unintelligible that sounds like nails on a chalkboard.", "something that is clearly not friendly.", "-- why are you still here? She obviously wants to eat you, leave her alone!"])
	neville.add_dialogue(["'I seem to have misplaced my toad. Can you find him?'", "'The Room of Requirement is stuck in sauna form, so the DA's meeting in the dungeons later.'", "'Have we met? I'm Neville.'"])
		
	npc = {'myrtle': myrtle, 'mermaid': mermaid, 'neville': neville}
	return npc

npc = make_people()
 
 