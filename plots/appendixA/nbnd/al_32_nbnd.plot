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
set terminal postscript eps monochrome enhanced blacktext  size 8,8
set output "al_32_nbnd.eps"
#
# Set multiple plot layout
#============================================
set multiplot layout 2,1 rowsfirst
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
#set xtics 1
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
set title "Al K-Point Energy Convergence"
set key on outside bmargin
set label 1 '' at graph 0.92,0.9 font ',8'
set xlabel "X-axis Label"
set ylabel "Y-axis Label"
set y2label "Y-axis Label"
set ytics nomirror tc lt 1
set y2tics nomirror tc lt 2
plot \
'al_32_nbnd.csv' using 1:2 with linespoints axes x1y1 title "Energy(Ry)", \
'al_32_nbnd.csv' using 1:3 with linespoints axes x1y2 title "Force (Ry/Au)"
#------------------
# Plot 2
#------------------
plot \
'al_32_nbnd.csv' using 1:4 with linespoints axes x1y1 title "Memory/MB", \
'al_32_nbnd.csv' using 1:5 with linespoints axes x1y2 title "Walltime/s"
#------------------
# Plot 3
#------------------
#------------------
# Plot 4
#------------------






#################################################################################
#################################################################################
