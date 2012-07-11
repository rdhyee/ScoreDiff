from music21 import *
from sys import argv

def test1(score1, score2):
	"""
	   >>> test1('bwv66.6.mxl', 'different_pitches.mxl')
	   Both scores start in the same key signature
	   The scores have the same time signature
	   Found a pitch that was not the same
	   Found a pitch that was not the same
	   Found a pitch that was not the same
	   Found a pitch that was not the same
		
	   >>> test1('bwv66.6.mxl','different_key.mxl')
	   The two scores do not start in the same key
	   The scores have the same time signature


	   >>> test1('bwv66.6.mxl', 'different_time.mxl')
	   Both scores start in the same key signature
	   The scores do not start in the same time signature
	   



	"""
	
	us=environment.UserSettings()
	us['localCorpusPath']='.'

	parsed1=corpus.parse(score1)
	parsed2=corpus.parse(score2)




	if (parsed1.parts[0].measure(0).keySignature.pitchAndMode==parsed2.parts[0].measure(0).keySignature.pitchAndMode):
		print "Both scores start in the same key signature"
	else:
		print "The two scores do not start in the same key"


	if (parsed1.parts[0].measure(0).timeSignature.numerator==parsed2.parts[0].measure(0).timeSignature.numerator and parsed1.parts[0].measure(0).timeSignature.denominator==parsed2.parts[0].measure(0).timeSignature.denominator):
		print "The scores have the same time signature"

	else:
		print "The scores do not start in the same time signature"

	parsed1_pitches=parsed1.parts[0].pitches
	parsed2_pitches=parsed2.parts[0].pitches

	for index, pitch in enumerate(parsed1_pitches):
		if not (parsed2_pitches[index]==pitch):
			print "Found a pitch that was not the same"




if __name__=='__main__':
	import doctest
	doctest.testmod()
