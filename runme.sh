#python single.py 0 2107 scores.txt

seg=2107
for i in `seq 0 7`
do
	let start=i*seg
	let end=start+seg
	python single.py  $start  $end   $i.txt &
done
