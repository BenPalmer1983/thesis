import numpy
import matplotlib.pyplot as plt





def v(ekin, erest):
  return numpy.sqrt(1-(erest/(ekin+erest))**2)
  
def v_classic(ekin, erest):
  return numpy.sqrt(2*ekin/erest)
  
def ke_classic(v, erest):
  return 0.5 * erest * v**2  
  
erest = 938.27

e = numpy.linspace(0.0, 1000.0, 1000)
v = v(e, erest)
v1 = numpy.linspace(0.0, 1.0, 1000)
e1 = ke_classic(v1, erest)

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 9}

plt.rc('font', **font)
plt.figure(figsize=(5,3.5), dpi=100)

plt.title("Effects of Relativity as Proton Energy Increases")
plt.xlabel("Energy (MeV)")
plt.ylabel("Velocity (c)")
plt.plot(e, v, color='k', ls='solid', label="Relativistic")   
plt.plot(e1, v1, color='k', ls='dashed', label="Classical")   
plt.legend()
plt.savefig("proton_energy.eps")
plt.show()


