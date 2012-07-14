
from music21 import *
from sys import argv

score=argv[1]

us=environment.UserSettings()
us['localCorpusPath']='.'

s=corpus.parse(score)
s.show()

