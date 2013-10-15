from rooms import phonebook
import json

rooms_to_dump = {}
for name, room in phonebook.iteritems():
    rooms_to_dump[name] = room.__dict__
    for direction, destination in room.paths.iteritems():
        rooms_to_dump[name]["paths"][direction] = destination.name

json.dump(rooms_to_dump, open("rooms.json", 'w'))