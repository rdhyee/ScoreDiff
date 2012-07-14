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

	#convenience method for debugging
	def display(self, score_number = 1):
		
		if (score_number == 1):
			
			self.score1.show()

		elif (score_number == 2):

			self.score2.show()
	
		else:
		
			raise ScoreException("Enter either 1 or 2 if specifying a score number")
	
	def have_same_key_signature(self, msr=0, part=0):

		if (part > len(self.score1.parts)):

			raise ScoreException("part number "+str(part)+" does not exist for "+self.name1)

		elif (part > len(self.score2.parts)):

			raise ScoreException("part number "+str(part)+" does not exist for "+self.name2)

		return self.score1.parts[part].measure(msr).keySignature.pitchAndMode == self.score2.parts[part].measure(msr).keySignature.pitchAndMode

	
			
