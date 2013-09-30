from scenes import *


class Thing(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description


broom = Thing("broom", "A non-descript broom awaits you.")
bludger = Thing("bludger", "A bludger is twitching on the ground.")
wand = Thing("wand", "Your surprisingly swishy wand is here.")
snitch = Thing("snitch", "A golden snitch hovers in the air!")

objectlist = {'broom': broom, 'bludger': bludger, 'wand': wand, 'snitch': snitch}

