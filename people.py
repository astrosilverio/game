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
				print self.quest_complete
				print self.reward[0] + '\n'
				room_object.add_invent(self.reward[1])
				del self.dialogue[0]
		if self.count < len(self.dialogue):
			print self.dialogue[self.count]
			self.count += 1
		else:
			self.count = 0
			print self.dialogue[self.count]
			self.count += 1


def make_people():

	myrtle = Person("Myrtle", "Myrtle is amusing herself by sobbing in between dives into the U-bend.")
	mermaid = Person("A Mermaid", "Behind the glass is a mermaid, whose teeth are displayed in a fearsome grin.")
	neville = Person("Neville", "Neville Longbottom is pacing around.", quest_item='trevor', quest_complete="Neville says, 'Thanks! I don't know how he keeps getting away...'", reward=("In his excitement over reuniting with Trevor, Neville has dropped a small piece of paper.", 'scrap of paper'))
	owl = Person("Owl", "A large owl blinks at you intelligently.", quest_item='food', quest_complete="The owl wolfs down the food you brought him, clicking his beak.", reward=("The owl squawks 'TREVOR!' and scuffs away some droppings to reveal a small-ish toad.", 'trevor'))
	
	myrtle.add_dialogue(["Myrtle says, 'You're just here to throw a book at me!'", "Myrtle says, 'Leave me alone!', and dives back into the toilet."])
	mermaid.add_dialogue(["The mermaid says something unintelligible that sounds like nails on a chalkboard.", "The mermaid says something that is clearly not friendly.", "The merm--hang on, why are you still here? She obviously wants to eat you, leave her alone!"])
	neville.add_dialogue(["Neville says, 'I seem to have misplaced my toad. Can you find him?'", "Neville says, 'The Room of Requirement is stuck in sauna form, so the DA's meeting in the dungeons later.'", "Neville says,'Have we met? I'm Neville.'"])
	owl.add_dialogue(["The owl squawks piteously, taps his stomach with one wing, and clicks his beak as if chewing.", "You feel a bit silly talking to an owl. He chirps in sympathy for your unease."])
		
	npc = {'myrtle': myrtle, 'mermaid': mermaid, 'neville': neville, 'owl': owl}
	return npc

npc = make_people()
 
 