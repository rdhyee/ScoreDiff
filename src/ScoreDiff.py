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

    def __init__(self, score1, score2, localCorpusPath='.'):
        """Initializes a ScoreDiff object.
    
        Args:
         score1 (str):  The pathname of a score to parse
         score2 (str):  The pathname of a score to parse and compare to score1

        Kwargs:
         localCorpusPath (str)  A path to a corpus if your files are located elswhere


        """
           
        music21.environment.set('localCorpusPath', localCorpusPath)
        self.score1 = base.parse(score1)
        self.score2 = base.parse(score2)
        self.name1 = score1
        self.name2 = score2
        
           
    def display(self, start_measure=0, end_measure=0):
        """Useful for displaying the differences between the two scores visually

        Kwargs:
          start_measure (int): A measure number to start from
          end_measure (int):  A measure number to end at.
    
    
        """
        partial1 = self.score1.measures(start_measure, end_measure)
        partial2 = self.score2.measures(start_measure, end_measure)

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

	self.verify_part_number(part)

        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes

        for index in range(0, min(len(notes1), len(notes2))):

            if(notes1[index].pitch.accidental is None and not (notes2[index].pitch.accidental is None)):
                
                return False
            
            elif(notes2[index].pitch.accidental is None and not(notes1[index].pitch.accidental is None)):

                return False

            elif(notes1[index].pitch.accidental is None and  notes2[index].pitch.accidental is None):

                continue
            
            elif(notes1[index].pitch.accidental.fullName != notes2[index].pitch.accidental.fullName):

                return False

        return True

               
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

	self.verify_part_number(part)
        
        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes
        
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

	self.verify_part_number(part)

        clef1 = self.score1.parts[part].measure(msr).clef
        clef2 = self.score2.parts[part].measure(msr).clef
	
	if(clef1 == None and not clef2 == None or clef2 == None and not clef1 == None):

		return False

	if(clef1 == None and clef2 == None):

		return True

        return clef1.sign == clef2.sign
    

    def have_same_key(self, msr=0, part=0):
        """Checks if the two scores both are in the same key at the specified measure and for the specified part

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
        
        self.verify_part_number(part)
        
        key_signature1 = self.score1.parts[part].measure(msr).keySignature
        key_signature2 = self.score2.parts[part].measure(msr).keySignature
        
	if(key_signature1 == None and not key_signature2 == None or key_signature2==None and not key_signature1==None):
		
		return False
	
	elif(key_signature1==None and key_signature2==None):
		
		return True
        
	return key_signature1.pitchAndMode == key_signature2.pitchAndMode



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

	self.verify_part_number(part)
        
        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes
        
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

	self.verify_part_number(part)

        pitches1 = self.score1.parts[part].pitches
        pitches2 = self.score2.parts[part].pitches

        return pitches1 == pitches2

    def have_same_spanners(self, msr=0, part=0):
        """Checks if the two scores both have the same spanners at the specified measure and for the specified part [#f1]_
	
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

	self.verify_part_number(part)
        
        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes
        
        for index in range(0, min(len(notes1), len(notes2))):
            
            if(notes1[index].getSpannerSites() != notes2[index].getSpannerSites()):
                
                return False
            
        return True

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

	self.verify_part_number(part)

        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes
        
        for index in range(0, min(len(notes1), len(notes2))):

            if(notes1[index].stemDirection != notes2[index].stemDirection):

                return False

        return True
      

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

	self.verify_part_number(part)

        time_signature1 = self.score1.parts[part].measure(msr).timeSignature
        time_signature2 = self.score2.parts[part].measure(msr).timeSignature
	
	if(time_signature1 == None and not time_signature2 == None or time_signature2 ==None and not time_signature1 == None):

		return False
	
	if(time_signature1 == None and time_signature2 == None):
		
		return True
	
	numerator1 = time_signature1.numerator
        numerator2 = time_signature2.numerator
        denominator1 = time_signature1.denominator
        denominator2 = time_signature2.denominator
    
        return numerator1 == numerator2 and denominator1 == denominator2 

              
    def verify_part_number(self, part):
        """Checks to make sure the part number a user has entered is not outside of the range that exists for either score

        Args:
          part (int): The part number to check

        Raises:
          ScoreException


        """

        if (part > len(self.score1.parts)):

            raise ScoreException("part number " + str(part) + " does not exist for " + self.name1)

        if (part > len(self.score2.parts)):

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

