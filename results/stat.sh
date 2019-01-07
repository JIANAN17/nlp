for fn in "."/09**.txt
do
    #echo analysis $fn
    python stat.py $fn
done
