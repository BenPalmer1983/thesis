#!/bin/bash
#================================================================================#

# Start time
startTime=`date +%s`

#################################################################################
#
# Functions
#########################
#
#
#
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

# Vars
#########################
output="thesis.pdf"


#################################################################################
#
# Cleanup
#########################
#rm *.aux
#rm *.xml
#rm *.toc
#rm *blx.bib
#rm *.blg
#rm *.log
#rm chapter1/*.aux
#rm bibliography/*.aux
#
#
# Symlink to SHARED
#########################
#rm SHARED
if [ ! \( -e "SHARED" \) ]; then
  echo "Make symlink"
  ln -s /cloud/latex/SHARED SHARED
fi
#
# Make plots
F_FindPlots
sleep 1.0
# Make bib file
SHARED/bib/prep.sh
# Make buildfile dir
mkdir -p buildfiles
# Make junk dir
mkdir -p buildfiles/junk
# Move junk
mv *.pdf buildfiles/junk
# Build first time
pdflatex --file-line-error main.tex
# Make bibliography
#bibtex8 main > buildfiles/bib_output.log
#makeglossaries main > buildfiles/glossary_output.log
bibtex8 main 
makeglossaries main 
# Build with bibliography
#pdflatex main.tex > buildfiles/finalpass.log
pdflatex --file-line-error main.tex 
pdflatex --file-line-error main.tex 
# First argument is used as output file name
if [[ "${args[0]}" == "" ]]; then  
  echo ${args[0]}
else
  echo ${args[0]}
  output=${args[0]}".pdf"
fi
# Rename
mv main.pdf $output
# Move build files
mv main.aux buildfiles/main.aux
mv main.bbl buildfiles/main.bbl
mv main.blg buildfiles/main.blg
mv main.lof buildfiles/main.lof
mv main.log buildfiles/main.log
mv main.run.xml buildfiles/main.run.xml
mv main.toc buildfiles/main.toc
mv main-blx.bib buildfiles/main-blx.bib
# Copy PDF
#cp $output ../aaa_all/$output
#cp $output ../../aaa_all/$output

#if [ -d "../aaa_all" ]; then
#  cp $output ../aaa_all/$output
#fi
#if [ -d "../../aaa_all" ]; then
#  cp $output ../../aaa_all/$output
#fi
if [ -d "/cloud/latex/aaa_all" ]; then
  cp $output /cloud/latex/aaa_all/$output
fi

#################################################################################

# End time
endTime=`date +%s`

runtime=$((endTime-startTime))

python3 share/python/wordcount.py main.tex

pdftotext $output - | wc -w

echo "Run time:    "$runtime


#================================================================================#
