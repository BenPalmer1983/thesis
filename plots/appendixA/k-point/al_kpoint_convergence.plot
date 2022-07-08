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
set terminal postscript eps monochrome enhanced blacktext  size 6.6,3.6
set output "al_kpoint_convergence.eps"
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
set xtics 1
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
'al_kpoint_convergence.csv' using 1:2 with linespoints axes x1y1 title "0.05 MV smearing", \
'al_kpoint_convergence.csv' using 4:5 with linespoints axes x1y1 title "0.08 MV smearing", \
'al_kpoint_convergence.csv' using 7:8 with linespoints axes x1y1 title "0.10 MV smearing", \
'al_kpoint_convergence.csv' using 10:11 with linespoints axes x1y1 title "0.12 MV smearing", \
'al_kpoint_convergence.csv' using 13:14 with linespoints axes x1y1 title "0.15 MV smearing"
#------------------
# Plot 2
#------------------
set title "Al K-Point Force Convergence"
set label 1 '' at graph 0.92,0.9 font ',8'
plot \
'al_kpoint_convergence_difference.csv' using 1:2 with linespoints axes x1y1 title "Change 0.05 MV smearing", \
'al_kpoint_convergence_difference.csv' using 4:5 with linespoints axes x1y1 title "Change 0.08 MV smearing", \
'al_kpoint_convergence_difference.csv' using 7:8 with linespoints axes x1y1 title "Change 0.10 MV smearing", \
'al_kpoint_convergence_difference.csv' using 10:11 with linespoints axes x1y1 title "Change 0.12 MV smearing", \
'al_kpoint_convergence_difference.csv' using 13:14 with linespoints axes x1y1 title "Change 0.15 MV smearing"
#------------------
# Plot 3
#------------------
set title "Al K-Point Energy Convergence (Difference)"
set label 1 '' at graph 0.92,0.9 font ',8'
plot \
'al_kpoint_convergence.csv' using 1:3 with linespoints axes x1y1 title "0.05 MV smearing", \
'al_kpoint_convergence.csv' using 4:6 with linespoints axes x1y1 title "0.08 MV smearing", \
'al_kpoint_convergence.csv' using 7:9 with linespoints axes x1y1 title "0.10 MV smearing", \
'al_kpoint_convergence.csv' using 10:12 with linespoints axes x1y1 title "0.12 MV smearing", \
'al_kpoint_convergence.csv' using 13:15 with linespoints axes x1y1 title "0.15 MV smearing"
#------------------
# Plot 4
#------------------
set title "Al K-Point Energy Convergence (Difference)"
set label 1 '' at graph 0.92,0.9 font ',8'
plot \
'al_kpoint_convergence_difference.csv' using 1:3 with linespoints axes x1y1 title "Change 0.05 MV smearing", \
'al_kpoint_convergence_difference.csv' using 4:6 with linespoints axes x1y1 title "Change 0.08 MV smearing", \
'al_kpoint_convergence_difference.csv' using 7:9 with linespoints axes x1y1 title "Change 0.10 MV smearing", \
'al_kpoint_convergence_difference.csv' using 10:12 with linespoints axes x1y1 title "Change 0.12 MV smearing", \
'al_kpoint_convergence_difference.csv' using 13:15 with linespoints axes x1y1 title "Change 0.15 MV smearing"







#################################################################################
#################################################################################
