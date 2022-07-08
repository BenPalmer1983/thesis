set term epslatex monochrome
set output "pbspI=elec_demand.tex"
set grid xtics mxtics ytics mytics back
set datafile separator "	"
set title "Electricity Demand UK: 1956-2013"
set xlabel "Year"
set ylabel "Electricity in Millions of Tonnes of Oil Equivalent"
set key autotitle columnheader
plot 'elec_demand.csv' using 1:2 with lines, 'elec_demand.csv' using 1:3 with lines, 'elec_demand.csv' using 1:4 with lines, 'elec_demand.csv' using 1:5 with lines, 'elec_demand.csv' using 1:6 with lines, 'elec_demand.csv' using 1:7 with lines, 'elec_demand.csv' using 1:8 with lines, 'elec_demand.csv' using 1:9 with lines, 'elec_demand.csv' using 1:10 with lines

