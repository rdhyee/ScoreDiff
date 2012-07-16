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

	   >>> test_key('bwv66.6.mxl', 'different_key2.mxl',1)
	   False

	   >>> test_key('bwv66.6.mxl', 'different_key3.mxl', 5)
	   False

	   >>> test_key('bwv66.6.mxl', 'scriabin_opus_2_no1.mxl')
	   False

	"""

	diff = ScoreDiff(score1, score2, path)
        return diff.have_same_key_signature(measure, part)

def test_time_signature(score1, score2, measure = 0, part = 0):

	"""
	   >>> test_time_signature('bwv66.6.xml', 'different_time.mxl')
	   False

	   >>> test_time_signature('bwv66.6.mxl', 'different_dynamics.mxl')
	   True

	   >>> test_time_signature('bwv66.6.mxl', 'different_key.mxl')
	   True

	   >>> test_time_signature('bwv66.6.mxl', 'different_time2.mxl', 5)
	   False

	   >>> test_time_signature('bwv66.6.mxl', 'different_time3.mxl', 4)
	   False

	   
	"""




	diff = ScoreDiff(score1, score2, path)
	return diff.have_same_time_signature(measure, part)


def test_clef(score1, score2, measure = 0, part = 0):

	"""
	   >>> test_clef('bwv66.6.mxl', 'different_clef.mxl')
	   False

	   >>> test_clef('bwv66.6.mxl', 'different_time.mxl')
	   True

	   >>> test_clef('bwv66.6.mxl', 'different_pitches.mxl')
	   True

	   >>> test_clef('bwv66.6.mxl', 'different_clef2.mxl', 1)
	   False

	   >>> test_clef('bwv66.6.mxl', 'different_clef3.mxl', 2)
	   False

	   >>> test_clef('bwv66.6.mxl', 'different_clef3.mxl')
	   True





	"""
	diff = ScoreDiff(score1, score2, path)
	return diff.have_same_clef_markings(measure, part)

def test_pitches(score1, score2, measure = 0, part = 0):

	"""
	   >>> test_pitches('bwv66.6.mxl', 'different_pitches.mxl')
	   False

	   >>> test_pitches('bwv66.6.mxl', 'different_pitches2.mxl', 1)
	   False

	   >>> test_pitches('bwv66.6.mxl', 'different_pitches2.mxl', 2)
	   False

	   >>> test_pitches('bwv66.6.mxl', 'different_dynamics.mxl')
	   True

	   >>> test_pitches('bwv66.6.mxl', 'different_key.mxl')
	   True

	   >>> test_pitches('bwv66.6.mxl', 'different_pitches3.mxl', 3)
	   False


	"""

	diff = ScoreDiff(score1, score2, path)
	return diff.have_same_pitches(measure, part)

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

def test_accidentals(score1, score2, measure = 0, part = 0):

	"""
	   >>> test_accidentals('bwv66.6.mxl', 'different_accidentals.mxl')
	   False

	   >>> test_accidentals('bwv66.6.mxl', 'different_ornaments.mxl')
	   True

	   >>> test_accidentals('bwv66.6.mxl', 'bwv66.6.mxl')
	   True

	   >>> test_accidentals('bwv66.6.mxl', 'different_accidentals2.mxl', 1)
	   False

	   >>> test_accidentals('bwv66.6.mxl', 'different_accidentals3.mxl', 2)
	   False

	   >>> test_accidentals('bwv66.6.mxl', 'different_pitches.mxl')
	   True

	  
	"""
	diff = ScoreDiff(score1, score2, path)
	return diff.have_same_accidentals(measure, part)

def test_stem_directions(score1, score2, measure = 0, part = 0):

	"""
	   >>> test_stem_directions('bwv66.6.mxl', 'different_stems.mxl')
	   False

	   >>> test_stem_directions('bwv66.6.mxl', 'different_stems2.mxl', 1)
	   False

	   >>> test_stem_directions('bwv66.6.mxl', 'different_stems3.mxl', 4)
	   False

	   >>> test_stem_directions('bwv66.6.mxl', 'different_ornaments.mxl')
	   True

	   >>> test_stem_directions('bwv66.6.mxl', 'different_time.mxl')
	   True

	   >>> test_stem_directions('bwv66.6.mxl', 'different_pitches.mxl')
	   True

	"""

	diff = ScoreDiff(score1, score2, path)
	return diff.have_same_stem_directions(measure, part)


def test_spanners(score1, score2, measure = 0, part = 0):

	"""
	   >>> test_spanners('bwv66.6.mxl', 'different_phrasing.mxl')
	   False

	   >>> test_spanners('bwv66.6.mxl', 'different_ornaments.mxl')
	   False

	   >>> test_spanners('bwv66.6.mxl', 'different_pitches.mxl')
	   True

	"""

	diff = ScoreDiff(score1, score2, path)
	return diff.have_same_spanners(measure, part)

if __name__ == '__main__':

	import doctest
	doctest.testmod()
