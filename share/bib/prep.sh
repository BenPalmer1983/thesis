cd SHARED/bib
pwd

echo "" > bibliography.bib

cmd="cat "
for file in *.bib; do 
  if [ $file != "bibliography.bib" ]; then
    echo $file
    cmd=$cmd" "$file    
  fi
done

cmd=$cmd" > bibliography.bib"
echo $cmd
eval $cmd
echo "bib created"

cd ../../
