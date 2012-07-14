#This file contains all of the tests for the ScoreDiff class

from ScoreDiff import *
from os.path import abspath

path = abspath('test_cases')

def test_key_signature(score1, score2, measure=0, part=0):

	"""
	   >>> test_key_signature('bwv66.6.mxl', 'different_key.mxl')
	   False

	   >>> test_key_signature('bwv66.6.mxl', 'different_pitches.mxl')
	   True

	   >>> test_key_signature('bwv66.6.mxl', 'different_ornaments.mxl')
	   True

	"""

	diff = ScoreDiff(score1, score2, path)
	return diff.have_same_key_signature(measure, part)

if __name__ == '__main__':

	import doctest
	doctest.testmod()
