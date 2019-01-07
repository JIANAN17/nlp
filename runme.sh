seg=2107
for i in `seq 0 7`
do
	let start=i*seg
	let end=start+seg
	python single.py  $start  $end   _$i.txt  >_$i.log 2>&1 && python beam.py &
    echo $!
done
