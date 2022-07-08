#!/bin/bash
rm *.aux
rm *.xml
rm *.toc
rm *blx.bib
rm *.blg
rm *.log
pdflatex notes.tex
bibtex8 notes
pdflatex notes.tex


