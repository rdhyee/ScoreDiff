#This file contains all of the tests for the ScoreDiff class

from ScoreDiff import *
from os.path import abspath

path = abspath('test_cases')

def test_key(score1, score2, measure=0, part=0):

	"""
	   >>> test_key('bwv66.6.mxl', 'different_key.mxl')
	   False

	   >>> test_key('bwv66.6.mxl', 'different_pitches.mxl')
	   True

	   >>> test_key('bwv66.6.mxl', 'different_ornaments.mxl')
	   True

	"""

	diff = ScoreDiff(score1, score2, path)
        return diff.have_same_key(measure, part)

def test_time_signature(score1, score2, measure = 0, part = 0):

	"""
	   >>> test_time_signature('bwv66.6.xml', 'different_time.mxl')
	   False

	   >>> test_time_signature('bwv66.6.mxl', 'different_dynamics.mxl')
	   True

	   >>> test_time_signature('bwv66.6.mxl', 'different_key.mxl')
	   True

	"""

	diff = ScoreDiff(score1, score2, path)
	return diff.have_same_time_signature(measure, part)

def test_ornaments(score1, score2, measure = 0, part = 0):

	"""
	   >>> test_ornaments('bwv66.6.mxl', 'different_ornaments.mxl')
	   False

	   >>> test_ornaments('bwv66.6.mxl', 'different_ornaments2.mxl')
	   False

	   >>> test_ornaments('bwv66.6.mxl', 'different_ornaments3.mxl')
	   False

	   >>> test_ornaments('bwv66.6.mxl', 'different_pitches.mxl')
	   True

	   >>> test_ornaments('bwv66.6.mxl', 'different_key.mxl')
	   True

	"""
	
	diff = ScoreDiff(score1, score2, path)
	return diff.have_same_ornaments(measure, part)

if __name__ == '__main__':

	import doctest
	doctest.testmod()
