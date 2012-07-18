This directory is where the finished version will be

Right now the test.py script will show some failed tests when the accidentals
method is called.  It seems the folks at music21 decided to consider sharps
and flats already present in the key signature as accidentals.  I'm working
on an interesting algorithm to fix this problem which should be up shortly.

Another issue not currently addressed is that it is possible for the key signature of a measure to be None.  Generally, the key signature for a measure is only recorded if is a new key signature.  This will also be addressed soon.  
