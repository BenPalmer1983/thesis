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
set output "sheng_eam_pd.eps"
#
# Set multiple plot layout
#============================================
set multiplot layout 1,1 rowsfirst
#
#
# Grid settings
#============================================
set grid xtics x2tics mxtics ytics y2tics mytics back
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
set title "Sheng Pd EAM Potential"
set key font ",9"
set label 1 '' at graph 0.92,0.9 font ',8'
set xlabel "Radius (Ang)"
set x2label "Electron Density"
set ylabel "V(r)   p(r)"
set y2label "F(p)"
set xtics nomirror tc lt 1
set x2tics nomirror tc lt 2
set ytics nomirror tc lt 1
set y2tics nomirror tc lt 2
set yrange [-2:30]
plot \
'sheng_eam_pd.csv' using 1:2 with lines axes x1y1 title "Pair function", \
'sheng_eam_pd.csv' using 3:4 with lines axes x1y1 title "Density function", \
'sheng_eam_pd.csv' using 5:6 with lines axes x2y2 title "Embedding functional"
#------------------
# Plot 2
#------------------







#################################################################################
#################################################################################
