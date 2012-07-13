import music21.environment
from music21.corpus import base
from os.path import abspath

music21.environment.set('localCorpusPath', abspath('test_cases'))

"""compares the starting key signature
of score1 against the starting
key signature of score2"""
def have_same_key_signature(score1, score2):
	
	"""
	   >>> have_same_key_signature('bwv66.6.mxl','different_key.mxl')
	   False

	   >>> have_same_key_signature('bwv66.6.mxl','different_pitches.mxl')
	   True

	   >>> have_same_key_signature('bwv66.6.mxl','different_time.mxl')
	   True

	"""
	
	parsed1=base.parse(score1)
	parsed2=base.parse(score2)

	#for now, I'm only testing the first part and the first measure
	if (parsed1.parts[0].measure(0).keySignature.pitchAndMode==
			parsed2.parts[0].measure(0).keySignature.pitchAndMode):
		
		return True
	
	else:
		
		return False	

#compares the starting time signature of score1 against the
#starting time signature of score2
def have_same_time_signature(score1, score2):
	
	"""
	   >>> have_same_time_signature('bwv66.6.mxl','different_time.mxl')
	   False

	   >>> have_same_time_signature('bwv66.6.mxl','different_pitches.mxl')
	   True

	   >>> have_same_time_signature('bwv66.6.mxl','different_key.mxl')
	   True

	"""
	parsed1= base.parse(score1)
	parsed2= base.parse(score2)

	#again, only testing the first part and first measure
	if (parsed1.parts[0].measure(0).timeSignature.numerator==parsed2.parts[0].measure(0).timeSignature.numerator 
			and parsed1.parts[0].measure(0).timeSignature.denominator==parsed2.parts[0].measure(0).timeSignature.denominator):
		
		return True

	else:
		
		return False

#compares the pitches in score1 against the pitches in score2
def have_same_pitches(score1, score2):

	"""
	   >>> have_same_pitches('bwv66.6.mxl','different_pitches.mxl')
	   False

	   >>> have_same_pitches('bwv66.6.mxl','different_key.mxl')
	   True

	   >>> have_same_pitches('bwv66.6.mxl','different_time.mxl')
	   True

	"""
	parsed1= base.parse(score1)
	parsed2= base.parse(score2)

	parsed1_pitches=parsed1.parts[0].pitches
	parsed2_pitches=parsed2.parts[0].pitches
	
	return parsed1_pitches==parsed2_pitches

#compares the clef markings in score1 against those in score2
def have_same_clef_markings(score1, score2):

	"""
	   >>> have_same_clef_markings('bwv66.6.mxl','different_clef.mxl')
	   False

	   >>> have_same_clef_markings('bwv66.6.mxl','different_accidentals')
	   True

	   >>> have_same_clef_markings('bwv66.6.mxl','different_stems.mxl')
	   True

	"""
	
	parsed1= base.parse(score1)
	parsed2= base.parse(score2)

	if(parsed1.parts[0].measure(0).clef.sign==parsed2.parts[0].measure(0).clef.sign):

		return True
	
	else:
		
		return False

#compares the accidentals in score1 against those in score2
def have_same_accidentals(score1, score2):

	"""
	   >>> have_same_accidentals('bwv66.6.mxl','different_accidentals')
           False

	   >>> have_same_accidentals('bwv66.6.mxl','different_clef.mxl')
           True

	   >>> have_same_accidentals('bwv66.6.mxl','different_stems.mxl')
           True

	"""
	parsed1= base.parse(score1)
	parsed2= base.parse(score2)
	
	notes1=parsed1.parts[0].measure(0).notes
	notes2=parsed2.parts[0].measure(0).notes

	for index in range(0,len(notes1)):
	
		if(notes1[index].pitch.accidental is None and not (notes2[index].pitch.accidental is None)):

			return False	
		
       		elif(notes2[index].pitch.accidental is None and not(notes1[index].pitch.accidental is None)):

			return False	
		
	
		elif(notes1[index].pitch.accidental is None and notes2[index].pitch.accidental is None):
		
			continue	
	
		elif(notes1[index].pitch.accidental.fullName != notes2[index].pitch.accidental.fullName):
		
			return False	

	return True

#compares the stem directions in score1 against those in score2
def have_same_stem_directions(score1, score2):
	
	"""
	   >>> have_same_stem_directions('bwv66.6.mxl', 'different_stems.mxl')
	   False

	   >>> have_same_stem_directions('bwv66.6.mxl','different_accidentals.mxl')
	   True

	   >>> have_same_stem_directions('bwv66.6.mxl','different_clef.xml')
	   True

	"""

	parsed1= base.parse(score1)
	parsed2= base.parse(score2)

	notes1= parsed1.parts[0].measure(0).notes
	notes2= parsed2.parts[0].measure(0).notes

	for index in range(0,len(notes1)):

		if(notes1[index].stemDirection != notes2[index].stemDirection):
		
			return False

	return True

#compare the ornaments in score1 against those in score2
def have_same_ornaments(score1, score2):
	
	"""
	   >>> have_same_ornaments('bwv66.6.mxl','different_ornaments.mxl')
	   False

	   >>> have_same_ornaments('bwv66.6.mxl', 'bwv66.6.mxl')
	   True

	   >>> have_same_ornaments('different_ornaments.mxl', 'different_ornaments2.mxl')
	   False

	   >>> have_same_ornaments('different_ornaments.mxl', 'different_ornaments3.mxl')
	   False

	   >>> have_same_ornaments('bwv66.6.mxl', 'different_ornaments2.mxl')
	   False

	   >>> have_same_ornaments('bwv66.6.mxl', 'different_ornaments3.mxl')
	   False

	"""

	parsed1= base.parse(score1)
	parsed2= base.parse(score2)

	notes1=parsed1.parts[0].measure(0).notes
	notes2=parsed2.parts[0].measure(0).notes
	
	o='Ornament'

	for index, item in enumerate(notes1):
		
		
		if (item.expressions==[] and notes2[index].expressions!=[] 
				or notes2[index].expressions==[] and item.expressions!=[]):
			
			return False	

		elif (item.expressions==[] and notes2[index].expressions==[]):

			continue
		
		
		elif(o in item.expressions[0].classes and not o in notes2[index].expressions[0].classes or 
				o in notes2[index].expressions[0].classes and not o in item.expressions[0].classes):

			return False	
				
		elif(not o in item.expressions[0].classes and not o in notes2[index].expressions[0].classes):
			
			continue

		elif(item.expressions[0].classes[item.expressions[0].classes.index(o)-1]
				!=notes2[index].expressions[0].classes[notes2[index].expressions[0].classes.index(o)-1]):

			return False

	return True

"""This function was originally intended to check for
phrasing only, but that turned out to be a somewhat
awkward task, so for now the function compares all spanners
including slurs, glissandos, etc.  
Take a look at: http://mit.edu/music21/doc/html/moduleSpanner.html?highlight=spanner
to read more about spanners"""
def have_same_spanners(score1, score2):
	
	"""
	   >>> have_same_spanners('bwv66.6.mxl','different_phrasing.mxl')
	   False

	   >>> have_same_spanners('bwv66.6.mxl', 'different_ornaments.mxl')
	   False

	   >>> have_same_spanners('bwv66.6.mxl', 'different_dynamics.mxl')
	   True

	"""

	parsed1= base.parse(score1)
	parsed2= base.parse(score2)

	spanner1=parsed1.parts[0].measure(0).notes[0].getSpannerSites()
	spanner2=parsed2.parts[0].measure(0).notes[0].getSpannerSites()

	return spanner1==spanner2

#compares the articulations from score1 against those in score2
def have_same_articulations(score1, score2):

	"""
	   >>> have_same_articulations('bwv66.6.mxl','different_articulations.mxl')
	   False

	   >>> have_same_articulations('bwv66.6.mxl', 'different_phrasing.mxl')
	   True

	   >>> have_same_articulations('bwv66.6.mxl', 'different_ornaments.mxl')
	   True

	"""

	parsed1= base.parse(score1)
	parsed2= base.parse(score2)

	notes1=parsed1.parts[0].measure(0).notes
	notes2=parsed2.parts[0].measure(0).notes


	for index, item in enumerate(notes1):

		if(item.articulations!=notes2[index].articulations):
		
			return False
	
	return True


#Run the doctests
if __name__=='__main__':
	import doctest
	doctest.testmod()
