import sys

from latex import latex
from spellcheck import spellcheck


    
    
filename = sys.argv[1]
mylatex = latex(filename)
mylatex.word_count()



#spell = spellcheck(['SHARED/python/SINGLE.TXT'])
#spell.check_list(mylatex.word_list)




