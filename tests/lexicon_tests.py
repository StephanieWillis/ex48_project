from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south west down up left right back east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'west'),
                          ('direction', 'down'),
                          ('direction', 'up'),
                          ('direction', 'left'),
                          ('direction', 'right'),
                          ('direction', 'back'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill stop eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'stop'),
                          ('verb', 'eat')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in from at it of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'from'),
                          ('stop', 'at'),
                          ('stop', 'it'),
                          ('stop', 'of')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 9134 50 98 91234")
    assert_equal(result, [('number', 3),
                          ('number', 9134),
                          ('number', 50),
                          ('number', 98),
                          ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS prince 23 yuk from eat princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('error', 'prince'),
                          ('number', 23),
                          ('error', 'yuk'),
                          ('stop', 'from'),
                          ('verb', 'eat'),
                          ('noun', 'princess')])

def test_input():
    string_in = raw_input('Please enter the sentance "go kill the bear in the north" > ')
    result = lexicon.scan(string_in)
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('stop', 'the'),
                          ('noun', 'bear'),
                          ('stop', 'in'),
                          ('stop', 'the'),
                          ('direction', 'north')] )
