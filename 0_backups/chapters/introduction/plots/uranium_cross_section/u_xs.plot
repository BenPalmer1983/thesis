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
# fontfile '/usr/share/texmf/fonts/type1/public/cm-super/sfrm1000.pfb'
set terminal postscript eps monochrome enhanced blacktext size 6.4,4.8 font 'sfrm1000,20'
set output "u_xs.eps"
#
# Set multiple plot layout
#============================================
set multiplot layout 2,1 rowsfirst
#
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
set datafile separator ";"
#
# Plot
#============================================
#------------------
# Plot 1
#------------------
set title "Uranium 235 Cross Section"
set key font ",9"
set label 1 '' at graph 0.92,0.9 font ',8'
set xlabel "Neutron Energy/eV"
set ylabel "Cross Section/Barns"
set xtics nomirror tc lt 1
set ytics nomirror tc lt 1
set logscale x 10
set logscale y 10
set format x "%2.0t{/Symbol \264}e{%L}"
plot \
'U235_cross_section.csv' using 1:2 with lines axes x1y1 title "U235"
#------------------
# Plot 2
#------------------
set title "Uranium 238 Cross Section"
plot \
'U238_cross_section.csv' using 1:2 with lines axes x1y1 title "U238"







#################################################################################
#################################################################################
