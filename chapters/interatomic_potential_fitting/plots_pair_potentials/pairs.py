import numpy
import matplotlib.pyplot as plt

class pot_plot:

  def run():
    x = numpy.linspace(1.0, 7, 100)
    y = pot_plot.lennard_jones(x, [2.3,3.5])
    y_a = pot_plot.lennard_jones_a(x, [2.3,3.5])
    y_b = pot_plot.lennard_jones_b(x, [2.3,3.5])
    dy = pot_plot.grad(pot_plot.lennard_jones, x, [2.3,3.5])

    plt.clf()   
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='small')
    plt.rc('ytick', labelsize='small')
    fig, axs = plt.subplots(1, 1, figsize=(7,5))
    fig.tight_layout(pad=5.0)    
    fig.suptitle('Lennard-Jones Potential')
    axs.plot(x, y, color='k', ls='solid', label='potential')
    axs.plot(x, y_a, color='k', ls='dashed', label='repulsion')
    axs.plot(x, y_b, color='k', ls='dotted', label='attraction')
    axs.plot(x, dy, color='k', ls='dashdot', label='gradient')
    axs.set_ylim(-5.0,5.0)
    axs.set_xlabel('Radius (angs)')
    axs.set_ylabel('Energy (eV)')
    axs.legend()
    plt.savefig('lennard_jones.eps', format='eps')


    x = numpy.linspace(0.1, 7, 100)
    y = pot_plot.morse(x, [4.669,1.256,2.8])
    y_a = pot_plot.morse_a(x, [4.669,1.256,2.8])
    y_b = pot_plot.morse_b(x, [4.669,1.256,2.8])
    dy = pot_plot.grad(pot_plot.morse, x, [4.669,1.256,2.8])


    plt.clf()   
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='small')
    plt.rc('ytick', labelsize='small')
    fig, axs = plt.subplots(1, 1, figsize=(7,5))
    fig.tight_layout(pad=5.0)    
    fig.suptitle('Morse Potential')
    axs.plot(x, y, color='k', ls='solid', label='potential')
    axs.plot(x, y_a, color='k', ls='dashed', label='repulsion')
    axs.plot(x, y_b, color='k', ls='dotted', label='attraction')
    axs.plot(x, dy, color='k', ls='dashdot', label='gradient')
    axs.set_ylim(-5.0,5.0)
    axs.set_xlabel('Radius (angs)')
    axs.set_ylabel('Energy (eV)')
    axs.legend()
    plt.savefig('morse.eps', format='eps')


    x = numpy.linspace(0.1, 7, 100)
    y = pot_plot.buckingham(x, [6.0,0.5,12.0])
    y_a = pot_plot.buckingham_a(x, [6.0,0.5,12.0])
    y_b = pot_plot.buckingham_b(x, [6.0,0.5,12.0])
    dy = pot_plot.grad(pot_plot.buckingham, x, [6.0,0.5,12.0])

    plt.clf()   
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='small')
    plt.rc('ytick', labelsize='small')
    fig, axs = plt.subplots(1, 1, figsize=(7,5))
    fig.tight_layout(pad=5.0)    
    fig.suptitle('Buckingham Potential')
    axs.plot(x, y, color='k', ls='solid', label='potential')
    axs.plot(x, y_a, color='k', ls='dashed', label='repulsion')
    axs.plot(x, y_b, color='k', ls='dotted', label='attraction')
    axs.plot(x, dy, color='k', ls='dashdot', label='gradient')
    axs.set_ylim(-5.0,5.0)
    axs.set_xlabel('Radius (angs)')
    axs.set_ylabel('Energy (eV)')
    axs.legend()
    plt.savefig('buckingham.eps', format='eps')

    x = numpy.linspace(0.1, 7, 100)
    y = pot_plot.zbl(x, [26,26])
    dy = pot_plot.grad(pot_plot.zbl, x, [26,26])

    plt.clf()   
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='small')
    plt.rc('ytick', labelsize='small')
    fig, axs = plt.subplots(1, 1, figsize=(7,5))
    fig.tight_layout(pad=5.0)    
    fig.suptitle('ZBL')
    axs.plot(x, y, color='k', ls='solid', label='potential')
    axs.plot(x, dy, color='k', ls='dashdot', label='gradient')
    axs.set_ylim(-5.0,5.0)
    axs.set_xlabel('Radius (angs)')
    axs.set_ylabel('Energy (eV)')
    axs.legend()
    plt.savefig('zbl.eps', format='eps')
    

  # Lennard Jones Potential
  # p[0] = e
  # p[1] = rm
  @staticmethod
  def lennard_jones(r, p):
    return p[0] * ((p[1] / r)**12 - 2 * (p[1]/r)**6)

  @staticmethod
  def lennard_jones_a(r, p):
    return p[0] * ((p[1] / r)**12)

  @staticmethod
  def lennard_jones_b(r, p):
    return p[0] * (- 2 * (p[1]/r)**6)
    
    
  # Morse Potential
  # p[0] = d
  # p[1] = a
  # p[2] = re
  @staticmethod
  def morse(r, p):
    return p[0] * (numpy.exp(-2 * p[1] * (r - p[2])) - 2 * numpy.exp (-p[1]*(r - p[2])))

  @staticmethod
  def morse_a(r, p):
    return p[0] * (numpy.exp(-2 * p[1] * (r - p[2])))

  @staticmethod
  def morse_b(r, p):
    return p[0] * ( - 2 * numpy.exp (-p[1]*(r - p[2])))

    
  # Buckingham Potential
  # p[0] = A
  # p[1] = B
  # p[2] = C
  @staticmethod
  def buckingham(r, p):
    return p[0] * numpy.exp(-1 * p[1] * r) - p[2] / r**6
  @staticmethod
  def buckingham_a(r, p):
    return p[0] * numpy.exp(-1 * p[1] * r)
  @staticmethod
  def buckingham_b(r, p):
    return (- p[2] / r**6)


  # Buckingham Potential
  # p[0] = e
  # p[1] = rm
  # p[2] = alpha
  @staticmethod
  def buckingham_r(r, p):
    a = (6.0*p[0]*numpy.exp(p[2]))
    b = p[2] / p[1]
    c = ((p[0] * p[2]) / (p[2]-6)) *p[1]**6
    return a * numpy.exp(-1 * b * r) - c / r**6


  # ZBL
  # p[0] = Z1
  # p[1] = Z2
  @staticmethod
  def zbl(r, p):
    e0 = 8.8541878128e-12
    pi = 3.141592654
    a0 = 0.529
    e = 1.602176634e-19
    a = (0.8854 * a0) / (p[0]**0.23 + p[1]**0.23)
    y = (1/(4 * pi * e0 *(1.0e-30)))*((p[0]*p[1]*e**2)/r) * pot_plot.zbl_screening(r/a)
    print(y)
    return y

  def zbl_screening(x):
    return 0.181 * numpy.exp(-3.2 * x) + 0.5099 * numpy.exp(-0.9423 * x) + 0.2802 * numpy.exp(-0.4029 * x) + 0.02817 * numpy.exp(-0.2016 * x)



  def grad(f, r, p):
    h = 1.0e-8
    xa = f(r, p)
    xb = f(r+h, p)
    return (xb - xa) / h



pot_plot.run()

