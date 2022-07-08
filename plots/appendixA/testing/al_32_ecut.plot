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
set output "al_32_ecut.eps"
#
# Set multiple plot layout
#============================================
set multiplot layout 2,1 rowsfirst
#
# Plot title
#============================================
#set title "Title"
#
# Grid settings
#============================================
set grid xtics mxtics ytics mytics back
#
# Axes
#============================================
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
#set title "Al K-Point Energy Convergence"
#set key on outside bmargin
#set key off
set key on 
set label 1 '' at graph 0.92,0.9 font ',8'
#------------------
# X Axis
#------------------
set xlabel "Ecutwfc/Ry"
set x2label "Ecutrho/Ry"
set xtics nomirror tc lt 1
set x2tics nomirror tc lt 1
set autoscale xfix
set autoscale x2fix
#------------------
# Y Axis
#------------------
set ylabel "Energy (Ry)"
set y2label "Force (Ry/Au)"
set ytics nomirror tc lt 1
set y2tics nomirror tc lt 2
plot \
'al.32.ecut.csv' using 1:3 with linespoints axes x1y1 title "Energy(Ry)", \
'al.32.ecut.csv' using 1:4 with linespoints axes x1y2 title "Force (Ry/Au)", \
'al.32.ecut.csv' using 2:3 with linespoints axes x2y1 title ""
#------------------
# Plot 2
#------------------
set key on
set ylabel "Memory (MB)"
set y2label "Walltime (s)"
plot \
'al.32.ecut.csv' using 1:5 with linespoints axes x1y1 title "Memory (MB)", \
'al.32.ecut.csv' using 1:6 with linespoints axes x1y2 title "Walltime (s)", \
'al.32.ecut.csv' using 2:5 with linespoints axes x2y1 title ""
#------------------
# Plot 3
#------------------
#------------------
# Plot 4
#------------------



#set autoscale xfix
#set autoscale x2fix



#################################################################################
#################################################################################
