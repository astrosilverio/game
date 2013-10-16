import rooms
import thesaurus
from random import randint
import pickle
import pdb

death = rooms.Death()
you = rooms.Player()

you.location = 'The Quad'
print rooms.phonebook[you.location].name	
rooms.phonebook[you.location].look(you)
rooms.phonebook["Stair Hall"].shuffle_stairs()
	
if __name__ == "__main__":
	while True:
		user_input = raw_input("> ").lower()
		next = thesaurus.process(user_input, you)
	