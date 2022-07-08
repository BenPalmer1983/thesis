import sys
import os
import re

class latex:

  def __init__(self, filename):
    self.tex = ""
    self.filename = filename
    self.load()
    
  def load(self):
    print("Loading " + self.filename)
    self.load_file(self.filename)

  def load_file(self, filename): 
    newline = chr(10)   
    fh = open(filename, "r")
    for line in fh:
      if("\include" in line):
        incfile = self.include(line) + ".tex"
        if(os.path.isfile(incfile)):
          self.load_file(incfile)
      else:      
        line = line.strip()
        if(line != ""):
          self.tex += line + '\n'
          
  def word_count(self):
    words = []
    temp = self.tex
    self.remove_comments()
    self.remove_equations()
    #self.remove_inline_equations()
    self.remove_figures()
    self.remove_tikz()
    self.tex = self.tex.replace("\n", " ")
    self.tex = self.tex.replace(".", " ")
    self.tex = self.tex.replace(";", " ")
    self.tex = self.tex.replace(",", " ")
    self.tex = self.tex.replace("?", " ")
    self.tex = self.tex.replace("!", " ")
    tempwords = self.tex.split(" ")
    for word in tempwords:
      word = word.strip()
      if(len(word)>0 and word[0] != "\\" and word[-1] != "}"):
        words.append(word)
    print(len(words))    
    self.tex = temp
          
  def remove_comments(self):
    self.tex = re.sub(r'%(.*)\n', '', self.tex)
          
  def remove_equations(self):
    self.tex = self.remove("\\begin{equation}","\\end{equation}", self.tex)
          
  def remove_inline_equations(self):
    self.tex = self.remove("$","$", self.tex)
          
  def remove_figures(self):
    self.tex = self.remove("\\begin{figure}","\\end{figure}", self.tex)
          
  def remove_tikz(self):
    self.tex = self.remove("\\begin{tikzpicture}","\\end{tikzpicture}", self.tex)
          
  def remove_misc(self):
    self.tex = re.sub(r'\\item', '', self.tex)
    self.tex = re.sub(r'\\begin{itemize}', '', self.tex)


  def include(self, line):
    filename = ""
    reading = False
    i = 0
    while (i < len(line)):
      if((i + 9) < len(line) and line[i+0:i+9] == "\include{"):
        reading = True
        i = i + 9
      elif(line[i] == "}"):
        reading = False
        i = i + 1
      elif(reading):
        filename = filename + line[i]
        i = i + 1
      else:        
        i = i + 1
    return filename
    
  def remove(self, start, end, text_in):
    in_len = len(text_in)
    text_out = ""
    reading = True
    i = 0
    start_len = len(start)
    end_len = len(end)
    while (i < in_len):
      if((i + start_len) < in_len and text_in[i+0:i+start_len] == start):
        reading = False
        i = i + start_len
      elif((i + end_len) < in_len and text_in[i+0:i+end_len] == end):
        reading = True
        i = i + end_len
      elif(reading):  
        # Read
        text_out = text_out + text_in[i]
        i = i + 1
      else:  
        # Skip 
        i = i + 1
    return text_out
    
    
filename = sys.argv[1]
mylatex = latex(filename)
mylatex.word_count()








