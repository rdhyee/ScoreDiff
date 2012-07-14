import music21.environment
from music21.corpus import base
from ScoreException import *

class ScoreDiff:

	def __init__(self, score1, score2, localCorpusPath = '.'):

		music21.environment.set('localCorpusPath', localCorpusPath)
		self.score1 = base.parse(score1)
		self.score2 = base.parse(score2)
		self.name1 = score1
		self.name2 = score2

	"""Useful for displaying the differences.  Be aware that
	finale notepad will distort the note spacing if selecting
	a single measure"""
	def display(self, start_measure = 0, end_measure = 0):
		
		partial1 = self.score1.measures(start_measure, end_measure)
		partial2 = self.score2.measures(start_measure, end_measure)

		partial1.show()
		partial2.show()

	
	def have_same_key(self, msr=0, part=0):

		if (part > len(self.score1.parts)):

			raise ScoreException("part number "+str(part)+" does not exist for "+self.name1)

		elif (part > len(self.score2.parts)):

			raise ScoreException("part number "+str(part)+" does not exist for "+self.name2)

		return self.score1.parts[part].measure(msr).keySignature.pitchAndMode == self.score2.parts[part].measure(msr).keySignature.pitchAndMode

	
			
