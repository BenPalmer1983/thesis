class spellcheck:

  def __init__(self, files):
    self.p = 500
    self.a = 136
    self.b = 13
    self.words = []
    self.tally = []
    for filename in files:
      self.load_words(filename)

  def load_words(self, filename):
    if(len(self.words) == 0):
      for i in range(self.p):
        self.words.append([])
        self.tally.append(0)
  
    fh = open(filename, "r")
    for line in fh:
      word = line.strip().upper()
      key = self.word_key(word)
      self.words[key].append(word)
      self.tally[key] += 1
    fh.close()

  def word_key(self, word):
    key = 0
    for letter in word:
      key = (key + self.a + self.b * ord(letter)) % self.p
    return key
    
  def check(self, word):  
    word = word.strip().upper()
    key = self.word_key(word)
    if(word in self.words[key]): 
      return True
    return False
    
  def check_list(self, word_list):
    bad_words = []
    for word in word_list:
      word = word.strip().upper()
      if(word not in bad_words):
        key = self.word_key(word)
        if(word not in self.words[key]): 
          bad_words.append(word)
    for word in bad_words:
      print(word)
