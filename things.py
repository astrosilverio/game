from scenes import *


class Thing(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.detail = "You notice nothing of interest."
		self.grabbable = True
		self.edible = False
	
	def examine(self):
		print self.detail
		
class Supporter(Thing):
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.detail = "You notice nothing of interest."
		self.grabbable = False
		self.edible = False
	
class Edibles(Thing):
	def __init__(self, name, description, taste, home):
		self.name = name
		self.description = description
		self.detail = "You notice nothing of interest."
		self.grabbable = True
		self.edible = True
		self.taste = taste
		self.home = home
	



broom = Thing("broom", "A non-descript broom awaits you.")
bludger = Thing("bludger", "A bludger is twitching on the ground.")
wand = Thing("wand", "Your wand is here.")
snitch = Thing("snitch", "A golden snitch hovers in the air!")
mirror = Supporter("mirror", "There is a large, dingy, streaky mirror in the corner.")
candy = Edibles("candy", "There is some candy in a heap.", "You eat the candy, but you've never been fond of fizzing whizbees. Perhaps someone else in the castle is...", 'NWGreatHall')
bones = Supporter("bones", "A large skeleton lies on the floor.")
food = Edibles("food", "There are plates heaped with the finest Scottish cuisine.", "::BURP::", 'Kitchen')

broom.detail = "The broom is an old and battered Nimbus 2000."
bludger.detail = "You can't get too close. The bludger seems intent on sending you to the hospital wing."
wand.detail = "Surprisingly swishy."
snitch.detail = "The snitch is jumping around too quickly for you to get a good look."
mirror.detail = "You become lost in a sort of reverie as you gaze into the mirror. This seems unsafe."
candy.detail = "They appear to be fizzing whizbees."
bones.detail = "The skeleton is of a large, dinosaur-like creature."
food.detail = "It appears to be haggis."


objectlist = {'broom': broom, 'bludger': bludger, 'wand': wand, 'snitch': snitch, 'candy': candy, 'food': food, 'mirror': mirror, 'bones': bones}

