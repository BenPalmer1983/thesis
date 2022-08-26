
import os








class wordcount:

  lines = []
  text = ''

  def run(topdir, filename):
  
    wordcount.topdir = topdir
    
    lines = []
    wordcount.read(os.path.join(wordcount.topdir, filename), lines)
    
    for line in lines:
      wordcount.text = wordcount.text + line.strip() + '\n '
    
    wordcount.text = wordcount.clean_tags(wordcount.text)
    wordcount.text = wordcount.clean_commands(wordcount.text)
    wordcount.text = wordcount.clean_titles(wordcount.text)
    #wordcount.text = wordcount.clean_inline(wordcount.text)
    wordcount.text = wordcount.clean_misc(wordcount.text)
    wordcount.text = wordcount.single_cr(wordcount.text)
    
    fh = open('combined.txt', 'w') 
    fh.write(wordcount.text)
    fh.close()
    
    
  def clean_tags(text):
    tags = ['equation', 'table', 'figure', 'tikzpicture', 'lstlisting', 'abstract', 'comment', 'appendices']    
    for tag in tags:
      print(tag)
      text = wordcount.clean_tag(text, tag)    
    return text 
    
    
  def clean_tag(text, tag):  
    text_out = ''
    a = 0
    b = 0
    save = True
    begin = '\\begin{' + tag + '}'
    end = '\end{' + tag + '}'
    
    n = 0
    while(n < len(text)):
      if(text[n:n+len(begin)] == begin):
        a = a + 1
        save = False
        #print(text[n:n+len(begin)])
        n = n + len(begin)
      elif(not save and text[n:n+len(end)] == end):
        b = b + 1
        save = True
        #print(text[n:n+len(end)])
        n = n + len(end)
      elif(save):
        text_out = text_out + text[n:n+1]
        n = n + 1  
      else:
        #print(text[n:n+1], end='')
        n = n + 1  
    print(a, b)    
    return text_out
    

            
    
  def clean_commands(text):
    commands = ['newglossaryentry', 'newcommand']    
    for command in commands:
      print(command)
      text = wordcount.clean_command(text, command)    
    return text 
    
  def clean_command(text, command):  
    text_out = ''
    n = 0
    save = True
    cn = 0
    cb = 0
    begin = '\\' + command
    while(n < len(text)):
      if(text[n:n+len(begin)] == begin):
        cn = 0
        cb = 0
        save = False
        n = n + len(begin)    
      elif(text[n:n+1] == "{" and not save):
        cb = cb + 1
        n = n + 1  
      elif(text[n:n+1] == "}" and not save):
        cb = cb - 1
        if(cn > 1):
          if(cb == 0):
            save = True
        cn = cn + 1
        n = n + 1  
      elif(save):
        text_out = text_out + text[n:n+1]
        n = n + 1  
      else:
        n = n + 1 
    return text_out
    
    
    
    
  def clean_titles(text):  
    titles = ['chapter', 'section', 'subsection', 'subsubsection', 'subsubsubsection']
    for t in titles:
      text = wordcount.clean_title(text, t) 
    return text 
    
  def clean_title(text, title):
    text_out = ''
    n = 0
    title = "\\" + title + "{"  
    title_text = '' 
    save = True
    cb = 0
    while(n < len(text)):
      if(text[n:n+len(title)] == title): 
        cb = 0
        title_text = '' 
        save = False
        save_text = True
        n = n + len(title)    
      elif(text[n:n+1] == "{" and not save):
        cb = cb + 1  
        n = n + 1  
      elif(text[n:n+1] == "}" and not save): 
        if(cb == 0):
          save = True 
          text_out = text_out + title_text
        cb = cb - 1
        n = n + 1  
      elif(save):
        text_out = text_out + text[n:n+1]
        n = n + 1  
      else:
        if(text[n:n+1] == "["):
          save_text = False
        elif(not save_text and text[n:n+1] == "]"): 
          save_text = True
        elif(save_text):
          title_text = title_text + text[n:n+1]
        n = n + 1 
    return text_out
    
    
  def clean_inline(text):  
    n = 0
    a = 0
    text_out = ''
    save = True
    while(n < len(text)):
      if(text[n:n+1] == '$' and text[n-1:n] != "\\" ): 
        a = a + 1
        print(a, text[n-5:n+5])
        save = False 
        n = n + 1 
      elif(text[n:n+1] == "$" and not save): 
        save = True 
        n = n + 1  
      elif(save):
        text_out = text_out + text[n:n+1]
        n = n + 1  
      else:
        n = n + 1 
    return text_out
    
    
  def clean_misc(text):  
    text = text.replace("\\\\", "\n")
    text = text.replace("\FloatBarrier", "\n")
    return text
    
    
  def single_cr(text): 
    text_out = ''
    last = None
    for c in text:
      if(not (last == '\n' and c == '\n')):
        text_out = text_out + c
      last = c
    return text_out
    

  def read(filename, lines=[]):
    appendix = False
  
    fh = open(filename, 'r')
    for line in fh:
      line = line.split("%")
      line = line[0].strip()
      if(line != ''):
        if(line[0:6] == "\input"):
          inp = line.split("}")
          inp = inp[0].split("\input{")
          inp_file = os.path.join(wordcount.topdir, inp[1] + ".tex")
          if(os.path.isfile(inp_file)):
            if(appendix):
              wordcount.read(inp_file, lines)
            else:
              if('appendix' not in inp_file):
                wordcount.read(inp_file, lines)
        elif(line[0:9] == "\include{"):
          inp = line.split("}")
          inp = inp[0].split("\include{")
          inp_file = os.path.join(wordcount.topdir, inp[1] + ".tex")
          if(os.path.isfile(inp_file)):
            if(appendix):
              wordcount.read(inp_file, lines)
            else:
              if('appendix' not in inp_file):
                wordcount.read(inp_file, lines)
        else:    
          lines.append(line)    
    fh.close()


wordcount.run('../', 'main.tex')



