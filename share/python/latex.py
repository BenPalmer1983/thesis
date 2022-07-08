import sys
import os
import re

class latex:

  def __init__(self, filename):
    self.tex = ""
    self.word_list = []
    self.chapter_tex = []
    self.chapter_titles = []
    self.filename = filename
    self.load()
    self.chapters()
    self.make_word_list()
    
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
          
  def chapters(self):
    self.chapter_tex, self.chapter_titles = self.split_by_tag(self.tex, "\\chapter{", "}")    
  
    
  def word_count(self, chapters=True):
    total = self.word_count_process(self.tex)
    if(chapters):
      for i in range(len(self.chapter_titles)-1):
        word_count = self.word_count_process(self.chapter_tex[i])
        print(word_count, self.chapter_titles[i])
    print(total, "TOTAL")
          
  def word_count_process(self, tex=None):
    if(tex is None):
      tex = self.tex
    words = []
    tex = self.remove_comments(tex)
    tex = self.remove_equations(tex)
    tex = self.remove_figures(tex)
    tex = self.remove_tikz(tex)
    tex = tex.replace("\n", " ")
    tex = tex.replace(".", " ")
    tex = tex.replace(";", " ")
    tex = tex.replace(",", " ")
    tex = tex.replace("?", " ")
    tex = tex.replace("!", " ")
    tempwords = tex.split(" ")
    for word in tempwords:
      word = word.strip()
      if(len(word)>0 and word[0] != "\\" and word[-1] != "}"):
        words.append(word)
    return len(words) 
          
  def make_word_list(self):
    self.word_list = []
    tex = self.tex
    tex = self.remove_comments(tex)
    tex = self.remove_equations(tex)
    tex = self.remove_figures(tex)
    tex = self.remove_tikz(tex)
    tex = tex.replace("\n", " ")
    tex = tex.replace(".", " ")
    tex = tex.replace(";", " ")
    tex = tex.replace(",", " ")
    tex = tex.replace("?", " ")
    tex = tex.replace("!", " ")
    tempwords = tex.split(" ")
    for word in tempwords:
      word = word.strip()
      if(len(word)>0 and word[0] != "\\" and word[-1] != "}"):
        self.word_list.append(word)
          
  def remove_comments(self, tex):
    return re.sub(r'%(.*)\n', '', tex)
          
  def remove_equations(self, tex):
    return self.remove("\\begin{equation}","\\end{equation}", tex)
          
  def remove_inline_equations(self, tex):
    return self.remove("$","$", tex)
          
  def remove_figures(self, tex):
    return self.remove("\\begin{figure}","\\end{figure}", tex)
          
  def remove_tikz(self, tex):
    return self.remove("\\begin{tikzpicture}","\\end{tikzpicture}", tex)
          
  def remove_misc(self, tex):
    tex = re.sub(r'\\item', '', tex)
    tex = re.sub(r'\\begin{itemize}', '', tex)
    return tex


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
    
  def split_by_tag(self, tex, tag_open, tag_close, keep_tag_content = True):
    tex_len = len(tex)
    tag_open_len = len(tag_open)
    tag_close_len = len(tag_close)
    output = ['']
    tag_content = ['Pre-chapters', '']
    counter = 0
  
    reading = True
    i = 0
    while (i < tex_len):
      # If start
      if((i + tag_open_len) < tex_len and tex[i+0:i+tag_open_len] == tag_open):
        reading = False
        i = i + tag_open_len
        output.append('')
      elif(reading == False and (i + tag_close_len) < tex_len and tex[i+0:i+tag_close_len] == tag_close):
        reading = True
        i = i + tag_close_len
        tag_content.append('')
        counter = counter + 1
      elif(reading):
        output[counter] = output[counter] + tex[i]
        i = i + 1
      else:     
        tag_content[counter+1] = tag_content[counter+1] + tex[i]
        i = i + 1
        
    # Return    
    return output, tag_content