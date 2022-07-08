#!/bin/bash
#================================================================================#

# Start time
startTime=`date +%s`

# Vars
#########################
output="thesis.pdf"



# Include functions file
#########################
source "share/make/make.inc.sh"

# End time
endTime=`date +%s`

runtime=$((endTime-startTime))

python3 share/python/wordcount.py main.tex

pdftotext $output - | wc -w

echo "Run time:    "$runtime


#================================================================================#
