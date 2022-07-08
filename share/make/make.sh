#!/bin/bash
#================================================================================#

# Start time
startTime=`date +%s`

# Vars
#########################
output="practical_maths.pdf"

# Symlink to SHARED
#########################
if [ ! \( -e "SHARED" \) ]; then
  echo "Make symlink"
  ln -s /cloud/latex/SHARED SHARED
fi

# Include functions file
#########################
source "SHARED/make/make.inc.sh"

# End time
endTime=`date +%s`

runtime=$((endTime-startTime))
echo "Run time:    "$runtime


#================================================================================#
