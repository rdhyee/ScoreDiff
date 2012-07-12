from music21 import *


us=environment.UserSettings()
us['localCorpusPath']='.'

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

	for index, item in enumerate(notes1):

		if (item.expressions==[] and notes2[index].expressions!=[] 
				or notes2[index].expressions==[] and item.expressions!=[]):
			
			print "different ornaments"
			test=True

		elif (item.expressions==[] and notes2[index].expressions==[]):

			continue
		
		elif (item.expressions[0].classes!=notes2[index].expressions[0].classes):
			
			print "different ornaments"
			test=True
	
	if(not test):
		print "The ornaments are the same"






if __name__=='__main__':
	import doctest
	doctest.testmod()
