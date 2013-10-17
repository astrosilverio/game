import json

class Thing(object):

	def __init__(self, name=None, description=None, grabbable=True, edible=False, taste=None, home=None, alive=False, dead_description=None):
		self.name = name
		self.description = description
		self.detail = "You notice nothing of interest."
		self.grabbable = grabbable
		self.edible = edible
		self.taste = taste
		self.home = home
		self.alive = alive
		self.dead_description = dead_description
	
	def examine(self):
		print self.detail

def make_things_from_json():
	objectlist = {}
	things = json.load(open("things.json"))
	for name, thing_data in things.iteritems():
		objectlist[name] = Thing()
		objectlist[name].__dict__.update(thing_data)

	return objectlist

# CHANGE NAME TO (NOT LIST)
objectlist = make_things_from_json()





