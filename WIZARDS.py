import rooms
import thesaurus
from things import objectlist
from people import npc

death = rooms.Death()
you = rooms.Player()

you.location = 'The Quad'
rooms.phonebook[you.location].look(you)
rooms.phonebook["Stair Hall"].shuffle_stairs()
	
if __name__ == "__main__":
	while True:
		user_input = raw_input("> ").lower()
		next = thesaurus.process(user_input, you)
		
		dead_people = [person for person in npc if npc[person].alive == False]

		if len(dead_people) > 1 or objectlist['trevor'].alive == False:
			rooms.phonebook[you.location].look(you)
			print "\nYou're terrible."
			exit(1)
	