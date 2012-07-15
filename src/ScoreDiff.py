import music21.environment
from music21.corpus import base
from ScoreException import *
import math

class ScoreDiff:
    
    ornaments = ['Appoggiatura', 'GeneralAppoggiatura', 'GeneralMordent', 'HalfStepAppoggiatura',
                 'HalfSetpInvertedAppoggiatura', 'HalfStepInvertedMordent', 'HalfStepMordent', 'HalfStepTrill',
                 'InvertedAppoggiatura', 'InvertedMordent', 'InvertedTurn', 'Mordent', 'Schleifer', 'Shake',
                 'Tremolo', 'Trill', 'Turn', 'WholeStepAppoggiatura', 'WholeStepInvertedAppoggiatura',
                 'WholeStepInvertedMordent', 'WholeStepMordent', 'WholeStepTrill']

    def __init__(self, score1, score2, localCorpusPath='.'):

        music21.environment.set('localCorpusPath', localCorpusPath)
        self.score1 = base.parse(score1)
        self.score2 = base.parse(score2)
        self.name1 = score1
        self.name2 = score2

    """Useful for displaying the differences.  Be aware that
    finale notepad will distort the note spacing if selecting
    a single measure"""
    def display(self, start_measure=0, end_measure=0):
        
        partial1 = self.score1.measures(start_measure, end_measure)
        partial2 = self.score2.measures(start_measure, end_measure)

        partial1.show()
        partial2.show()

    
    def verify_part_number(self, part):

        if (part > len(self.score1.parts)):

            raise ScoreException("part number " + str(part) + " does not exist for " + self.name1)

        if (part > len(self.score2.parts)):

            raise ScoreException("part number " + str(part) + " does not exist for " + self.name2)
    
    
    def have_same_key(self, msr=0, part=0):

        self.verify_part_number(part)
        
        key_signature1 = self.score1.parts[part].measure(msr).keySignature
        key_signature2 = self.score2.parts[part].measure(msr).keySignature
       
        return key_signature1.pitchAndMode == key_signature2.pitchAndMode

    
    def have_same_time_signature(self, msr=0, part=0):
        
        self.verify_part_number(part)

        time_signature1 = self.score1.parts[part].measure(msr).timeSignature
        time_signature2 = self.score2.parts[part].measure(msr).timeSignature
        numerator1 = time_signature1.numerator
        numerator2 = time_signature2.numerator
        denominator1 = time_signature1.denominator
        denominator2 = time_signature2.denominator
    
        return numerator1 == numerator2 and denominator1 == denominator2 

    
    def have_same_pitches(self, msr=0, part=0):

        self.verify_part_number(part)

        pitches1 = self.score1.parts[part].pitches
        pitches2 = self.score2.parts[part].pitches

        return pitches1 == pitches2

    
    def have_same_clef_markings(self, msr=0, part=0):

        self.verify_part_number(part)

        clef1 = self.score1.parts[part].measure(msr).clef
        clef2 = self.score2.parts[part].measure(msr).clef

        return clef1.sign == clef2.sign
    
    
    def have_same_accidentals(self, msr=0, part=0):

        self.verify_part_number(part)

        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes

        for index in range(0, min(len(notes1),len(notes2))):

            if(notes1[index].pitch.accidental is None and not (notes2[index].pitch.accidental is None)):
                
                return False
            
            elif(notes2[index].pitch.accidental is None and not(notes1[index].pitch.accidental is None)):

                return False

            elif(notes1[index].pitch.accidental is None and  notes2[index].pitch.accidental is None):

                continue
            
            elif(notes1[index].pitch.accidental.fullName != notes2[index].pitch.accidental.fullName):

                return False

        return True

    
    def have_same_stem_directions(self, msr=0, part=0):

        self.verify_part_number(part)

        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes
        
        for index in range(0, min(len(notes1), len(notes2))):

            if(notes1[index].stemDirection != notes2[index].stemDirection):

                return False

        return True
    
    def have_same_ornaments(self, msr = 0, part = 0):
        
        self.verify_part_number(part)
        
        notes1 = self.score1.parts[part].measure(msr).notes
        notes2 = self.score2.parts[part].measure(msr).notes
        
        for index in range(0,min(len(notes1),len(notes2))):
            
            e1 = notes1[index].expressions
            e2 = notes2[index].expressions
            
            if(e1 == [] and not e2 == [] or e2 == [] and not e1 == []):
                
                return False
            
            elif(e1 == [] and e2 == []):
                
                continue
            
            ornaments1 = []
            ornaments2 = []
            
            inner_index=0
            while inner_index < min(len(e1),len(e2)):
                
                if(e1[inner_index] in ScoreDiff.ornaments):
                    
                    ornaments1.append(e1[inner_index])
                
                if(e2[inner_index] in ScoreDiff.ornaments):
                    
                    ornaments2.append(e2[inner_index])
                    
                inner_index+=1
                
            
            if(max(len(e1),len(e2)) == len(e1)):
                left_over = e1
            
            else:
                
                left_over = e2
            
            while inner_index < len(left_over):
                
                if(left_over[inner_index] in ScoreDiff.ornaments):
                    
                    if(left_over == e1):
                        
                        ornaments1.append(left_over[inner_index])
                    else:
                        
                        ornaments2.append(left_over[inner_index])
                
                inner_index+=1
                
            if(ornaments1 != ornaments2):
                
                return False
                    
        return True

        
    

