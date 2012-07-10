from music21 import *
from sys import argv

us=environment.UserSettings()
us['localCorpusPath']='.'
score1=argv[1]
score2=argv[2]

parsed1=corpus.parse(score1)
parsed2=corpus.parse(score2)

print "Analyzing "+score1+" and "+score2

