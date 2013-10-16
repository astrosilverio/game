from rooms import phonebook
import json

def dump_rooms_to_json(phonebook):
    rooms_to_dump = {}
    for name, room in phonebook.iteritems():
        rooms_to_dump[name] = { k : v for k,v in room.__dict__.iteritems() if v }

    json.dump(rooms_to_dump, open("rooms.json", 'w'))
   
def add_rooms_to_json(rooms_to_add):
	rooms_file = open('rooms.json')
	existing_rooms = json.load(rooms_file)
	rooms_file.close()
	for name, room in rooms_to_add.iteritems():
		existing_rooms[name] = { k : v for k,v in room.__dict__.iteritems() if v }
	rooms_file = open('rooms.json', 'w')
	json.dump(existing_rooms, rooms_file)
    

# if __name__ == '__main__':
#     dump_rooms_to_json(phonebook)