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
set output "elec_demand.eps"
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
set title "Electricity Demand UK: 1956-2013"
set label 1 '' at graph 0.92,0.9 font ',8'
set xlabel "Year"
set ylabel "Electricity in Millions of Tonnes of Oil Equivalent"
#set y2label "Y-axis Label"
set ytics nomirror tc lt 1
#set y2tics nomirror tc lt 2
#set logscale y 10
#set yrange [0.001:1000000]
set key on
set key autotitle columnheader
set key box opaque
plot \
'elec_demand.csv' using 1:2 with lines, \
'elec_demand.csv' using 1:3 with lines, \
'elec_demand.csv' using 1:4 with lines, \
'elec_demand.csv' using 1:5 with lines, \
'elec_demand.csv' using 1:6 with lines, \
'elec_demand.csv' using 1:7 with lines, \
'elec_demand.csv' using 1:8 with lines, \
'elec_demand.csv' using 1:9 with lines, \
'elec_demand.csv' using 1:10 with lines







#################################################################################
#################################################################################

