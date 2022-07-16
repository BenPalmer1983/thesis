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
# set terminal pngcairo size 1024,768 enhanced font 'Verdana,10'
# set output "plot.png"
# 3. ps - colour
# set terminal postscript eps enhanced color size 8,6 font 'Helvetica,20' linewidth 2
# set output "plot.eps"
# 4. ps - monochrome
# set terminal postscript eps monochrome enhanced blacktext  size 8,6
# set output "plot.eps"
set terminal postscript eps monochrome enhanced blacktext  size 6.4,4.8
set output "po218.eps"
#
# Set multiple plot layout
#============================================
set multiplot layout 1,1 rowsfirst
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
#set y2tics nomirror tc lt 2
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
set title "Pd Ecutwfc Energy Convergence"
set label 1 '' at graph 0.92,0.9 font ',8'
set xlabel "Time (seconds)"
set ylabel "Po-218 (mircograms)"
#set y2label "Y-axis Label"
set ytics nomirror tc lt 1
#set y2tics nomirror tc lt 2
set logscale y 10
set yrange [0.001:1000000]
plot \
'po-218_decay.csv' using 1:2 with line axes x1y1 title "Analytic Decay", \
'po-218_decay.csv' using 3:4 with line axes x1y1 title "G-S m=7", \
'po-218_decay.csv' using 5:6 with line axes x1y1 title "G-S m=8"






#################################################################################
#################################################################################