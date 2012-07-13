The simple.py script has several functions, each with several doctests
based on the mxl files in the test_cases directory.  The algorithms are 
currently in a simplified form, but many of the same concepts will be
in the finished version.  I am currently considering rewriting some
of the functions to deal directly with musicxml instead of using music21.
This will be significantly more complex, but will obviously improve
efficiency quite a bit. I compared the time it takes to parse a score with
music21 to the time it takes with more light-weight xml parsers, and there
is no noticeable difference.  However, importing from music21 dramatically
slows down the program.  
