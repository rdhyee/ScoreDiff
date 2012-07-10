from music21 import *
from sys import argv

us=environment.UserSettings()
us['localCorpusPath']='.'
score1=argv[1]
score2=argv[2]

parsed1=corpus.parse(score1)
parsed2=corpus.parse(score2)

print "Analyzing "+score1+" and "+score2
print "Checking to see if the scores are well-formed..."

if(parsed1.isWellFormedNotation() and parsed2.isWellFormedNotation()):
	print "Both scores are well formed"
else:
	print "At least one of the input scores is not well formed."

print "Comparing Key Signatures..."

if (parsed1.parts[0].measure(0).keySignature.pitchAndMode==parsed2.parts[0].measure(0).keySignature.pitchAndMode):
	print "Both scores start in the same key signature"
else:
	print "The two scores do not start in the same key"

print "Comparing Time Signatures..."

if (parsed1.parts[0].measure(0).timeSignature.numerator==parsed2.parts[0].measure(0).timeSignature.numerator and parsed1.parts[0].measure(0).timeSignature.denominator==parsed2.parts[0].measure(0).timeSignature.denominator):
	print "The scores have the same time signature (at least for first measure)"

else:
	print "The scores do not start in the same time signature"

print "Comparing pitches..."
parsed1_pitches=parsed1.parts[0].pitches
parsed2_pitches=parsed2.parts[0].pitches

for index, pitch in enumerate(parsed1_pitches):
	if not (parsed2_pitches[index]==pitch):
		print "Found a pitch that was not the same"


print "Finished comparing scores"
print "Goodbye!"

