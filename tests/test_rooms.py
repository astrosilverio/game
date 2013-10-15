from rooms import phonebook

def test_map_is_ok(phonebook):
    for name, room in phonebook.iteritems():
        for destination in room.paths.itervalues():
            if destination not in phonebook:
                print "bad destination: %s" % destination

if __name__ == '__main__':
    test_map_is_ok(phonebook)
