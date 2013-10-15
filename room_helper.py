from rooms import phonebook
import json

def dump_rooms_to_json(phonebook):
    rooms_to_dump = {}
    for name, room in phonebook.iteritems():
        rooms_to_dump[name] = { k : v for k,v in room.__dict__.iteritems() if v }

    json.dump(rooms_to_dump, open("rooms.json", 'w'))

if __name__ == '__main__':
    dump_rooms_to_json(phonebook)