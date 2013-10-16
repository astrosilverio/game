from people import npc
import json

def dump_people_to_json(npc):
    people_to_dump = {}
    for name, person in npc.iteritems():
        people_to_dump[name] = { k : v for k,v in person.__dict__.iteritems() if v }

    json.dump(people_to_dump, open("people.json", 'w'))

def add_things_to_json(people_to_add):
	people_file = open('people.json')
	existing_people = json.load(people_file)
	people_file.close()
	for name, person in people_to_add.iteritems():
		existing_people[name] = { k : v for k,v in person.__dict__.iteritems() if v }
	people_file = open('people.json', 'w')
	json.dump(existing_people, people_file)
    