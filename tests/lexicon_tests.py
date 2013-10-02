from nose.tools import *
from bin import lexicon as lexicon

def test_directions():
	assert_equal(lexicon.scan("north"), [('direction', 'north')])
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
							('direction', 'south'),
							('direction', 'east')])
							

def test_verbs():
	assert_equal(lexicon.scan("go"), [('verb', 'go')])
	result = lexicon.scan("go wave get")
	assert_equal(result, [('verb','go'),
							('verb', 'wave'),
							('verb','get')])
							
							
def test_stops():
	assert_equal(lexicon.scan("the"), [('stop', 'the')])
	result = lexicon.scan("the In Of")
	assert_equal(result, [('stop','the'),
							('stop', 'in'),
							('stop', 'of')])
							
							
def test_nouns():
	assert_equal(lexicon.scan("diary"), [('noun', 'diary')])
	result = lexicon.scan("Wand Broom Owl")
	assert_equal(result, [('noun','wand'),
							('noun','broom'),
							('noun','owl')])
							
							
def test_people():
	assert_equal(lexicon.scan("Nightwing"), [('person','nightwing')])
	result = lexicon.scan("McGonagall Hagrid Dumbledore")
	assert_equal(result, [('person','mcgonagall'),
							('person', 'hagrid'),
							('person', 'dumbledore')])
							
							
def test_numbers():
	assert_equal(lexicon.scan('1234'), [('number',1234)])
	result = lexicon.scan("3 91234")
	assert_equal(result, [('number', 3),
							('number', 91234)])
							
							
def test_errors():
	assert_equal(lexicon.scan("BUTTS"), [('error', 'butts')])
	result = lexicon.scan("Wave Wand farts")
	assert_equal(result, [('verb','wave'),
							('noun','wand'),
							('error','farts')])
							
							

	