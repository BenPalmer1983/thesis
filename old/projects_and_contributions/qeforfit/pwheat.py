import numpy
import sys
import os
import matplotlib.pyplot as plt


"""
Example Use:
python3 pwheat.py ru.in 30 0.0001 0.001


ru.in is the file name of a standard pwscf input file, 30 is the number of files to make, 0.0001 is the lower maximum crystal lattice amount to perturb by and 0.001 is the upper maximum crystal lattice amount to perturb by.

"""

class pwheat:

  s = None
  sn = 0

  def main():
    print("pwheat")
    print("=====================")


    if(len(sys.argv) < 2):
      print("Error: give pw input file name")
      print("exiting")
      exit()
    filename = sys.argv[1]
    if(not os.path.isfile(filename)):
      print("Error: file does not exist")
      print("exiting")
      exit()

    fh = open(filename, 'r')
    c = numpy.zeros((3,),)
    lines = []
    for line in fh:
      lines.append(line)
      if("&CONTROL" in line):
        c[0] = 1
      if("ATOMIC_SPECIES " in line):
        c[1] = 1
      if("ATOMIC_POSITIONS " in line):
        c[2] = 1
    fh.close()
   
    if(sum(c) != 3):
      print("Error: file is not a pw input file")
      print("exiting")
      exit()
        
    files = 10
    if(len(sys.argv) > 2):
      try:
        files = int(sys.argv[2])
      except:
        pass
        
    heat_min = 0.01  
    heat_max = 0.01   
    if(len(sys.argv) > 3):
      try:
        heat_min = float(sys.argv[3])
        heat_max = heat_min
      except:
        pass
    if(len(sys.argv) > 4):
      try:
        heat_max = float(sys.argv[4])
      except:
        pass
     
    
    
    mu, sigma = 0, 1.0 
    pwheat.s = numpy.random.normal(mu, sigma, 10000)

    for fn in range(files):
      heat = numpy.random.uniform(heat_min, heat_max)
      pwheat.make(filename, heat, fn)


  def make(filename, heat, fn_in):
    fn = str(fn_in+1)
    while(len(fn)<4):
      fn = "0" + fn
   
  
    outfile = filename.split(".")
    filenamebase = outfile[0] + "_" + str(fn)
    outfile = filenamebase + '.in'
    print('mpirun -n 72 pw.x -in ' + filenamebase + '.in > ' + filenamebase + '.out')
    
    fin = []
    fh = open(filename, 'r')
    for line in fh:
      fin.append(line)
    fh.close()

    for line in fin:
      line = line.strip()
      if("NAT" in line.upper() and "=" in line): 
        f = line.split(",")
        f = f[0]
        f = f.split("=")
        nat = int(f[1])
    
    out = []
    out.append("! " + str(filename) + "  " + str(heat) + "   " + str(fn) + "\n")
    n = 0
    while(n<len(fin)):
      if("ATOMIC_POSITIONS" in fin[n].upper()):
        out.append(fin[n])
        n = n + 1
        for i in range(nat):
          line = pwheat.one_space(fin[n].strip())
          f = line.split(" ")
          label = f[0]
          x = float(f[1])
          y = float(f[2])
          z = float(f[3])
          
          x, pwheat.sn = ((x + heat * pwheat.s[pwheat.sn]) % 1.0), pwheat.sn + 1
          y, pwheat.sn = ((y + heat * pwheat.s[pwheat.sn]) % 1.0), pwheat.sn + 1
          z, pwheat.sn = ((z + heat * pwheat.s[pwheat.sn]) % 1.0), pwheat.sn + 1

          
          
          line = "{0:16s} {1:6f}   {2:6f}   {3:6f}\n". format(label, x, y, z)
          out.append(line)
          n = n + 1
          
      elif("PREFIX" in fin[n].upper()):
        prefix = fin[n].strip()
        prefix = prefix.split("=")
        prefix = prefix[1]
        prefix = prefix.replace('"','')
        prefix = prefix.replace("'","")
        prefix = prefix.replace(",","")
        prefix = prefix.strip() + "_" + str(fn)
        out.append('PREFIX = "' + prefix + '",\n')
        n = n + 1
      else:
        out.append(fin[n])
        n = n + 1
        
    fh = open(outfile, 'w')
    for line in out:
      fh.write(line)
    fh.close()
 
 
 
  def one_space(inp):
    out = ''
    last = None
    for c in inp:
      if(not (last == " " and c == " ")):
        out = out + c
      last = c
    return out
 

if __name__ == "__main__":
  pwheat.main()    

