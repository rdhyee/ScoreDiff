from music21 import *

us=environment.UserSettings()
us['localCorpusPath']='./test_cases'


#compares the starting key signature
#of score1 against the starting
#time signature of score2
def check_key(score1, score2):
	"""
	   >>> check_key('bwv66.6.mxl','different_key.mxl')
	   The two scores do not start in the same key

	   >>> check_key('bwv66.6.mxl','different_pitches.mxl')
	   Both scores start in the same key signature

	   >>> check_key('bwv66.6.mxl','different_time.mxl')
	   Both scores start in the same key signature
	"""
	

	parsed1=corpus.parse(score1)
	parsed2=corpus.parse(score2)



	#for now, I'm only testing the first part and the first measure
	if (parsed1.parts[0].measure(0).keySignature.pitchAndMode==parsed2.parts[0].measure(0).keySignature.pitchAndMode):
		print "Both scores start in the same key signature"
	else:
		print "The two scores do not start in the same key"

#compares the starting time signature of score1 against the
#starting time signature of score2
def check_time(score1, score2):
	
	"""
	   >>> check_time('bwv66.6.mxl','different_time.mxl')
	   The scores do not start in the same time signature
	   
	   >>> check_time('bwv66.6.mxl','different_pitches.mxl')
	   The scores have the same time signature

	   >>> check_time('bwv66.6.mxl','different_key.mxl')
	   The scores have the same time signature

	"""
	parsed1=corpus.parse(score1)
	parsed2=corpus.parse(score2)
	#again, only testing the first part and first measure
	if (parsed1.parts[0].measure(0).timeSignature.numerator==parsed2.parts[0].measure(0).timeSignature.numerator and parsed1.parts[0].measure(0).timeSignature.denominator==parsed2.parts[0].measure(0).timeSignature.denominator):
		print "The scores have the same time signature"

	else:
		print "The scores do not start in the same time signature"

#compares the pitches in score1 against the pitches in score2
def check_pitches(score1, score2):

	"""
	   >>> check_pitches('bwv66.6.mxl','different_pitches.mxl')
	   False

	   >>> check_pitches('bwv66.6.mxl','different_key.mxl')
	   True

	   >>> check_pitches('bwv66.6.mxl','different_time.mxl')
	   True

	"""
	parsed1=corpus.parse(score1)
	parsed2=corpus.parse(score2)

	parsed1_pitches=parsed1.parts[0].pitches
	parsed2_pitches=parsed2.parts[0].pitches
	
	return parsed1_pitches==parsed2_pitches

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

#compare the ornaments in score1 against those in score2
def check_ornaments(score1, score2):
	
	"""
	   >>> check_ornaments('bwv66.6.mxl','different_ornaments.mxl')
	   different ornaments
	   different ornaments

	   >>> check_ornaments('bwv66.6.mxl', 'bwv66.6.mxl')
	   The ornaments are the same

	"""

	parsed1=corpus.parse(score1)
	parsed2=corpus.parse(score2)

	notes1=parsed1.parts[0].measure(0).notes
	notes2=parsed2.parts[0].measure(0).notes

	test=False
	o='Ornament'
	for index, item in enumerate(notes1):
		
		
		if (item.expressions==[] and notes2[index].expressions!=[] 
				or notes2[index].expressions==[] and item.expressions!=[]):
			
			print "different ornaments"
			test=True

		elif (item.expressions==[] and notes2[index].expressions==[]):

			continue
		
		
		elif(o in item.expressions[0].classes and not o in notes2[index].expressions[0].classes or o in notes2[index].expressions[0].classes and not o in item.expressions[0].classes):
				
			print "different ornaments"
			test=True
		
		elif(not o in item.expressions[0].classes and not o in notes2[index].expressions[0].classes):
			
			continue

		elif(item.expressions[0].classes[item.expressions[0].classes.index(o)-1]!=notes2[index].expressions[0].classes[notes2[index].expressions[0].classes.index(o)-1]):

			print "different ornaments"
			test=True
			
	if(not test):
		print "The ornaments are the same"


#This function was originally intended to check for
#phrasing only, but that turned out to be a somewhat
#awkward task, so for now the function compares all spanners
#including slurs, glissandos, etc.  
#Take a look at: http://mit.edu/music21/doc/html/moduleSpanner.html?highlight=spanner
#to read more about spanners
def check_spanners(score1, score2):
	

	"""
	   >>> check_spanners('bwv66.6.mxl','different_phrasing.mxl')
	   False

	   >>> check_spanners('bwv66.6.mxl', 'different_ornaments.mxl')
	   False

	   >>> check_spanners('bwv66.6.mxl', 'different_dynamics.mxl')
	   True

	"""

	parsed1=corpus.parse(score1)
	parsed2=corpus.parse(score2)

	spanner1=parsed1.parts[0].measure(0).notes[0].getSpannerSites()
	spanner2=parsed2.parts[0].measure(0).notes[0].getSpannerSites()

	return spanner1==spanner2

def check_articulations(score1, score2):

	"""
	   >>> check_articulations('bwv66.6.mxl','different_articulations.mxl')
	   True

	   >>> check_articulations('bwv66.6.mxl', 'different_phrasing.mxl')
	   False

	   >>> check_articulations('bwv66.6.mxl', 'different_ornaments.mxl')
	   False

	"""

	parsed1=corpus.parse(score1)
	parsed2=corpus.parse(score2)

	notes1=parsed1.parts[0].measure(0).notes
	notes2=parsed2.parts[0].measure(0).notes

	different_articulations=False

	for index, item in enumerate(notes1):

		if(item.articulations!=notes2[index].articulations):
			different_articulations=True

	return different_articulations


if __name__=='__main__':
	import doctest
	doctest.testmod()
