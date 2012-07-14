import music21.environment
from music21.corpus import base
from ScoreException import *

class ScoreDiff:

	def __init__(self, score1, score2, localCorpusPath = '.'):

		music21.environment.set('localCorpusPath', localCorpusPath)
		self.score1 = base.parse(score1)
		self.score2 = base.parse(score2)


	#convenience method for debugging
	def display(self, score_number = 1):
		
		if (score_number == 1):
			
			self.score1.show()

		elif (score_number == 2):

			self.score2.show()
	
		else:
		
			raise ScoreException("Enter either 1 or 2 if specifying a score number")
		
