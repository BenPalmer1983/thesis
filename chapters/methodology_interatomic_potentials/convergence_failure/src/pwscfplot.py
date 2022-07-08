import numpy
import os
import sys
import matplotlib.pyplot as plt




class pwscfplot:

  @staticmethod
  def main():  
    print("Plotting SCF Convergence")

    if(len(sys.argv) < 2):
      print("Please specify pw output file.")
      exit()

    pwfile = sys.argv[1] 
    
    if(not os.path.isfile(pwfile)):
      print("File does not exist.")

    # read file
    fh = open(pwfile, 'r')

    d = []
    for line in fh:
      d.append(line)
    fh.close()

    i = None
    data = []
    m = -1

    for n in range(len(d)):
      if(d[n][0:16] == "     iteration #"):
        iteration = int(d[n][16:20])
        if(iteration == 1):
          m = m + 1
          data.append({'iteration': [], 'total_energy': [], 'scf_accuracy': [], 'total_mag': [], 'absolute_mag': [],})
        data[m]['iteration'].append(int(d[n][16:20]))
      elif("total energy              =" in d[n]):
        data[m]['total_energy'].append(float(d[n][34:49]))
      elif("estimated scf accuracy    <" in d[n]):
        data[m]['scf_accuracy'].append(float(d[n][34:49]))
      elif("total magnetization       =" in d[n]):
        data[m]['total_mag'].append(float(d[n][34:41]))
      elif("absolute magnetization    =" in d[n]):
        data[m]['absolute_mag'].append(float(d[n][34:41]))
  
    pwfn = os.path.basename(pwfile)
    print(pwfn)

    for m in range(len(data)):
      plotname = pwfn.replace(".out", "_total_energy_" + str(m) + ".eps")
      pwscfplot.plot1(data[m]['iteration'], data[m]['scf_accuracy'], data[m]['total_energy'], plotname)
      plotname = pwfn.replace(".out", "_total_mag_" + str(m) + ".eps")
      pwscfplot.plot2(data[m]['iteration'], data[m]['scf_accuracy'], data[m]['total_mag'], plotname)
      plotname = pwfn.replace(".out", "_absolute_mag_" + str(m) + ".eps")
      pwscfplot.plot3(data[m]['iteration'], data[m]['scf_accuracy'], data[m]['absolute_mag'], plotname)




  def plot1(iteration, scf_accuracy, total_energy, plotname):
    fig, ax1 = plt.subplots()
    plt.title("Total Energy")  
    color = 'tab:red'
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Estimated accuracy (Ry)', color=color)
    ax1.set_yscale('log')
    ax1.plot(iteration, scf_accuracy, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Total Energy (Ry)', color=color)  
    ax2.plot(iteration, total_energy, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    fig.tight_layout() 
    plt.savefig('plots/' + plotname)
    plt.close(fig)
    plt.cla()

  def plot2(iteration, scf_accuracy, total_mag, plotname):
    fig, ax1 = plt.subplots()
    plt.title("Total Magnetization")  
    color = 'tab:red'
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Estimated accuracy (Ry)', color=color)
    ax1.set_yscale('log')
    ax1.plot(iteration, scf_accuracy, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Total Magnetization (Bohr mag/cell)', color=color)  
    ax2.plot(iteration, total_mag, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    fig.tight_layout() 
    plt.savefig('plots/' + plotname)
    plt.close(fig)
    plt.cla()

  def plot3(iteration, scf_accuracy, absolute_mag, plotname):
    fig, ax1 = plt.subplots()
    plt.title("Absolute Magnetization")  
    color = 'tab:red'
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Estimated accuracy (Ry)', color=color)
    ax1.set_yscale('log')
    ax1.plot(iteration, scf_accuracy, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Absolute Magnetization (Bohr mag/cell)', color=color)  
    ax2.plot(iteration, absolute_mag, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    fig.tight_layout() 
    plt.savefig('plots/' + plotname)
    plt.close(fig)
    plt.cla()





if __name__ == "__main__":
  pwscfplot.main()    








