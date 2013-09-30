from bin import parse
from bin import lexicon
from scenes import *
from random import randint
from quiz import *
from rooms import *
from things import *
from spells import *
from riddles import *


start = Room("The Quad","You are standing outside a wizarding school in Scotland. The entrance to the castle is to the north. Paths lead east, west, and south.")
quidditch = Room("Quidditch Pitch", "You are on the Quidditch pitch. Why don't you explore?")
flying = Room("Flying", "You are soaring above the Quiddich pitch!")
westlibrary = Room("West Library", "You are in the restricted wing of the library. A chill, slightly ominous draft stirs dust motes in the air. There's a doorway to the north. The main section of the library is to the east.")
eastlibrary = Room("East Library", "You are in the library. Stacks of books lie scattered on tables and comfy chairs that are perenially dappled with late afternoon sunshine. The restricted section is to the west and there is a broad archway to the north through which you can glimpse stairs leading down and stripes of green, red, blue, and yellow.")
westsecondewcorr = Room("WestSecondEWCorr", "You are at the western end of a long east-west corridor in the North Tower. A stairway leads down and the rest of the corridor extends east.")
centralsecondewcorr = Room("CentralSecondEWCorr", "You are in the middle of a long east-west corridor in the North Tower. There is another corridor to the south, and stairways leads up and down from here.")
eastsecondewcorr = Room("EastSecondEWCorr", "You are at the eastern end of a long east-west corridor in the North Tower. There is a disused classroom to the north, and a stairway to the east.")
southsecondnscorr = Room("SouthSecondNSCorr", "You are at the southern end of a north-south corridor in Lion Tower. There is a doorway to the west and a stairway going down.")
northsecondnscorr = Room("NorthSecondNSCorr", "You are at the northern end of a north-south corridor in Lion Tower. There is a portrait of Dawn French on the eastern wall. A passage leads north and a narrow stairway is to the west.")
gryffindor = Password("Gryffindor", "You are in the Lion House Common Room! The circular room is filled with large comfy armchairs. Scarlet and gold hangings line the walls. A fire crackles in the fireplace. There is a hole in the wall to the west.", "Dawn French coughs lightly and says, 'Password?'  ","pig snout", "\n'Sorry dear, that was last week. Or the week before. Run along now.'\n")
myrtle = Room("Myrtle's Bathroom", "You are in a disused girls' lavatory on the second floor. Someone is crying messily in one of the stalls. The sinks are arrayed in a curious circle, and the circular floor tile in the center of the sink-circle looks like it moves.")
chute = Room("Chute", "You slide down the dark chute and land in front of a door covered with elaborate snake carvings. When you repeat the hissing noise you made upstairs, the snakes writhe and the door swings open.\nThe Chamber of Secrets has been opened!")
chamber = Room("Chamber of Secrets", "You are in the Chamber of Secrets. A large skeleton lies on the floor.")
nwgreathall = Room("NWGreatHall", "You are in the NW corner of the Great Hall. There is door to the west, behind the teacher's table. There is also a path to the north.")
sortingquiz = SortingQuiz(quiz)
negreathall = GreatHall("NEGreatHall", "You are in the NE corner of the Great Hall. A doorway lies behind a tapestry to the north, and a stairway leads down.", sortingquiz)
swgreathall = Room("SWGreatHall", "You are in the SW corner of the Great Hall. There is a broad archway in the west wall.")
segreathall = Room("SEGreatHall", "You are in the SE corner of the Great Hall. There is a stairway to the south and a door to the east.")
disusedroom = Room("Disused", "You are in a disused classroom.")
divination = Room("Divination", "You are in the Divining classroom.")
trophy = Room("Trophy", "You are in the trophy room.")
nbasecorr = Room("North Basement Corridor", "You are at the northern end of a basement corridor. The hall is filled with the smell of baking bread. The kitchens are through a low archway to the east and there is a circular door in the wall to the north.")
sbasecorr = Room("South Basement Corridor", "You are at the southern end of a basement corridor. It is decidedly less pleasant here than the northern end. The walls are covered with foul slime. A heavy door is in the south wall. Emerald green gems light the stairway leading down.")
hufflepuff = Room("Hufflepuff", "You are in the Hufflepuff Common Room. It is full of overstuffed armchairs. There is a large tapestry on the east wall and a fireplace on the west wall.")
kitchens = Room("Kitchen", "You are in the castle kitchen. Pots are boiling, fires are crackling, and sinks bubbling. The main door is to the west.")
emeraldhall = Room("Emerald Hall", "You are in a hall encrusted with emeralds. An ebony door is set into the southern, gem-like wall. A grimy passageway leads east. A green-lit stairway goes up.")
slytherin = Password("Slytherin", "You are in the Slyterin Common Room. There are windows that appear to look out into the lake.", "A silky voice murmurs, 'Password?' ", "giant squid", "\nThe door grates on its hinges as it shouts, 'BEGONE'!\n")
dungeons = Room("Dungeons", "You are in the dungeons. They have obviously not been used or cleaned in a very long time. Slime appears to be oozing from the walls. You are seized by a strong urge to leave to the west.")
filch = Room("Filch's Office", "You are in a small, spotless room. A filing cabinet stands in the corner and a discontented cat hisses at you from the floor.")
potions = Room("Potions classroom", "You are in the Potions classroom. Herbs hang from the ceiling. There is a general air of misery.")
hospital = Room("Hospital", "You are in the hospital wing. The exit is to the south.")
gates = Room("Castle Gates", "You are inside the Hogwarts main gates. The castle is to the west. You can just make out Hogsmeade down a long path through the gates. The gates are locked.")
hogspath = Room("Path to Hogsmeade", "To your east is a set of imposing gates. They appear to be locked. You can just make out Hogsmeade at the end of the long path to your west. There is a hole in the ground near your feet.")
hogstunnelone = Dark("Dark tunnel", "You are in a long dark tunnel. There is a dim light from above.", hospital)
hogstunneltwo = Dark("Dark tunnel", "You are in a long dark tunnel.", hospital)
hogstunnelthree = Dark("Dark tunnel", "You are in a long dark tunnel. There is a dim light from above.", hospital)
witch = Password("Entrance to One-Eyed Witch's Passage", "The statue creakily walks a pace towards you to expose a hole in the floor. It seems to be a very dark tunnel.", "You approach the singularly ugly statue, apparently of Gunhilda of Gorsemoor.\nYou have the impression that the statue is waiting for you to say something.\n", "dissendium", "\nThe statue's single eye fixes on you displeasedly.")
westthirdewcorr = Room("WestThirdEWCorr", "You are at the western end of a third-floor corridor. In a nook in the far western corner is a statue of a one-eyed, humpbacked witch.")
eastthirdewcorr = Room("EastThirdEWCorr", "You are at the eastern end of a third-floor corridor. There is a closed door in the north wall and a staircase going down.")
astrohall = Room("Astronomy Tower Hall", "You are on a low level of the Astronomy Tower. A spiral staircase winds up and down, and there are passageways to the north and south.")
dumblehall = Room("Headmaster's Tower", "You are in a small octagonal room in the Headmaster's Tower. A passageway leads south. A staircase that is more of a ladder disappears through a trapdoor in the ceiling. A door-sized gargoyle is on the east wall.")
dumblegarg = Password("Gargoyle", "The gargoyle swings out to reveal a stone spiral staircase.", "You can't be sure, but the gargoyle seems to blink at you as you approach it.\n", "fizzing whizbee", "The gargoyle continues to survey you impassively.")
dumblestair = Room("Headmaster's Stairs", "You are on a tightly wound stone spiral staircase that noiselessy moves under your feet and you switch floors efforlessly. If you lift your foot up, it moves you up and vice versa.")
dumbledore = Room("Headmaster's Office", "You are in the Headmaster's Office.")
owlery = Room("Owlery", "You have climbed to the Owlery. The floor is cluttered with feathers and small bones.")
requirehall = Room("Third Floor Corridor", "You are in a non-descript third-floor corridor. There is a passage to the west and a door in the south wall.")
ravenhall = Room("Astronomy Tower Landing", "You are on a landing in the Astronomy Tower. In the west wall is a blue door with a bronze knocker set into it. A spiral staircase winds up and down.")
astronomy = Room("Top of Astronomy Tower", "You are out on the roof of the Astronomy Tower. The view is spectacular.")
ravenclaw = Password("Ravenclaw Common Room", "You are in the Ravenclaw Common Room.", "The eagle-shaped knocker intones, "+riddles[randint(0, len(riddles)-1)][0], riddles[randint(0, len(riddles)-1)][1], "\nThe knocker replies, 'Incorrect!'")




stairrooms = [westsecondewcorr, westlibrary, southsecondnscorr]
stair_hall = StairHall("StairHall", "You are in a room with many stairways that appear to be continuously moving. There is a large door in the south wall and a broad archway to the east.", stairrooms)
start.add_paths({'n': stair_hall, 's': quidditch, 'e': gates})
gates.add_paths({'w': start})
hogspath.add_paths({'d': hogstunnelthree})
hogstunnelthree.add_paths({'u': hogspath, 'e': hogstunneltwo})
hogstunneltwo.add_paths({'w': hogstunnelthree, 'e': hogstunnelone})
hogstunnelone.add_paths({'w': hogstunneltwo, 'u': witch})
stair_hall.add_paths({'s': start, 'e': swgreathall, 'n': filch})
quidditch.add_paths({'n': start})	
flying.add_paths({'down': quidditch, 'd': quidditch})
westlibrary.add_paths({'e': eastlibrary, 'n': stair_hall})
eastlibrary.add_paths({'w': westlibrary, 'n': segreathall})
westsecondewcorr.add_paths({'d': stair_hall, 'e': centralsecondewcorr})
centralsecondewcorr.add_paths({'w': westsecondewcorr, 'e': eastsecondewcorr, 's': northsecondnscorr, 'd': negreathall, 'u': astrohall})
eastsecondewcorr.add_paths({'w': centralsecondewcorr, 'n': disusedroom, 'e': divination,'u': divination})
southsecondnscorr.add_paths({'d': stair_hall, 'n': northsecondnscorr, 'w': myrtle})
northsecondnscorr.add_paths({'s': southsecondnscorr,'n': centralsecondewcorr, 'e': gryffindor, 'u': eastthirdewcorr})
gryffindor.add_paths({'w': northsecondnscorr})
swgreathall.add_paths({'w': stair_hall,'e': segreathall, 'n': nwgreathall})
segreathall.add_paths({'w': swgreathall, 'n': negreathall, 'u': eastlibrary, 's': eastlibrary, 'e': trophy})
negreathall.add_paths({'s': segreathall,'w': nwgreathall, 'n': centralsecondewcorr, 'd': nbasecorr})
nwgreathall.add_paths({'s': swgreathall,'e': negreathall, 'n': hospital})
disusedroom.add_paths({'s': eastsecondewcorr})
divination.add_paths({'d': eastsecondewcorr})
filch.add_paths({'s': stair_hall})
trophy.add_paths({'w': segreathall})
nbasecorr.add_paths({'u': negreathall, 'n': hufflepuff, 'e': kitchens, 's': sbasecorr})
hufflepuff.add_paths({'s': nbasecorr, 'e': kitchens})
kitchens.add_paths({'n': hufflepuff, 'w': nbasecorr})
sbasecorr.add_paths({'n': nbasecorr, 's': potions, 'd': emeraldhall})
potions.add_paths({'n': sbasecorr})
emeraldhall.add_paths({'u': sbasecorr, 'e': dungeons, 's': slytherin})
slytherin.add_paths({'n': emeraldhall})
dungeons.add_paths({'w': emeraldhall})
myrtle.add_paths({'e': southsecondnscorr})
chute.add_paths({'w': chamber, 'u': myrtle})
chamber.add_paths({'e': chute})
hospital.add_paths({'s': nwgreathall})
witch.add_paths({'e': westthirdewcorr, 'd': hogstunnelone})
westthirdewcorr.add_paths({'w': witch, 'e': eastthirdewcorr})
eastthirdewcorr.add_paths({'d': northsecondnscorr, 'w': westthirdewcorr})
astrohall.add_paths({'d': centralsecondewcorr, 'n': dumblehall, 's': requirehall, 'u': ravenhall})
dumblehall.add_paths({'s': astrohall, 'e': dumblegarg, 'u': owlery})
dumblegarg.add_paths({'w': dumblehall, 'u': dumblestair})
dumblestair.add_paths({'u': dumbledore, 'd': dumblehall})
dumbledore.add_paths({'d': dumblestair})
owlery.add_paths({'d': dumblehall})
requirehall.add_paths({'w': astrohall})
ravenhall.add_paths({'d': astrohall, 'u': astronomy, 'w': ravenclaw})
astronomy.add_paths({'d': ravenhall})
ravenclaw.add_paths({'e': ravenhall})


quidditch.add_invent(broom)
quidditch.add_invent(bludger)
start.add_invent(wand)
flying.add_invent(snitch)



you.location = start

def go(direction):
	next = you.location.paths.get(direction, None)
	if direction == 'd' and you.flying == True:
		if you.location.name == 'Flying':
			you.flying = False
			print "You have successfully dismounted."
			you.location = quidditch
			return you.location.look()
		else:
			you.flying = False
			print "You have successfully dismounted."
			print you.location.name
			return you.location.look()
	if next:
		if hasattr(next, 'try_to_enter'):
			next.try_to_enter()
		else:
			you.location = next
			print you.location.name
			return you.location.look()
	else:
		print "You can't go that way!"
		
def fly():

	you.flying = True

	if "broom" in inventory.invent.keys():
		print "You are flying! Everything looks different up here."
	else:
		print "You're not He-Who-Must-Not-Be-Named. Broom is necessary."
	if you.location.name == "Quidditch Pitch":
		you.location = flying
		return flying.look()
	else:
		pass
	if "bludger" in you.location.invent.keys():
		print "An unsecured bludger clocks you in the head. You come to your senses painfully and your vision clears slowly.\n"
		you.flying = False
		you.location = hospital
		print you.location.name
		return you.location.look()
		
		
def where():
	print "You are in " + you.location.name
		
		
def process(input):
	words = lexicon.scan(input)
	sentence = parse.parse_sentence(words)
	if sentence:
		subject = sentence.subject
		verb = sentence.verb
		object = sentence.object
		error = sentence.error
		if error:
			print error
		elif 'invent' in verb:
			return inventory.look()
		elif 'inventory' in verb:
			return inventory.look()
		elif 'look' in verb:
			return you.location.look()
		elif 'go' in verb:
			return go(object)
		elif 'put' in verb:
			return inventory.move(object, you.location)
		elif 'drop' in verb:
			return inventory.move(object, you.location)
		elif 'take' in verb:
			return you.location.move(object, inventory)
		elif 'get' in verb:
			return you.location.move(object, inventory)
		elif 'fly' in verb:
			return fly()
		elif 'cast' in verb:
			spell = spellbook[object].cast()
			return spell
		elif 'accio' in verb:
			return you.location.accio(object)
		elif 'sort' in verb:
			return sortingquiz.try_to_enter()
		elif 'where' in verb:
			return where()
		elif 'parseltongue' in verb:
			if you.location.name == "Myrtle's Bathroom":
				print "The sinks creakily move upward and outward, and the floor tile swings up to reveal a dark chute."
				myrtle.description = myrtle.description + "\nThe sink circle has opened to reveal a dark chute."
				myrtle.add_paths({'d': chute})
			else:
				print "Nothing happens."
		else:
			return None
						
	else:
		return None
					
start.look()
stair_hall.initialize()

	
while True:
	input = raw_input("> ")
	next = process(input)

	
								
	
	