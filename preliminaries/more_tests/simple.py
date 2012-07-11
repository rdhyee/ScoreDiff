from music21 import *
from sys import argv

us=environment.UserSettings()
us['localCorpusPath']='.'
score1=argv[1]
score2=argv[2]

parsed1=corpus.parse(score1)
parsed2=corpus.parse(score2)

print "Analyzing "+score1+" and "+score2

print "Checking to see if both scores start with the same clef sign..."

if(parsed1.parts[0].measure(0).clef.sign==parsed2.parts[0].measure(0).clef.sign):
	print "Both scores start with the same clef sign"
else:
	print "The scores don't start with the same clef sign"

notes1=parsed1.parts[0].measure(0).notes
notes2=parsed2.parts[0].measure(0).notes

print "Checking to see if the accidentals are the same..."

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

print "Comparing stem directions..."

test=False
for index in range(0,len(notes1)):
	if(notes1[index].stemDirection != notes2[index].stemDirection):
		print "found different stem directions"
		test=True
if(not test):
	print "The stem directions are the same"

print "Finished comparing scores"
print "Goodbye!"
