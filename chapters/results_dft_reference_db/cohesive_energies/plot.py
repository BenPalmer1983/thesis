import os
import sys
import matplotlib.pyplot as plt
import numpy



class plot:


  inp = None
  data = []
  palette = 'hex'

  markers = ['x','+','.','v','o','^','8','s','p']
  linestyle = ["solid", "dashed", "dashdot", "dotted"]
  colours_hex = ["#009933","#CC9900","#0033CC","#CC3300","#6600CC","#000066","#333300","#FF0000","#FF9966","#009999","#993366","#66FF33","#FF0066","#00FFFF","#FFFF00","#990000","#663300"]
  colours_base = ["b", "c", "k", "g", "m", "r", "y"]   # w removed   
  colours_tab = ["tab:blue", "tab:brown", "tab:orange", "tab:pink", "tab:green", "tab:gray", "tab:red", "tab:olive", "tab:purple", "tab:cyan"]
  colours_grey = ["#202020", "#404040", "#606060", "#808080", "#303030", "#505050", "#707070", "#080808", "#181818", "#383838", "#585858", "#282828", "#484848", "#686868", "#787878"]

  mcount = 0
  lscount = 0
  ccount = 0

  @staticmethod
  def run():
    print(sys.argv)
    print("Plotting")
  
    if(len(sys.argv) != 2):      
      print("Provide input file")
      exit()

    input_file = sys.argv[1]
    if(not os.path.isfile(input_file)):
      print("Provide input file")
      exit()

    # Read input file
    plot.inp = inpf.read(input_file)
    
    

    plot.load_plot()
    plot.load_data()

    plot.make_plot()


  @staticmethod
  def load_plot():
    plot.fitpoints = plot.get_data(plot.inp['plot'], 'fitpoints', 101, 'int') 
    plot.palette = plot.get_data(plot.inp['plot'], 'palette', 'hex') 



  @staticmethod
  def load_data():
    fh = open("fit.log", "w")
    fh.close()
    n = 0
    while(True):
      n = n + 1
      k = 'data' + str(n)
      if(k not in plot.inp.keys()):
        break
      else:
        file_name = plot.inp[k]['file'][0]
        
        if(os.path.isfile(file_name)):
          sep = plot.inp[k]['sep'][0]
          data_in = plot.read_csv(file_name, sep)
        
          visible = plot.get_data(plot.inp[k], 'visible', True, 'bool') 
          mx = plot.get_data(plot.inp[k], 'mx', 1.0, 'float')
          my = plot.get_data(plot.inp[k], 'my', 1.0, 'float')
          marker = plot.get_data(plot.inp[k], 'marker', '') 
          colour = plot.get_data(plot.inp[k], 'colour', '')
          line = plot.get_data(plot.inp[k], 'line', '')  
          plottype = plot.get_data(plot.inp[k], 'type', 'line')
          fitmarker = plot.get_data(plot.inp[k], 'fitmarker', 'none')  
          fitline = plot.get_data(plot.inp[k], 'fitline', '')    
          fitcolour = plot.get_data(plot.inp[k], 'fitcolour', '') 

          label = []
          if('label' in plot.inp[k].keys()):
            label = plot.inp[k]['label']

          for i in range(1, len(data_in[0])):
            data = numpy.zeros((len(data_in),2),)
            data[:,0] = mx * data_in[:,0]
            data[:,1] = my * data_in[:,i]

            # Fit data
            fit = plot.get_data(plot.inp[k], 'fit', None)
            fit_data = plot.fit(data[:,0], data[:,1], fit)
            
            marker, colour, line = plot.get_line(marker, colour, line)
            if(fitcolour == 'match' or fitcolour == '*'):
              fitcolour = colour
            fitmarker, fitcolour, fitline = plot.get_line(fitmarker, fitcolour, fitline)

            p = {
              'file_name': file_name,
              'visible': visible,
              'data': data,
              'sep': sep,
              'fit': None,
              'fit_p': None,
              'm': None,
              'marker': marker,
              'colour': colour,
              'type': plottype,
              'line': line,
              'fit': fit,
              'fit_data': fit_data,
              'fitmarker': fitmarker,
              'fitcolour': fitcolour,
              'fitline': fitline,
              'label': label[i % len(label)],
              }

            
            plot.data.append(p)

  @staticmethod
  def fit(x, y, fit_type):
    if(fit_type == None):
      return None
    s = plot.fitpoints 
    fit_data = numpy.zeros((s,2,),)
    fit_data[:,0] = numpy.linspace(numpy.amin(x), numpy.amax(x), s) 
    if(fit_type == "poly2"): 
      p = numpy.polyfit(x, y, 2)
      fit_data[:,1] = plot.fpoly(fit_data[:,0], p)
      plot.fitlog(fit_type, p)
      return fit_data    
    elif(fit_type == "poly3"): 
      p = numpy.polyfit(x, y, 3)
      fit_data[:,1] = plot.fpoly(fit_data[:,0], p)
      plot.fitlog(fit_type, p)
      return fit_data
    elif(fit_type == "poly4"): 
      p = numpy.polyfit(x, y, 4)
      fit_data[:,1] = plot.fpoly(fit_data[:,0], p)
      plot.fitlog(fit_type, p)
      return fit_data
    elif(fit_type == "eosfit"): 
      p = plot.eosfit(x, y)
      fit_data[:,1] = plot.eoscalc(fit_data[:,0], p)
      return fit_data   
    elif(fit_type == "lagrange"): 
      fit_data[:,1] = plot.interp(fit_data[:,0], x, y)
      return fit_data
    return None

  @staticmethod
  def fitlog(fit, p):
    fh = open("fit.log", "a")    
    fh.write(fit)   
    fh.write("\n")
    for pi in p:  
      fh.write(str(pi) + "\n")
    fh.write("\n")      
    fh.close()
 
  @staticmethod
  def fpoly(x, p):
    y = 0.0
    for i in range(len(p)):
      y = y + p[-(i+1)] * x**i
    return y
    
  def eosfit(V, E):  
    eos = {"E0": 0.0, "V0": 0.0, "B0": 0.0, "B0P": 0.0}

    # 2nd order polynomial fit
    poly = numpy.polyfit(V, E, 2)

    # Starting points
    eos['V0'] = (-1 * poly[1]) / (2 * poly[0])
    eos['E0'] = (poly[0] * eos['V0'] * eos['V0']) + (poly[1] * eos['V0']) + poly[2]
    eos['B0'] = 2.0 * poly[0] * eos['V0']
    eos['B0P'] = 2.0
    
    # Parameters
    p = numpy.zeros((4))
    p[0] = eos['V0']
    p[1] = eos['E0']
    p[2] = eos['B0']
    p[3] = eos['B0P']
    
    bestrss = plot.eosrss(V, E, p)
    bestp = numpy.copy(p)

    for i in range(500):
      p[3] = 2.0 + i * 0.01  
      newrss = plot.eosrss(V, E, p)
      if(newrss < bestrss):
        bestrss = newrss 
        bestp = numpy.copy(p)
    p = bestp

    for i in range(1000):
      p[0] = bestp[0] * (1.0 + 0.01 * (0.5 - numpy.random.uniform()))
      p[1] = bestp[1] * (1.0 + 0.01 * (0.5 - numpy.random.uniform()))
      p[2] = bestp[2] * (1.0 + 0.01 * (0.5 - numpy.random.uniform()))
      p[3] = bestp[3] * (1.0 + 0.001 * (0.5 - numpy.random.uniform()))
      newrss = plot.eosrss(V, E, p)
      if(newrss < bestrss):
        bestrss = newrss
        bestp = numpy.copy(p)
    p = bestp

    for i in range(1000):
      p[0] = bestp[0] * (1.0 + 0.001 * (0.5 - numpy.random.uniform()))
      p[1] = bestp[1] * (1.0 + 0.001 * (0.5 - numpy.random.uniform()))
      p[2] = bestp[2] * (1.0 + 0.001 * (0.5 - numpy.random.uniform()))
      p[3] = bestp[3] * (1.0 + 0.0001 * (0.5 - numpy.random.uniform()))
      newrss = plot.eosrss(V, E, p)
      if(newrss < bestrss):
        bestrss = newrss
        bestp = numpy.copy(p)
    p = bestp

    return p

  @staticmethod
  def eoscalc(V, p):
    V0 = p[0]
    E0 = p[1]
    B0 = p[2]
    B0P = p[3]
    eta = (V/V0)**(1/3.0)
    return E0 + (9/16.0) * (B0 * V0) * ((eta*eta - 1)*(eta*eta - 1)) * (6.0 + B0P * (eta * eta - 1) - 4 * eta * eta ) 

  @staticmethod
  def interp(x, xv, yv):
    y = numpy.zeros((len(x),),)
    n = 0
    p = numpy.zeros((4,2,),)
    set = False
    for i in range(len(x)):
      while(not(xv[n] <= x[i] <= xv[n+1])):        
        n = n + 1 
        set = False
      if(not set):
        set = True
        if(n+3 >= len(xv)):
          n = len(xv) - 4
        p[:,0] = xv[n:n+4]
        p[:,1] = yv[n:n+4]
      y[i] = plot.lagrange(x[i], p[:,0], p[:,1])
    return y

  @staticmethod
  def lagrange(x, xv, yv):    
    n = len(xv)
    y = 0
    for i in range (0, n):
      li = 1.0
      for j in range(0,n):
        if(j != i):
          li = li * (x - xv[j]) / (xv[i] - xv[j])
      y = y + li * yv[i]
    return y

  
  @staticmethod
  def eosrss(V, E, p):
    return sum((E - plot.eoscalc(V, p))**2)
  
  @staticmethod
  def get_data(lst, k, empty=None, t=None):
    if(k not in lst.keys()):
      return empty
    if(len(lst[k]) == 1):
      if(t == None):
        return lst[k][0]
      elif(t == "int"):
        return int(lst[k][0])
      elif(t == "float"):
        return float(lst[k][0])
      elif(t == "bool"):
        if(lst[k][0].upper() == "TRUE" or lst[k][0].upper() == "ON"):
          return True
        return False
    return lst[k]
        
  
  @staticmethod
  def make_plot():
    print(plot.inp)
    p = {
        'file_name': 'plot.eps',
        'title': '',
        'xlabel': '',
        'ylabel': '',
        'dpi': 144,
        'w': 8,
        'h': 6,
        'font_family': 'serif',
        'xtick_labelsize': 'x-small',
        'ytick_labelsize': 'x-small',
        }

    # Load input details
    if('name' in plot.inp['output'].keys()):
      p['file_name'] = plot.inp['output']['name'][0]
    if('title' in plot.inp['plot'].keys()):
      p['title'] = plot.inp['plot']['title'][0]
    if('xlabel' in plot.inp['plot'].keys()):
      p['xlabel'] = plot.inp['plot']['xlabel'][0]
    if('ylabel' in plot.inp['plot'].keys()):
      p['ylabel'] = plot.inp['plot']['ylabel'][0]
    if('width' in plot.inp['plot'].keys()):
      p['w'] = float(plot.inp['plot']['width'][0])
    if('height' in plot.inp['plot'].keys()):
      p['h'] = float(plot.inp['plot']['height'][0])

    legend = plot.get_data(plot.inp['plot'], 'legend', False) 


    plt.figure(figsize=(p['w'], p['h']), dpi=p['dpi'])
    plt.rc('font', family=p['font_family'])
    plt.rc('xtick', labelsize=p['xtick_labelsize'])
    plt.rc('ytick', labelsize=p['ytick_labelsize'])
    plt.grid(visible=True, which='major', axis='both')

    plt.title(p['title'])
    plt.xlabel(p['xlabel'])
    plt.ylabel(p['ylabel'])
    #plt.xscale('log')
    #plt.yscale('log')
    for pd in plot.data:   
      if(pd['visible']):
        if(pd['type'] == 'line'):
          plt.plot(pd['data'][:,0], pd['data'][:,1], color=pd['colour'], marker=pd['marker'], ls=pd['line'], label=pd['label']) 
        elif(pd['type'] == 'scatter'):
          plt.scatter(pd['data'][:,0], pd['data'][:,1], color=pd['colour'], marker=pd['marker'], label=pd['label']) 
        if(type(pd['fit_data']) == numpy.ndarray): 
          plt.plot(pd['fit_data'][:,0], pd['fit_data'][:,1], color=pd['fitcolour'], marker=pd['fitmarker'], ls=pd['fitline']) 


    #plt.plot(plot.data[:,0], plot.data[:,1], color='k')  
    if(legend):
      plt.legend()
    plt.savefig(p['file_name'] , format='eps')
    plt.close()



  @staticmethod
  def get_line(m, c, ls):
    m = m.lower().strip()
    c = c.lower().strip()
    cu = c.upper().strip()
    ls = ls.lower().strip()

    # Markers
    if(m == "none"):
      m = ""
    else:
      if(m != "" and m not in plot.markers):
        m = ""
      if(m == ""):
        m = plot.markers[plot.mcount % len(plot.markers)]
        plot.mcount = plot.mcount + 1

    # Colours
    if(c == "none"):
      c = ""
    else:
      if(c != "" and cu not in plot.colours_hex and c not in plot.colours_base and c not in plot.colours_tab and c not in plot.colours_grey):
        c = ""
      if(c == "" and plot.palette == "hex"):
        c = plot.colours_hex[plot.ccount % len(plot.colours_hex)]
        plot.ccount = plot.ccount + 1
      if(c == "" and plot.palette == "tab"):
        c = plot.colours_tab[plot.ccount % len(plot.colours_tab)]
        plot.ccount = plot.ccount + 1
      if(c == "" and plot.palette == "base"):
        c = plot.colours_base[plot.ccount % len(plot.colours_base)]
        plot.ccount = plot.ccount + 1
      if(c == "" and plot.palette == "grey"):
        c = plot.colours_grey[plot.ccount % len(plot.colours_grey)]
        plot.ccount = plot.ccount + 1   

    # Line Style
    if(ls == "none"):
      ls = ""
    else:
      if(ls != "" and ls not in plot.linestyle):
        ls = ""
      if(ls == ""):
        ls = plot.linestyle[plot.lscount % len(plot.linestyle)]
        plot.lscount = plot.lscount + 1

    return m, c, ls

  @staticmethod
  def set(inp1, inp2):
    return inp1

  @staticmethod
  def read_csv(filename, sep=","):
    data = []
    if(os.path.isfile(filename)):
# Read from file into memory
      fh = open(filename, 'r')
      file_data = ""
      for line in fh:
        file_data = file_data + line
      fh.close()
# Remove comments
      file_data = plot.remove_comments_data(file_data)
# Read Data
      lines = file_data.split("\n")
      for line in lines:
        line = line.strip()
        if(line != ""):
          f = line.split(sep)
          for i in range(len(f)):
            f[i] = float(f[i])
          data.append(f)  

    data = numpy.asarray(data)
    data = data[numpy.argsort(data[:, 0])]   

    return numpy.asarray(data)



# Remove comments from a block of data/text
  @staticmethod
  def remove_comments_data(data):
    out = ""
    n = 0
    inquotes = 0
    incomment = 0
    while n < len(data):
# Get char and next char
      char = data[n]
      next = None
      prev = None
      if(n < len(data)-1):
        next = data[n + 1]
      if(n > 0):
        prev = data[n - 1]        
# If in '  '
      if(inquotes == 1 and char != "'" and last_char != "\\"):
        out = out + char
      elif(inquotes == 1 and char == "'" and last_char != "\\"):
        out = out + char
        inquotes = 0
# If in "  "
      elif(inquotes == 2 and char != '"' and last_char != "\\"):
        out = out + char
      elif(inquotes == 2 and char == '"' and last_char != "\\"):
        out = out + char
        inquotes = 0
# If not inside quotes
      elif(inquotes == 0):
# Comment on a line
        if(incomment == 0 and char == "/" and next == "/"):
          incomment = 1
        elif(incomment == 0 and char == "!"):
          incomment = 1
        elif(incomment == 0 and char == "#"):
          incomment = 1    
# Comment on line close
        elif(incomment == 1 and char == "\n"):
          incomment = 0
# Comment block
        elif(incomment == 0 and char == "/" and next == "*"):
          incomment = 3
        elif(incomment == 3 and prev == "*" and char == "/"):
          incomment = 0
        elif(incomment == 0):
          out = out + char  
# Increment counter
      n = n + 1
    return out       



class inpf:
  @staticmethod
  def read(file_path):

    # Input dictionary
    input = {}

    # READ DATA
    d = []
    fh = open(file_path, 'r')
    for line in fh:
      line = line.strip()
      if(len(line) > 0 and line[0] != "#"):
        d.append(line)      
    fh.close()


    for line in d:
      instrs = inpf.split_by(line, sep=' ', ignore_double_sep=True)
      cmd = instrs[0]

      input[cmd] = {}
      for instr in instrs[1:]: 
        f = inpf.split_by(instr.strip(), sep='=', ignore_double_sep=True)
        k = f[0]
        d = inpf.split_by(f[1], sep=',', ignore_double_sep=True)

        for i in range(len(d)):
          
          if((d[i][0] == "'" and d[i][-1] == "'") or (d[i][0] == '"' and d[i][-1] == '"')):
            d[i] = d[i][1:-1]
        input[cmd][k] = d

    """
    for line in d:
      f = line.split(" ")
      cmd = f[0]
      instrs = inpf.split_by(line[len(cmd):].strip(), sep=' ', ignore_double_sep=True)

      input[cmd] = {}
      for instr in instrs:
        f = inpf.split_by(instr.strip(), sep='=', ignore_double_sep=True)
        k = f[0]
        d = inpf.split_by(f[1], sep=',', ignore_double_sep=True)
        input[cmd][k] = d
    """
    return input


  @staticmethod  
  def split_by(line, sep=' ', ignore_double_sep=True):
    last_char = None
    in_quotes = 0
    end_quote = 0
    fields = []
    temp_line = ""    
    for char in line:
      if(char == "'" and in_quotes == 0 and last_char != "\\"):
        in_quotes = 1
        if(last_char != sep):
          temp_line = temp_line + "'"
          end_quote = 1
      elif(char == "'" and in_quotes == 1 and last_char != "\\"):
        in_quotes = 0
        if(end_quote == 1):
          temp_line = temp_line + "'"
          end_quote = 0
      elif(char == '"' and in_quotes == 0 and last_char != "\\"):
        in_quotes = 2
        if(last_char != sep):
          temp_line = temp_line + '"'
          end_quote = 1
      elif(char == '"' and in_quotes == 2 and last_char != "\\"):
        in_quotes = 0
        if(end_quote == 1):
          temp_line = temp_line + '"'
          end_quote = 0
      elif(in_quotes > 0):
        temp_line = temp_line + char
      elif(in_quotes == 0 and char != sep):
        temp_line = temp_line + char
      elif(char == sep and last_char == sep and ignore_double_sep):
        pass
      elif(char == sep):
        fields.append(temp_line)
        temp_line = "" 
    if(temp_line != ""):
      fields.append(temp_line)    
    return fields



"""
class read_config:
  
  @staticmethod
  def read_file(file_path):
  
    # Input dictionary
    input = {}
  
    # READ DATA
    d = []
    fh = open(file_path, 'r')
    for line in fh:
      line = line.strip()
      if(len(line) > 0 and line[0] != "#"):
        d.append(line)      
    fh.close()
    
    # Count commands
    commands = {}
    for line in d:
      fields = read_config.split_by(line, ' ')
      c = fields[0].lower()
      if(c in commands.keys()):
        commands[c] = commands[c] + 1
      else:
        commands[c] = 1
        
    # Prepare input dictionary    
    for k in commands.keys():
      if(commands[k] == 1):
        input[k] = None
      else:
        input[k] = []
    
    # Read Data into input
    for line in d:
      fields = read_config.split_by(line, ' ')
      fkey = fields[0].lower()
      
      fd_size = {}
      for i in range(1, len(fields)):
        f = fields[i]
        fs = f.split("=")
        fc = fs[0].lower()
        if(fc in fd_size.keys()):
          fd_size[fc] = fd_size[fc] + 1
        else:
          fd_size[fc] = 1
          
      # Prepare dictionary   
      fd = {} 
      for k in fd_size.keys():
        if(fd_size[k] == 1):
          fd[k] = None
        else:
          fd[k] = []        
        
      for i in range(1, len(fields)):
        f = fields[i]
        fs = f.split("=")     
        fc = fs[0].lower()        
        fs = read_config.split_by(fs[1], ',')         
        fs = read_config.store(fs)
        
        if(fd_size[fc] == 1):
          if(len(fs) == 1):
            fd[fc] = read_config.store(fs[0])
          else:
            fd[fc] = read_config.store(fs)
        else:
          if(len(fs) == 1):
            fd[fc].append(read_config.store(fs[0]))
          else:
            fd[fc].append(read_config.store(fs))
            
      if(commands[fkey] == 1):
        input[fkey] = fd
      else:
        input[fkey].append(fd)  

    return input
        
        
    
  @staticmethod  
  def split_by(line, sep=' ', ignore_double_sep=True):
    last_char = None
    in_quotes = 0
    fields = []
    temp_line = ""
    
    for char in line:
      if(char == "'" and in_quotes == 0 and last_char != "\\"):
        in_quotes = 1
      elif(char == "'" and in_quotes == 1 and last_char != "\\"):
        in_quotes = 0
      elif(char == '"' and in_quotes == 0 and last_char != "\\"):
        in_quotes = 2
      elif(char == '"' and in_quotes == 2 and last_char != "\\"):
        in_quotes = 0
      elif(in_quotes > 0):
        temp_line = temp_line + char
      elif(in_quotes == 0 and char != sep):
        temp_line = temp_line + char
      elif(char == sep and last_char == sep and ignore_double_sep):
        pass
      elif(char == sep):
        fields.append(temp_line)
        temp_line = "" 
    if(temp_line != ""):
      fields.append(temp_line)
    
    return fields
    
    
  @staticmethod
  def store(inp):  
    if(isinstance(inp, list)):
      for i in range(len(inp)):
        try:
          if('.' in inp[i]  or 'e' in inp[i]):
            inp[i] = float(inp[i])
          else:
            inp[i] = int(inp[i])
        except:
          pass
    else:
      try:
        if('.' in inp or 'e' in inp):
          inp = float(inp)
        else:
          inp = int(inp)
      except:
        pass
    return inp
"""




def main():
  plot.run()

if __name__ == "__main__":
    main()    
