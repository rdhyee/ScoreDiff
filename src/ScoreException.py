
#Class used for handling exceptions in ScoreDiff
class ScoreException(Exception):

	def __init__(self , value):

		self.value = value

	def __str__(self):

		return repr(self.value)


