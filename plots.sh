#!/bin/bash

# F_FindPlots
# Runs through dir and sub dirs and runs gnuplot where it finds .plot files
function F_FindPlots {
  for item in *; do
    if [ "$item" == "SHARED" ]; then
      echo "Skip shared"
    else
      if [ -d "$item" ]; then
        (cd -- "$item" && F_FindPlots)
      fi
      extension=".plot"
      if [[ "$item" == *$extension ]]; then
        gnuplot $item
        echo $item
      fi
    fi
  done
}

# Make plots
#########################
F_FindPlots
