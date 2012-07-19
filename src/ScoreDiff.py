"""

.. module:: ScoreDiff
    :synopsis: A module for comparing two musicxml files and displaying the differences

..  moduleauthor:: Julien Dubeau <jdubeau@dons.usfca.edu>


"""

import music21.environment
from music21.corpus import base

import math


class ScoreDiff:
    """The ScoreDiff class uses the music21 toolkit to parse and analyze two scores passed
    to the initialization function, so that the user can detect and display certain differences.

    """
    
    #This ornaments list is used as a reference when comparing ornaments    
    ornaments = ['Appoggiatura', 'GeneralAppoggiatura', 'GeneralMordent', 'HalfStepAppoggiatura',
                 'HalfSetpInvertedAppoggiatura', 'HalfStepInvertedMordent', 'HalfStepMordent', 'HalfStepTrill',
                 'InvertedAppoggiatura', 'InvertedMordent', 'InvertedTurn', 'Mordent', 'Schleifer', 'Shake',
                 'Tremolo', 'Trill', 'Turn', 'WholeStepAppoggiatura', 'WholeStepInvertedAppoggiatura',
                 'WholeStepInvertedMordent', 'WholeStepMordent', 'WholeStepTrill']

    def __init__(self, score1, score2, localCorpusPath = '.'):
        """Initializes a ScoreDiff object.
    
        Args:
         score1 (str):  The pathname of a score to parse
         
	 score2 (str):  The pathname of a score to parse and compare to score1

        Kwargs:
         localCorpusPath (str)  A path to a corpus if your files are located elsewhere

	 
        """        
	music21.environment.set('localCorpusPath', localCorpusPath)
        self.score1 = base.parse(score1)
       	self.score2 = base.parse(score2)
        self.name1 = score1
        self.name2 = score2
	
    def display(self, msr=0, part=0):
        """Useful for displaying the differences between the two scores visually

        Kwargs:
          msr (int): A measure number to display

	  part (int): A part number to examine.  If not specified then all parts are displayed
          
	  
        """
	self.__verify_part_and_measure__(msr, part)	
	
	partial1 = self.score1.parts[part].getElementsByClass('Measure')[msr]
	partial2 = self.score2.parts[part].getElementsByClass('Measure')[msr]
        partial1.show()
        partial2.show()

    def have_same_accidentals(self, msr=0, part=0):
        """Checks if the two scores both have the same accidentals at the specified measure and for the specified part

        Kwargs:
          msr (int):  the measure number at which to make the comparison
          
	  part (int): the part for which to make the comparison

        Returns:
           boolean.   The result of the comparison::

            True -- The scores have the same accidentals
            False -- The scores do not have the same accidentals

        Raises:
          ScoreException
       

        """
	self.__verify_part_and_measure__(msr, part)

        measures1 = self.score1.parts[part].getElementsByClass('Measure')
	measures2 = self.score2.parts[part].getElementsByClass('Measure')
	notes1 = measures1[msr].flat.notes
        notes2 = measures2[msr].flat.notes
	accidentals1 = []
	accidentals2 = []

	if(measures1[msr].keySignature == None):
		
		measure_of_last_key_change = self.__get_most_recent_key__(msr, part, 1)
		altered1 = self.score1.parts[part].measure(measure_of_last_key_change).keySignature.alteredPitches
		altered1 = [x.name for x in altered1]
		
	else:

		altered1 = measures1[msr].keySignature.alteredPitches
		altered1 = [x.name for x in altered1]

	if(measures2[msr].keySignature == None):
		
		measure_of_last_key_change = self.__get_most_recent_key__(msr, part, 2)
		altered2 = self.score1.parts[part].measure(measure_of_last_key_change).keySignature.alteredPitches
		altered2 = [x.name for x in altered2]
	else:
		
		altered2 = measures2[msr].keySignature.alteredPitches
		altered2 = [x.name for x in altered2]

        for index in range(0, min(len(notes1), len(notes2))):

        	if(notes1[index].isChord):

			for pitch in notes1[index].pitches:

				if(not pitch.accidental is None and not pitch.name in altered1):

					accidentals1.append(pitch.accidental)

		elif(not notes1[index].accidental is None and not notes1[index].name in altered1):

			accidentals1.append(notes1[index].accidental)
            		
		if(notes2[index].isChord):

			for  pitch in notes2[index].pitches:

				if(not pitch.accidental is None and not pitch.name in altered2):

					accidentals2.append(pitch.accidental)

		elif(not notes2[index].accidental is None and not notes2[index].name in altered2):

			accidentals2.append(notes2[index].accidental)

	
	return accidentals1 == accidentals2

    def __get_most_recent_key__(self, msr=0, part=0, score_number=1):
        """Gets the measure number of the most recent key change
	
	Kwargs:
	  msr (int): measure number that is used to determine what is considered the most recent key change

	  part (int): the part to examine

	  score_number (int): A score number so the function knows which score to analyze

	"""
	if(score_number == 1):

		keys = self.score1.parts[part].flat.getKeySignatures()
		target_measure = self.score1.parts[part].getElementsByClass('Measure')[msr].notes[0].measureNumber

	elif(score_number == 2):

		keys = self.score2.parts[part].flat.getKeySignatures()
		target_measure = self.score2.parts[part].getElementsByClass('Measure')[msr].notes[0].measureNumber
	
	current = 0

	for key in keys:

		if(key.measureNumber > current and key.measureNumber <= target_measure):

			current = key.measureNumber

	return current	

    def have_same_articulations(self, msr=0, part=0):
        """Checks if the two scores both have the same articulations at the specified measure and for the specified part [#f2]_
	
	Kwargs:
          msr (int):  the measure number at which to make the comparison
          
	  part (int): the part for which to make the comparison

        Returns:
          boolean.   The result of the comparison::

           True -- The scores have the same articulations
           False -- The scores do not have the same articulations

        Raises:
          ScoreException
       

        """

	self.__verify_part_and_measure__(msr, part)
        
        
	notes1 = self.score1.parts[part].getElementsByClass('Measure')[msr].flat.notes
        notes2 = self.score2.parts[part].getElementsByClass('Measure')[msr].flat.notes
        
        for index in range(0, min(len(notes1), len(notes2))):
            
            if(notes1[index].articulations != notes2[index].articulations):
                
                return False
            
        return True

    def have_same_clef_markings(self, msr=0, part=0):
        """Checks if the two scores both have the same clef markings at the specified measure and for the specified part

        Kwargs:
          msr (int):  the measure number at which to make the comparison
          
	  part (int): the part for which to make the comparison

        Returns:
          boolean.   The result of the comparison::

           True -- The scores have the same clef markings
           False -- The scores do not have the same clef markings

        Raises:
          ScoreException
       
        """

	self.__verify_part_and_measure__(msr, part)

        clef1 = self.score1.parts[part].getElementsByClass('Measure')[msr].clef
        clef2 = self.score2.parts[part].getElementsByClass('Measure')[msr].clef
	
	if(clef1 == None and not clef2 == None or clef2 == None and not clef1 == None):

		return False

	if(clef1 == None and clef2 == None):

		return True

        return clef1.sign == clef2.sign
    

    def have_same_key_signature(self, msr=0, part=0):
        """Checks if the two scores both have the same key signature at the specified measure and for the specified part

        Kwargs:
          msr (int):  the measure number at which to make the comparison
          
	  part (int): the part for which to make the comparison

        Returns:
          boolean.   The result of the comparison::

           True -- The scores have the same key
           False -- The scores do not have the same key

        Raises:
          ScoreException
       

        """
        self.__verify_part_and_measure__(msr, part)
        measures1 = self.score1.parts[part].getElementsByClass('Measure')
	measures2 = self.score2.parts[part].getElementsByClass('Measure')
	key_signature1 = measures1[msr].keySignature
        key_signature2 = measures2[msr].keySignature

	if(key_signature1 == None):

		keys = self.score1.parts[part].flat.getKeySignatures()

		current = 0
		target_measure = measures1[msr].notes[0].measureNumber

		for key in keys:

			if(key.measureNumber > current and key.measureNumber <= target_measure):

				current = key.measureNumber

		key_signature1 = self.score1.parts[part].measure(current).keySignature

	if(key_signature2 == None):

		keys = self.score2.parts[part].flat.getKeySignatures()

		current = 0
		target_measure = measures2[msr].notes[0].measureNumber

		for key in keys():

			if(key.measureNumber > current and key.measureNumber <= target_measure):

				current = key.measureNumber

		key_signature2 = self.score2.parts[part].measure(current).keySignature
        

	return key_signature1.sharps == key_signature2.sharps


    def have_same_ornaments(self, msr=0, part=0):
        """Checks if the two scores both have the same ornaments at the specified measure and for the specified part

        Kwargs:
          msr (int):  the measure number at which to make the comparison
          
	  part (int): the part for which to make the comparison

        Returns:
          boolean.   The result of the comparison::

           True -- The scores have the same ornaments
           False -- The scores do not have the same ornaments

        Raises:
          ScoreException
       
        """

	self.__verify_part_and_measure__(msr, part)
        
        notes1 = self.score1.parts[part].getElementsByClass('Measure')[msr].flat.notes
        notes2 = self.score2.parts[part].getElementsByClass('Measure')[msr].flat.notes
        
        for index in range(0, min(len(notes1), len(notes2))):
            
            e1 = notes1[index].expressions
            e2 = notes2[index].expressions
            
            if(e1 == [] and not e2 == [] or e2 == [] and not e1 == []):
                
                return False
            
            elif(e1 == [] and e2 == []):
                
                continue
            
            ornaments1 = []
            ornaments2 = []
            
            inner_index = 0
            while inner_index < min(len(e1), len(e2)):
                
                if(e1[inner_index] in ScoreDiff.ornaments):
                    
                    ornaments1.append(e1[inner_index])
                
                if(e2[inner_index] in ScoreDiff.ornaments):
                    
                    ornaments2.append(e2[inner_index])
                    
                inner_index += 1
                
            
            if(max(len(e1), len(e2)) == len(e1)):
                
                left_over = e1
            
            else:
                
                left_over = e2
            
            while inner_index < len(left_over):
                
                if(left_over[inner_index] in ScoreDiff.ornaments):
                    
                    if(left_over == e1):
                        
                        ornaments1.append(left_over[inner_index])
                    else:
                        
                        ornaments2.append(left_over[inner_index])
                
                inner_index += 1
                
            if(ornaments1 != ornaments2):
                
                return False
                    
        return True
    
    
    def have_same_pitches(self, msr=0, part=0):
        """Checks if the two scores both have the same pitches at the specified measure and for the specified part
	
	.. note:: This function will compares pitches in the order that they occur.  To compare without considering order, use have_same_pitches_ignore_order.

        
	Kwargs:
          msr (int):  the measure number at which to make the comparison
          
	  part (int): the part for which to make the comparison

        Returns:
          boolean.   The result of the comparison::

           True -- The scores have the same pitches
           False -- The scores do not have the same pitches

        Raises:
          ScoreException
       
        """

	self.__verify_part_and_measure__(msr, part)

        pitches1 = self.score1.parts[part].getElementsByClass('Measure')[msr].flat.notes.pitches
        pitches2 = self.score2.parts[part].getElementsByClass('Measure')[msr].flat.notes.pitches

        return pitches1 == pitches2


    def have_same_pitches_ignore_order(self, msr=0, part=0):
        """Checks if the two scores both have the same pitches at the specified measure and for the specified part

        .. note:: This function will determine if the same pitches are present without considering the order in which they appear.

        Kwargs:
          msr (int): the measure number at which to make the comparison

	  part (int): the part for which to make the comparison

        Returns:
          boolean.  The result of the comparison::

	    True -- The scores have the same pitches
	    False -- The scores do not have the same pitches

        Raises:
	   ScoreException

	"""

	self.__verify_part_and_measure__(msr, part)

	pitches1 = sorted(self.score1.parts[part].getElementsByClass('Measure')[msr].flat.notes.pitches)
        pitches2 = sorted(self.score2.parts[part].getElementsByClass('Measure')[msr].flat.notes.pitches)

        return pitches1 == pitches2
	



    def have_same_spanners(self, msr=0, part=0):
        """Checks if the two scores both have the same spanner sites at the specified measure and for the specified part [#f1]_
	
	Kwargs:
          msr (int):  the measure number at which to make the comparison
          
	  part (int): the part for which to make the comparison

        Returns:
          boolean.   The result of the comparison::

           True -- The scores have the same spanners
           False -- The scores do not have the same spanners

        Raises:
          ScoreException
       
        """

	self.__verify_part_and_measure__(msr, part)
        
        notes1 = self.score1.parts[part].getElementsByClass('Measure')[msr].flat.notes
        notes2 = self.score2.parts[part].getElementsByClass('Measure')[msr].flat.notes

	spanners1=[]
	spanners2=[]

	for index in range(0, min(len(notes1), len(notes2))):

		if(notes1[index].isChord):

			for pitch in notes1[index].pitches:

				spanners1 += pitch.getSpannerSites()

		else:

			spanners1 += notes1[index].getSpannerSites()

		if(notes2[index].isChord):

			for pitch in notes2[index].pitches:

				spanners2 += pitch.getSpannerSites()

		else:

			spanners2 += notes2[index].getSpannerSites()
	

        return spanners1 == spanners2


    def have_same_stem_directions(self, msr=0, part=0):
        """Checks if the two scores both have the same stem directions at the specified measure and for the specified part

        Kwargs:
          msr (int):  the measure number at which to make the comparison
          
	  part (int): the part for which to make the comparison

        Returns:
          boolean.   The result of the comparison::

           True -- The scores have the same stem directions
           False -- The scores do not have the same stem directions

        Raises:
          ScoreException
       
        """

	self.__verify_part_and_measure__(msr, part)

        notes1 = self.score1.parts[part].getElementsByClass('Measure')[msr].flat.notes
        notes2 = self.score2.parts[part].getElementsByClass('Measure')[msr].flat.notes

        stems1=[]
	stems2=[]
        
	for index in range(0, min(len(notes1), len(notes2))):

		if(notes1[index].isChord):

			for pitch in notes1[index].pitches:

				stems1+=[notes1[index].getStemDirection(pitch)]

			stems1 = list(set(stems1))
			
		else:

			stems1+=[notes1[index].stemDirection]
	
		if(notes2[index].isChord):

			for pitch in notes2[index].pitches:

				stems2+=[notes2[index].getStemDirection(pitch)]

			stems2 = list(set(stems2))

		else:

			stems2+=[notes2[index].stemDirection]
			
        return stems1 == stems2
      
   	
    def have_same_time_signature(self, msr=0, part=0):
        """Checks if the two scores both have the same time signature at the specified measure and for the specified part

        Kwargs:
          msr (int):  the measure number at which to make the comparison
          
	  part (int): the part for which to make the comparison

        Returns:
          boolean.   The result of the comparison::

           True -- The scores have the same time signature
           False -- The scores do not have the same time signature

        Raises:
          ScoreException
       
        """

	self.__verify_part_and_measure__(msr, part)

        time_signature1 = self.score1.parts[part].getElementsByClass('Measure')[msr].timeSignature
        time_signature2 = self.score2.parts[part].getElementsByClass('Measure')[msr].timeSignature
	
	if(time_signature1 == None and not time_signature2 == None or time_signature2 ==None and not time_signature1 == None):

		return False
	
	if(time_signature1 == None and time_signature2 == None):
		
		return True
	
	numerator1 = time_signature1.numerator
        numerator2 = time_signature2.numerator
        denominator1 = time_signature1.denominator
        denominator2 = time_signature2.denominator
    
        return numerator1 == numerator2 and denominator1 == denominator2 

              
    def __verify_part_and_measure__(self, msr, part):
        """Checks to make sure the part and measure numbers a user has entered are not outside of the range that exists for either score

        Args:
          part (int): The part number to check

	  msr (int): The measure number to check

        Raises:
          ScoreException

        """
	self.__verify_part__(part)

	if (msr >= len(self.score1.parts[part].getElementsByClass('Measure').elements) or msr < 0):

		raise ScoreException("measure number "+str(msr) + "does not exist for "+self.name1)
	
	if (msr >= len(self.score2.parts[part].getElementsByClass('Measure').elements) or msr < 0):
		
		raise ScoreException("measure number "+str(msr) + "does not exist for "+self.name2)


    def __verify_part__(self, part):
        """Checks to make sure the part number a user has entered is not outside the range that exists for either score

	Args:
	  part (int): The part number to check

	Raises:
	  ScoreException

	"""
	if (part >= len(self.score1.parts) or part < 0):

        	raise ScoreException("part number " + str(part) + " does not exist for " + self.name1)

        if (part >= len(self.score2.parts) or part < 0):

        	raise ScoreException("part number " + str(part) + " does not exist for " + self.name2)


class ScoreException(Exception):
	"""Class for handling exceptions while using the ScoreDiff tool


	"""
        def __init__(self , value):
		"""Initializes the ScoreException object

		Args:
		 value (str): An error message

		"""
		self.value = value

	def __str__(self):
		"""Function for fetching this object's error message
		Returns:
		 This object's error message

		"""
		return repr(self.value)

"""

.. rubric:: Footnotes

.. [#f2] http://mit.edu/music21/doc/html/moduleArticulations.html?highlight=articulation#music21.articulations

.. [#f1] http://mit.edu/music21/doc/html/moduleSpanner.html

"""

