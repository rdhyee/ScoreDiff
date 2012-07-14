import music21.environment
from music21.corpus import base

class ScoreDiff:

	def __init__(self, score1, score2, localCorpusPath = '.'):

		self.localCorpusPath=localCorpusPath
		music21.environment.set('localCorpusPath', self.localCorpusPath)
		self.score1 = score1
		self.score2 = score2	

	#convenience method for debugging
	def display(self):
		
		s = base.parse(self.score1)
		s.show()
