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
set terminal postscript eps monochrome enhanced blacktext size 12.8,7.2 font 'Helvetica,28'
set output "po218_po218.eps"
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
#
#
#------------------------------------
# Set Encoding
#------------------------------------
#
set encoding iso_8859_1
#
#
#------------------------------------
# Set Title
#------------------------------------
#
set label 1 '' at graph 0.92,0.9 font ',8'
#
#
#------------------------------------
# Set Key
#------------------------------------
#
#set nokey
set key top right
#
#
#------------------------------------
# Set Axes
#------------------------------------
#
### X Axis ###
set xlabel "Time (seconds)"
set format x "%g"
#
### Y Axis ###
set ylabel "Po-218 (mircograms)"
set logscale y 10
set format y "%g"
set ytics nomirror tc lt 1
set yrange [1E-6:1E9]
#
### Y2 Axis ###
#set y2label "Y-axis Label"
#set y2tics nomirror tc lt 2
#
#
#------------------------------------
# Datafile + Separator
#------------------------------------
set datafile separator ","
plot \
'po-218_comparisons.csv' using 1:2 with line axes x1y1 title "Po-218 (Analytic)", \
'po-218_comparisons.csv' using 1:10 with line axes x1y1 title "Po-218 (Gaver-Stehfest)"
# 




#
#
#plot \
#'po-218_comparisons.csv' using 1:2 with line axes x1y1 title "Po-218", \
#'po-218_comparisons.csv' using 1:3 with line axes x1y1 title "Pb-214", \
#'po-218_comparisons.csv' using 1:4 with line axes x1y1 title "Bi-214", \
#'po-218_comparisons.csv' using 1:5 with line axes x1y1 title "Po-214", \
#'po-218_comparisons.csv' using 1:6 with line axes x1y1 title "Pb-210", \
#'po-218_comparisons.csv' using 1:7 with line axes x1y1 title "Bi-210", \
#'po-218_comparisons.csv' using 1:8 with line axes x1y1 title "Tl-206", \
#'po-218_comparisons.csv' using 1:9 with line axes x1y1 title "Pb-206", \
#'po-218_comparisons.csv' using 1:10 with line axes x1y1 title "Po-218 (GS)", \
#'po-218_comparisons.csv' using 1:11 with line axes x1y1 title "Pb-214 (GS)", \
#'po-218_comparisons.csv' using 1:12 with line axes x1y1 title "Bi-214 (GS)", \
#'po-218_comparisons.csv' using 1:13 with line axes x1y1 title "Po-214 (GS)", \
#'po-218_comparisons.csv' using 1:14 with line axes x1y1 title "Pb-210 (GS)", \
#'po-218_comparisons.csv' using 1:15 with line axes x1y1 title "Bi-210 (GS)", \
#'po-218_comparisons.csv' using 1:16 with line axes x1y1 title "Tl-206 (GS)", \
#'po-218_comparisons.csv' using 1:17 with line axes x1y1 title "Pb-206 (GS)"






#################################################################################
#################################################################################
