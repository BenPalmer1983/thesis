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
# set terminal postscript eps monochrome enhanced blacktext  size 12.8,7.2
set terminal postscript eps monochrome enhanced blacktext  size 12.8,7.2 font 'Helvetica,32'
set output "fission_spectra.eps"
#
# Set multiple plot layout
#============================================
set multiplot layout 1,1 rowsfirst
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
#
# Plots
#============================================
#
# Notes
# with points pt 13 ps 1.5
# with lines
#
#============================================
# Plot 1
#============================================
#
#
set encoding iso_8859_1
#
#------------------------------------
# Set Title
#------------------------------------
#
#set title "13MeV Protons in Fe"
set label 1 '' at graph 0.92,0.9 font ',8'
#
#------------------------------------
# Set Axes
#------------------------------------
#
set xlabel "Energy (MeV)"
set ylabel "n(E)"
#set y2label "Y-axis Label"
set ytics nomirror tc lt 1
#set y2tics nomirror tc lt 2
#------------------------------------
# Datafile + Separator
#------------------------------------
set datafile separator ","
plot \
'fission_spectra.csv' using 1:2 with lines axes x1y1 title "Fission Spectrum thermal induced fission"
# 







#################################################################################
#################################################################################
