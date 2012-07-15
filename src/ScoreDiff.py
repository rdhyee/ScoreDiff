"""
File:    ScoreDiff.py
Author:    Julien Dubeau
Purpose:    To provide a class that can be used to compare and display 
            differences between two music scores in the musicxml format
Input:    The class __init__ function takes as input two score names, and an optional
          corpus path if the scores are located elsewhere
"""

import music21.environment
from music21.corpus import base
from ScoreException import *
import math

class ScoreDiff:

    #This ornaments list is used as a reference when comparing ornaments    
    ornaments = ['Appoggiatura', 'GeneralAppoggiatura', 'GeneralMordent', 'HalfStepAppoggiatura',
                 'HalfSetpInvertedAppoggiatura', 'HalfStepInvertedMordent', 'HalfStepMordent', 'HalfStepTrill',
                 'InvertedAppoggiatura', 'InvertedMordent', 'InvertedTurn', 'Mordent', 'Schleifer', 'Shake',
                 'Tremolo', 'Trill', 'Turn', 'WholeStepAppoggiatura', 'WholeStepInvertedAppoggiatura',
                 'WholeStepInvertedMordent', 'WholeStepMordent', 'WholeStepTrill']

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    __init__
    Purpose:    Initializes the ScoreDiff object.
    
    """
    def __init__(self, score1, score2, localCorpusPath='.'):

        music21.environment.set('localCorpusPath', localCorpusPath)
        self.score1 = base.parse(score1)
        self.score2 = base.parse(score2)
        self.name1 = score1
        self.name2 = score2
        
        """ __init__ """
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    display
    Purpose:    To display the differences between the two scores visually
    Input Args:    start_measure:  A measure number to start from.  Defaults to 0
                   end_measure:    A measure number to end at.  Defaults to 0
    Output:    Two partial scores which should allow the user to see the differences side
                by side
    """
    
    def display(self, start_measure=0, end_measure=0):
        
        partial1 = self.score1.measures(start_measure, end_measure)
        partial2 = self.score2.measures(start_measure, end_measure)

        partial1.show()
        partial2.show()
        
        """ display """
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    verify_part_number
    Purpose:    To make sure the part number a user has entered is not outside of the range that makes
                sense for the two scores
    Input:    part:    the part number to check
    Ouput:    The function will raise a ScoreException if the part number is outside the appropriate range
              and will do nothing if the part number is acceptable
    
    """
    def verify_part_number(self, part):

        if (part > len(self.score1.parts)):

            raise ScoreException("part number " + str(part) + " does not exist for " + self.name1)

        if (part > len(self.score2.parts)):

            raise ScoreException("part number " + str(part) + " does not exist for " + self.name2)
    
        """ verify_part_number """
        
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    have_same_key
    Purpose:    To check if the two scores both are in the same key at the specified measure
                and for the specified part
    Input:     msr:    the measure number at which to make the comparison
               part:    the part for which to make the comparison
    Return Value:    a boolean value representing whether or not the keys are the same
    
    """
    def have_same_key(self, msr=0, part=0):

        self.verify_part_number(part)
        
        key_signature1 = self.score1.parts[part].measure(msr).keySignature
        key_signature2 = self.score2.parts[part].measure(msr).keySignature
       
        return key_signature1.pitchAndMode == key_signature2.pitchAndMode

        """ have_same_key """
        
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    have_same_time_signature
    Purpose:    To check if the two scores have the same time signature at the specified
                measure and for the specified part
    Input:    msr:    the measure number at which to make the comparison
              part:   the part for which to make the comparsion
    Return Value:    a boolean value representing whether or not the time signatures are the same
    
    """
    def have_same_time_signature(self, msr=0, part=0):
        
        self.verify_part_number(part)

        time_signature1 = self.score1.parts[part].measure(msr).timeSignature
        time_signature2 = self.score2.parts[part].measure(msr).timeSignature
        numerator1 = time_signature1.numerator
        numerator2 = time_signature2.numerator
        denominator1 = time_signature1.denominator
        denominator2 = time_signature2.denominator
    
        return numerator1 == numerator2 and denominator1 == denominator2 

        """ have_same_time_signature """
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    have_same_pitches
    Purpose:    To check if the two scores have the same pitches at the specified measure
                and for the specified part
    Input:    msr:    the measure number at which to make the comparison
              part:    the part for which to make the comparison
    Return Value:    a boolean value representing whether or not the pithces are the same
    
    
    """
    def have_same_pitches(self, msr=0, part=0):

        self.verify_part_number(part)

        pitches1 = self.score1.parts[part].pitches
        pitches2 = self.score2.parts[part].pitches

        return pitches1 == pitches2

        """ have_same_pitches """
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    have_same_clef_markings
    Purpose:    To check if the two scores have the same clef markings at the
                specified measure and for the specified part
    Input:    msr:    the measure number at which to make the comparison
              part:    the part for which to make the comparison
    Return Value:    a boolean value representing whether or not the clef
                    markings are the same
    
    """
    def have_same_clef_markings(self, msr=0, part=0):

        self.verify_part_number(part)

        clef1 = self.score1.parts[part].measure(msr).clef
        clef2 = self.score2.parts[part].measure(msr).clef

        return clef1.sign == clef2.sign
    
        """ have_same_clef_markings """
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    have_same_accidentals
    Purpose:    To check if the two scores have the same accidentals at the specified measure and for the
                specified part
    Input:    msr:    the measure number at which to make the comparison
              part:    the part for which to make the comparison
    Return Value:    a boolean value representing whether or not the accidentals are the same
    Notes:    Because there is no guarantee that a user will enter in a measure for which
              the number of notes are the same in score1 and score2, the function will iterate through
              only enough notes to cover the smaller of the two measures.
    
    """
    def have_same_accidentals(self, msr=0, part=0):

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

        """ have_same_accidentals """
        
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    have_same_stem_directions
    Purpose:    To check if the two scores have the same stem directions on notes
                at the specified measure and for the specified part
    Input:    msr:    the measure at which the comparison should be made
              part:    the part for which to make the comparison
    Return Value:    a boolean value representing whether or not the stem directions
                    are the same
    Notes:    Because there is no guarantee that a user will enter in a measure for which
              the number of notes are the same in score1 and score2, the function will iterate through
              only enough notes to cover the smaller of the two measures.
    
    """
    
    def have_same_stem_directions(self, msr=0, part=0):

        self.verify_part_number(part)

        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes
        
        for index in range(0, min(len(notes1), len(notes2))):

            if(notes1[index].stemDirection != notes2[index].stemDirection):

                return False

        return True
        """ have_same_stem_directions """
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    have_same_ornaments
    Purpose:    To check if the two scores have the same ornaments on notes
                at the specified measure and for the specified part
    Input:    msr:    the measure at which the comparison should be made
              part:    the part for which to make the comparison
    Return Value:    a boolean representing whether or not the ornaments are the
                    same
    Notes:    Because there is no guarantee that a user will enter in a measure for which
              the number of notes are the same in score1 and score2, the function will iterate through
              only enough notes to cover the smaller of the two measures.

    
    """
    
    def have_same_ornaments(self, msr=0, part=0):
        
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
    
        """ have_same_ornaments """
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    have_same_spanners
    Purpose:    To check if the two scores have the same spanners at the specified measure and
                for the specified part
    Input:    msr:    the measure at which the comparison should be made
              part:    the part for which to make the comparison
    Return Value:    a boolean value representing whether or not the spanners are the same
    Notes:   (1) Because there is no guarantee that a user will enter in a measure for which
              the number of notes are the same in score1 and score2, the function will iterate through
              only enough notes to cover the smaller of the two measures.
            (2)'Spanner' is not exactly a technical music term.  It is a term used by music21
            Some examples of things considered spanners are crescendos, slurs, extended trills,
            and glissandos.  Have a look at the music21 documentation at: 
            http://mit.edu/music21/doc/html/moduleSpanner.html?highlight=spanner#music21.spanner
            
            to read more about spanners
    
    """    
    
    def have_same_spanners(self, msr=0, part=0):
        
        self.verify_part_number(part)
        
        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes
        
        for index in range(0, min(len(notes1), len(notes2))):
            
            if(notes1[index].getSpannerSites() != notes2[index].getSpannerSites()):
                
                return False
            
        return True

        """ have_same_spanners """
        
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Function:    have_same_articulations
    Purpose:    To check if the two scores have the same articulations on notes
                at the specified measure and for the specified part
    Input:    msr:    the measure at which the comparison should be made
              part:    the part for which to make the comparison
    Return Value:    a boolean value representing whether or not the articulations
                    are the same
    Notes:    (1)  Because there is no guarantee that a user will enter in a measure for which
              the number of notes are the same in score1 and score2, the function will iterate through
              only enough notes to cover the smaller of the two measures.
            (2) Have a look at: 
            http://mit.edu/music21/doc/html/moduleArticulations.html?highlight=articulations#music21.articulations
            
            to read more about what music21 considers an articulation to be
    
    """
         
    def have_same_articulations(self, msr=0, part=0):
        
        self.verify_part_number(part)
        
        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes
        
        for index in range(0, min(len(notes1), len(notes2))):
            
            if(notes1[index].articulations != notes2[index].articulations):
                
                return False
            
        return True
    
        """ have_same_articulations """

