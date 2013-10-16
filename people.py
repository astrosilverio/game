import json

class Person(object):

	def __init__(self, name=None, description=None, quest_item=None, quest_complete=None, reward=()):
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
		if self.name == 'Draco':
			if player.house != 'Snake' and player.invisible == False:
				print "Draco doesn't reply."
				return
			elif player.invisible == True:
				print "Draco appears not to notice you."
				print "Draco mumbles to himself as he tosses the snitch, '...Giant Squid...embarassingly uncreative...' Something falls out of his pocket. You pick it up."
				player.add_invent('invite')
				return
			else:
				print "Draco nods hello and passes you an invite to the upcoming Slytherin dance."
				player.add_invent('invite')
		if player.invisible == True:
			print "%s appears not to notice you." % self.name

		else:
			if self.quest_item:
				if self.quest_item in player.invent:
					player.remove_invent(self.quest_item)
					print self.quest_complete
					print self.reward[0] + '\n'
					room_object.add_invent(self.reward[1])
					del self.dialogue[0]
				else:
					if self.count < len(self.dialogue):
						print self.dialogue[self.count]
						self.count += 1
					else:
						self.count = 0
						print self.dialogue[self.count]
						self.count += 1
			else:
				if self.count < len(self.dialogue):
					print self.dialogue[self.count]
					self.count += 1
				else:
					self.count = 0
					print self.dialogue[self.count]
					self.count += 1

	
def make_people_from_json():
	npc = {}
	people = json.load(open("people.json"))
	for name, person_data in people.iteritems():
		npc[name] = Person()
		npc[name].__dict__.update(person_data)

	return npc

npc = make_people_from_json()
 
 