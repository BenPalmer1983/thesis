import matplotlib.pyplot as plt
import numpy


def make_array(text):
  d = []
  temp = text.split("\n")
  for line in temp:
    if(line.strip() != ""):
      f = line.split("\t")
      row = []
      for item in f:
        row.append(float(item)) 
      d.append(row)
  return numpy.asarray(d)

pd_iso = """4096	-0.011473680915908
4913	-0.006188141295024
5832	-0.00350781977186
6859	-0.002104800708592
8000	-0.001152674312052
9261	-0.000379870949334
10648	-0.000615657609082
12167	-0.000283814756276
13824	-0.000149118395353
15625	-0.00018721433584
17576	0"""

ru_iso = """4096	-0.029666669381043
4913	-0.016094854545992
5832	-0.008697983484877
6859	-0.004639269202995
8000	-0.002454603075723
9261	-0.001204239888477
10648	-0.00070477489784
12167	-0.000343815862871
13824	-0.00016612551196
15625	-4.31300470266969E-05
17576	0"""

fe_iso = """4096	-0.033069045031955
4913	-0.016973238086697
5832	-0.009514461122001
6859	-0.004679678110807
8000	-0.002158679253116
9261	-0.000873077320861
10648	-0.001506966558345
12167	-0.000583003945476
13824	-0.000482185760728
15625	-0.000237147229354
17576	0
"""


pd_iso = make_array(pd_iso)
ru_iso = make_array(ru_iso)
fe_iso = make_array(fe_iso)

print(pd_iso)
print(ru_iso)
print(fe_iso)

"""
'tab:blue'
'tab:orange'
'tab:green'
'tab:red'
'tab:purple'
'tab:brown'
'tab:pink'
'tab:gray'
'tab:olive'
'tab:cyan'
"""


"""
        'font_family': 'serif',
        'xtick_labelsize': 'x-small',
        'ytick_labelsize': 'x-small',
        
    ax1.rc('font', family=p['font_family'])
    ax1.rc('xtick', labelsize=p['xtick_labelsize'])
    ax1.rc('ytick', labelsize=p['ytick_labelsize'])
    ax1.grid(visible=True, which='major', axis='both')
"""

fig, ax1 = plt.subplots(figsize=(8,6), dpi=144)
plt.title("Isolated Atom Energies")
plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')
ax1.set_xlabel('Cell Volume (Bohr Cubed)')
ax1.set_ylabel('Energy (eV)')
ax1.plot(pd_iso[:,0], pd_iso[:,1], label='Pd', ls='solid', marker="+", color='tab:blue')
ax1.plot(ru_iso[:,0], ru_iso[:,1], label='Ru', ls='solid', marker="x", color='tab:orange')
ax1.plot(fe_iso[:,0], fe_iso[:,1], label='Fe', ls='solid', marker="o", color='tab:green')
ax1.grid(visible=True, which='major', axis='both')
fig.legend(loc='lower right', bbox_to_anchor=(0.9, 0.1))
fig.tight_layout()
fig.savefig("isolated_86.eps", format='eps')
plt.close()

fig, ax1 = plt.subplots(figsize=(6,3), dpi=144)
plt.title("Isolated Atom Energies")
plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')
ax1.set_xlabel('Cell Volume (Bohr Cubed)')
ax1.set_ylabel('Energy (eV)')
ax1.plot(pd_iso[:,0], pd_iso[:,1], label='Pd', ls='solid', marker="+", color='tab:blue')
ax1.plot(ru_iso[:,0], ru_iso[:,1], label='Ru', ls='solid', marker="x", color='tab:orange')
ax1.plot(fe_iso[:,0], fe_iso[:,1], label='Fe', ls='solid', marker="o", color='tab:green')
ax1.grid(visible=True, which='major', axis='both')
fig.legend(loc='lower right', bbox_to_anchor=(0.9, 0.2))
fig.tight_layout()
fig.savefig("isolated_63.eps", format='eps')
plt.close()

"""
fig, ax1 = plt.subplots(figsize=(8,6))
plt.title("Gaussian Heating")
colour = 'tab:green'
ax1.set_xlabel('Maximum perturbation (angs)')
ax1.set_ylabel('Energy (eV)', color=colour)
ax1.plot(he[:,0], he[:,1], label='Increase in energy', ls='none', marker="+", color=colour)
ax1.tick_params(axis='y', labelcolor=colour)


ax1.axhline(y=0.086, color='tab:purple', linestyle='-', label='1,000K')
ax1.axhline(y=0.172, color='tab:orange', linestyle='-', label='2,000K')
ax1.axhline(y=0.259, color='tab:red', linestyle='-', label='3,000K')

ax2 = ax1.twinx() 

colour = 'tab:blue'
ax2.set_ylabel('Total force (eV/angs)', color=colour)
ax2.plot(hf[:,0], hf[:,1], label='Increase in force', ls='none', marker="x")
ax2.tick_params(axis='y', labelcolor=colour)
fig.legend()
fig.tight_layout()
fig.savefig("alheat.eps", format='eps')
plt.close()
"""

