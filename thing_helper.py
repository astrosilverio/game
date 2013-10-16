from things import objectlist
import json

def dump_things_to_json(objectlist):
    things_to_dump = {}
    for name, thing in objectlist.iteritems():
        things_to_dump[name] = { k : v for k,v in thing.__dict__.iteritems() if v }

    json.dump(things_to_dump, open("things.json", 'w'))

def add_things_to_json(things_to_add):
	things_file = open('things.json')
	existing_things = json.load(things_file)
	things_file.close()
	for name, thing in things_to_add.iteritems():
		existing_things[name] = { k : v for k,v in thing.__dict__.iteritems() if v }
	things_file = open('things.json', 'w')
	json.dump(existing_things, things_file)
    
