import numpy
import matplotlib.pyplot as plt

peaks1_e = [204.117,314.27,316.5,434.71,460.04,535.78,568.88,582.082,765.789,778.22,786.198,812.54,835.149,849.86,934.49,947.67,1073.71,1091.3,1126.85,1200.17]
peaks1_a = [169831.136463892,257015.170667166,147467.96320696,79000.6945751574,45293.7315564236,43187.0463677527,96907.5186788597,80448.9988706477,4574315.31666401,10533425.9433543,23249.871035527,8658474.01368385,71498.9433589587,10301692.6843539,31582.510521147,95145.9536117795,182515.278647478,115867.685376897,1601078.63163646,38973.675990411]

peaks2_e = [778,813,850,1127]
peaks2_a = [4.74e6,4.15e6,4.93e6,7.66e5]

peaks3_e = [763,776,810,847,1123]
peaks3_a = [511811,1355491,1154666,1385648,210272]

plt.clf()
plt.figure(figsize=(6,4))    
plt.title('Gamma Line Comparison')
plt.xlabel('Energy (keV)')
plt.ylabel('Activity (Bq)')
plt.xlim(0,1180)

plt.stem(peaks1_e, peaks1_a, 'b', markerfmt='bo', label="Calculated")
plt.stem(peaks2_e, peaks2_a, 'g', markerfmt='go', label="Estimate")
plt.stem(peaks3_e, peaks3_a, 'r', markerfmt='ro', label="Experimental")
plt.legend()

plt.savefig('gammas.eps', format='eps', transparent=False)
plt.close('all') 
