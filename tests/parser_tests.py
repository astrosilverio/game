from nose.tools import *
from bin import parser as parser

def test_peek():
	words = [('verb', 'go'), ('direction', 'north')]
	assert_equal(parser.peek(words), 'verb')
	

def test_match():
	words = [('verb', 'go'), ('direction', 'north')]
	assert_equal(parser.match(words, 'verb'), ('verb','go'))
	words = [('direction', 'north'), ('verb','go')]
	assert_equal(parser.match(words, 'verb'), None)
	
def test_parse_verb():
	words = [('verb', 'wave'), ('noun', 'wand')]
	assert_equal(parser.parse_verb(words), ('verb','wave'))
	words = [('noun', 'wand'), ('verb', 'wave')]
	assert_raises(parser.ParserError, parser.parse_verb, words)
	
def test_parse_object():
	words = [('noun', 'wand'), ('verb', 'wave')]
	assert_equal(parser.parse_object(words), ('noun', 'wand'))
	words = [('verb', 'wave'), ('noun', 'wand')]
	assert_raises(parser.ParserError, parser.parse_object, words)
	
def test_parse_subject():
	words = [('verb', 'go'), ('direction', 'west')]
	sen = parser.parse_subject(words, ('noun','player'))
	assert_equal(sen.subject, 'player')
	assert_equal(sen.verb, 'go')
	assert_equal(sen.object, 'west')
	
	
def test_parse_sentence():
	words = [('verb','go'),('stop','in'),('stop','the'),('noun','door')]
	sen = parser.parse_sentence(words)
	assert_equal(sen.subject, 'player')
	assert_equal(sen.verb, 'go')
	assert_equal(sen.object, 'door')
