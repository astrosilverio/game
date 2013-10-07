from scenes import *


class Thing(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.detail = "You notice nothing of interest."
	
	def examine(self):
		print self.detail
		
#class Supporter(Thing):

#class Edibles(Thing):
	
#	def eat(self):			
#		print ""
#		self.delete


broom = Thing("broom", "A non-descript broom awaits you.")
bludger = Thing("bludger", "A bludger is twitching on the ground.")
wand = Thing("wand", "Your wand is here.")
snitch = Thing("snitch", "A golden snitch hovers in the air!")
mirror = Thing("mirror", "There is a large, dingy, streaky mirror in the corner.")
candy = Thing("candy", "There is some candy in a heap.")
bones = Thing("bones", "A large skeleton lies on the floor.")
food = Thing("food", "There are plates heaped with the finest Scottish cuisine.")

broom.detail = "The broom is an old and battered Nimbus 2000."
bludger.detail = "You can't get too close. The bludger seems intent on sending you to the hospital wing."
wand.detail = "Surprisingly swishy."
snitch.detail = "The snitch is jumping around too quickly for you to get a good look."
mirror.detail = "You become lost in a sort of reverie as you gaze into the mirror. This seems unsafe."
candy.detail = "They appear to be fizzing whizbees."
bones.detail = "The skeleton is of a large, dinosaur-like creature."
food.detail = "It appears to be haggis."

wand.grabbable = True

objectlist = {'broom': broom, 'bludger': bludger, 'wand': wand, 'snitch': snitch, 'candy': candy, 'food': food, 'mirror': mirror, 'bones': bones}

