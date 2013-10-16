from rooms import phonebook
import json

def dump_rooms_to_json(phonebook):
    rooms_to_dump = {}
    for name, room in phonebook.iteritems():
        rooms_to_dump[name] = { k : v for k,v in room.__dict__.iteritems() if v }

    json.dump(rooms_to_dump, open("rooms.json", 'w'))
   
def add_rooms_to_json(rooms_to_add):
	existing_rooms = json.load(open("rooms.json", 'a+'))
	rooms_to_dump = {}
	for name, room in rooms_to_add.iteritems():
		rooms_to_dump[name] = { k : v for k,v in room.__dict__.iteritems() if v }
	json.dump(rooms_to_dump, existing_rooms)
    

# if __name__ == '__main__':
#     dump_rooms_to_json(phonebook)