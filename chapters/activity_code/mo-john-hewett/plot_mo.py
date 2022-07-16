import matplotlib.pyplot as plt
import numpy

depth1 = [23.545,69.265,112.225,152.375,189.65,223.975,248.035,262.93,277.04,290.355,302.85,314.505]
activity = [863162.980944226,1069637.55228783,1013605.35657343,
            815529.560737969,606485.036061676,394024.009205905,123315.241813163,
            81148.6548341006,48298.6138319571,25641.308656807,12029.3355090429,
            4677.33046280323]

depth2 = [0,47.09,91.44,133.01,171.74,207.56,240.39,255.68,270.18,283.9,296.81,308.89,320.12]
energy = [13,12,11,10,9,8,7,6.5,6,5.5,5,4.5,4]


fig, ax1 = plt.subplots(figsize=(6,3.8))
plt.title("Tc96 Activity and Ion Energy vs Depth Into Target")


colour = 'tab:red'
ax1.set_xlabel('Depth (micrometers)')
ax1.set_ylabel('Tc96 Activity', color=colour)
ax1.plot(depth1, activity, label='TC-96 Activity', ls='none', marker="+", color=colour)
ax1.tick_params(axis='y', labelcolor=colour)


ax2 = ax1.twinx() 

colour = 'tab:blue'
ax2.set_ylabel('Proton Energy (MeV)', color=colour)
ax2.plot(depth2, energy, label='Proton energy', marker="")
ax2.tick_params(axis='y', labelcolor=colour)

fig.tight_layout()
fig.savefig("mo96_pn_tc96_activity_depth.eps", format='eps')
plt.close()
