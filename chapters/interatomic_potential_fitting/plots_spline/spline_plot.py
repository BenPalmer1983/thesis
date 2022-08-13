import numpy
import matplotlib.pyplot as plt

class spline_plot:

  def run():
    x = numpy.linspace(1.0, 7, 1001)
    y = spline_plot.slater(x, [5.0, 1.323])

    knots = 7
    i_nodes = 3
    
    x_min = 1.0
    x_max = 7.0

    xk = []
    xi = []
    for k in range(knots):
      xk.append(x_min + k * ((x_max - x_min) / (knots - 1)))
      if(k < (knots - 1)):
        for i in range(i_nodes):
          xi.append(xk[-1] + (i + 1) * (((x_max - x_min) / (knots - 1)) / (i_nodes + 1)))

    xk = numpy.asarray(xk)
    xi = numpy.asarray(xi)
    yk = spline_plot.slater(xk, [5.0, 1.323])
    yi = spline_plot.slater(xi, [5.0, 1.323])

    
    plt.clf()   
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='x-small')
    plt.rc('ytick', labelsize='x-small')
    fig, axs = plt.subplots(1, 1, figsize=(7,5))
    fig.tight_layout(pad=5.0)    
    fig.suptitle('Knot to Knot Spline')
    axs.plot(x, y, color='k', ls='dashed', label='potential')
    axs.scatter(xk, yk, color='red', marker='o', label='knots')
    axs.scatter(xi, yi, color='blue', marker='s', label='nodes for interpolation')
    axs.set_xlabel('Radius (angs)')
    axs.set_ylabel('Energy (eV)')
    axs.set_ylim(-1.0,9.0)
    axs.legend()
    plt.savefig('spline.eps', format='eps')
    

  @staticmethod
  def slater(r, p):
    return (p[0] * r**3 * numpy.exp(-p[1] * r))**2



spline_plot.run()

