
# ScoreDiff #

The goal of this project is to create a simple python tool that can be used to compare two music scores.  

The code will rely on the music21 toolkit, which you can read about and download here: [music21](http://mit.edu/music21/ "music21")

The preliminaries directory above contains some simple test code that I'm using to explore music21. Bits and pieces of it are likely to show up in the finished product.

The simple.py script in each subdirectory of preliminaries has a few functions,
each with several doctests based on the mxl files in the same subdirectory. The tests are meant to be as simple as possible so the algorithms are currently very incomplete.  The tests focus on small portions of the piece rather than the entire piece, since it is straightforward
to take the simple cases I've written and expand them iteratively to cover
the entire piece.

