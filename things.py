from scenes import *


class Thing(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.detail = "You notice nothing of interest."
	
	def examine(self):
		print self.detail


broom = Thing("broom", "A non-descript broom awaits you.")
bludger = Thing("bludger", "A bludger is twitching on the ground.")
wand = Thing("wand", "Your wand is here.")
snitch = Thing("snitch", "A golden snitch hovers in the air!")

broom.detail = "The broom is an old and battered Nimbus 2000."
bludger.detail = "You can't get too close. The bludger seems intent on sending you to the hospital wing."
wand.detail = "Surprisingly swishy."
snitch.detail = "The snitch is jumping around too quickly for you to get a good look."




objectlist = {'broom': broom, 'bludger': bludger, 'wand': wand, 'snitch': snitch}

