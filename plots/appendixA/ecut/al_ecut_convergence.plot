#################################################################################
# Gnuplot
#
#################################################################################
# Output
#============================================
# 1. EspLaTeX monochrome
# set terminal epslatex monochrome
# set output "plot.tex"
# 2. png
# set terminal pngcairo size 1280,600 enhanced font 'Verdana,10'
# set output "plot.png"
# 3. ps - colour
# set terminal postscript eps enhanced color size 8,6 font 'Helvetica,20' linewidth 2
# set output "plot.eps"
# 4. ps - monochrome
# set terminal postscript eps monochrome enhanced blacktext  size 8,6
# set output "plot.eps"
set terminal postscript eps monochrome enhanced blacktext  size 6.6,3.6
set output "al_ecut_convergence.eps"
#
# Set multiple plot layout
#============================================
set multiplot layout 2,2 rowsfirst
#
# Plot title
#============================================
set title "Title"
#
# Grid settings
#============================================
set grid xtics mxtics ytics mytics back
#
# Axes
#============================================
set xlabel "X-axis Label"
set ylabel "Y-axis Label"
set ytics nomirror tc lt 1
set y2tics nomirror tc lt 2
#
# Data file
#============================================
set datafile separator ","
#
# Plot
#============================================
#------------------
# Plot 1
#------------------
set title "Al Ecutwfc Energy Convergence"
set label 1 '' at graph 0.92,0.9 font ',8'
set xlabel "Ecutwfc (Ry)"
set ylabel "Energy/Atom (eV)"
set y2label "Energy Difference/Atom (eV)"
set ytics nomirror tc lt 1
set y2tics nomirror tc lt 2
plot \
'al_ecut_convergence.csv' using 9:10 with linespoints axes x1y1 title "Energy per Atom (eV)", \
'al_ecut_convergence.csv' using 13:14 with linespoints axes x1y2 title "Energy difference per Atom (eV)"
#------------------
# Plot 2
#------------------
set title "Al Ecutwfc Force Convergence"
set label 1 '' at graph 0.92,0.9 font ',8'
set xlabel "Ecutwfc (Ry)"
set ylabel "Force/Atom (Ry/Bohr)"
set y2label "Force Difference/Atom (Ry/Bohr)"
set ytics nomirror tc lt 1
set y2tics nomirror tc lt 2
plot \
'al_ecut_convergence.csv' using 11:12 with linespoints axes x1y1 title "Total Force (Ry/au)", \
'al_ecut_convergence.csv' using 15:16 with linespoints axes x1y2 title "Force Difference (Ry/au)"
#------------------
# Plot 3
#------------------
set title "Al Ecutrho Energy Convergence"
set label 1 '' at graph 0.92,0.9 font ',8'
set xlabel "Ecutwfc (Ry)"
set ylabel "Energy/Atom (eV)"
set y2label "Energy Difference/Atom (eV)"
plot \
'al_ecut_convergence.csv' using 1:2 with linespoints axes x1y1 title "Energy per Atom (eV)", \
'al_ecut_convergence.csv' using 5:6 with linespoints axes x1y2 title "Energy difference per Atom (eV)"
#------------------
# Plot 4
#------------------
set title "Al Ecutrho Force Convergence"
set label 1 '' at graph 0.92,0.9 font ',8'
set xlabel "Ecutwfc (Ry)"
set ylabel "Force/Atom (Ry/Bohr)"
set y2label "Force Difference/Atom (Ry/Bohr)"
plot \
'al_ecut_convergence.csv' using 3:4 with linespoints axes x1y1 title "Total Force (Ry/au)", \
'al_ecut_convergence.csv' using 7:8 with linespoints axes x1y2 title "Force Difference (Ry/au)"







#################################################################################
#################################################################################
