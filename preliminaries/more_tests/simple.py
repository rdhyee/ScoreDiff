from music21 import *
from sys import argv

#Set the local corpus path to the current directory
us=environment.UserSettings()
us['localCorpusPath']='.'



#compares the clef markings in score1 against those in score2
def check_clef(score1, score2):

	"""
	   >>> check_clef('bwv66.6.mxl','different_clef.mxl')
	   The scores don't start with the same clef sign

	   >>> check_clef('bwv66.6.mxl','different_accidentals')
	   Both scores start with the same clef sign

	   >>> check_clef('bwv66.6.mxl','different_stems.mxl')
	   Both scores start with the same clef sign


	"""
	
	parsed1=corpus.parse(score1)
	parsed2=corpus.parse(score2)



	if(parsed1.parts[0].measure(0).clef.sign==parsed2.parts[0].measure(0).clef.sign):
		print "Both scores start with the same clef sign"
	else:
		print "The scores don't start with the same clef sign"

#compares the accidentals in score1 against those in score2
def check_accidentals(score1, score2):

	"""
	   >>> check_accidentals('bwv66.6.mxl','different_accidentals')
	   found an accidental in one version that is not in the other version
	   found an accidental in one version that is not in the other version

	   >>> check_accidentals('bwv66.6.mxl','different_clef.mxl')
           The accidentals are the same

	   >>> check_accidentals('bwv66.6.mxl','different_stems.mxl')
	   The accidentals are the same

	"""
	parsed1=corpus.parse(score1)
	parsed2=corpus.parse(score2)
	
	notes1=parsed1.parts[0].measure(0).notes
	notes2=parsed2.parts[0].measure(0).notes


	test=False
	for index in range(0,len(notes1)):
	
		if(notes1[index].pitch.accidental is None and not (notes2[index].pitch.accidental is None)):
			print "found an accidental in one version that is not in the other version"
			test=True
		
       
		elif(notes2[index].pitch.accidental is None and not(notes1[index].pitch.accidental is None)):
			print "found an accidental in one version that is not in the other version"
			test=True
		
	
		elif(notes1[index].pitch.accidental is None and notes2[index].pitch.accidental is None):
			continue	
	
		elif(notes1[index].pitch.accidental.fullName != notes2[index].pitch.accidental.fullName):
			print "found an accidental in one version that is not in the other version"
			test=True

	if(not test):
		print "The accidentals are the same"

#compares the stem directions in score1 against those in score2
def check_stems(score1, score2):
	
	"""
	   >>> check_stems('bwv66.6.mxl', 'different_stems.mxl')
	   found different stem directions
	   found different stem directions

	   >>> check_stems('bwv66.6.mxl','different_accidentals.mxl')
	   The stem directions are the same

	   >>> check_stems('bwv66.6.mxl','different_clef.xml')
	   The stem directions are the same

	"""

	parsed1= corpus.parse(score1)
	parsed2= corpus.parse(score2)

	notes1= parsed1.parts[0].measure(0).notes
	notes2= parsed2.parts[0].measure(0).notes

	test=False
	for index in range(0,len(notes1)):
		if(notes1[index].stemDirection != notes2[index].stemDirection):
			print "found different stem directions"
			test=True
	if(not test):
		print "The stem directions are the same"

#Run the doctests
if __name__=='__main__':
	import doctest
	doctest.testmod()
