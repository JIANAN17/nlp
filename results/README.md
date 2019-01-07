##整体结果
```
_0.txt - _7.txt 
```
##run.sh 提取每天结果
```
#把_0.txt -- _7.txt合并到all.txt
rm -f all.txt
for i in `seq 0 7` 
do
    cat _$i.txt >> all.txt
done

#从all.txt中，分别提取每天的区间
#如0901这一天，是第2行到第5行
#...
sed -n '2, 5p' all.txt > 0901.txt
sed -n '6,5437p'  all.txt > 0902.txt
sed -n '5438,11584p'  all.txt > 0903.txt
sed -n '11585, 12276p'  all.txt > 0904.txt
sed -n '12277, 12702p'  all.txt > 0905.txt
sed -n '12703,15684p'  all.txt > 0906.txt
sed -n '15685,16355p'  all.txt > 0907.txt
sed -n '16356, 16498p'  all.txt > 0908.txt
sed -n '16499, 16658p'  all.txt > 0909.txt
sed -n '16659, 16800p'  all.txt > 0910.txt
sed -n '16801, 16854p'  all.txt > 0911.txt
wc -l 09**.txt
```

##stat.sh依次进行情感分析

```
#从0901.txt 到 0911.txt
#依次执行python stat.py 090N.txt
#stat.py每次接受一个txt进行分析
for fn in "."/09**.txt
do
    python stat.py $fn
done
```

##逐天分析结果如下

```
./0901.txt
	+, -, 0
	2 0 2
./0902.txt
	+, -, 0
	4239 1070 123
./0903.txt
	+, -, 0
	5864 283 0
./0904.txt
	+, -, 0
	665 27 0
./0905.txt
	+, -, 0
	403 23 0
./0906.txt
	+, -, 0
	2958 24 0
./0907.txt
	+, -, 0
	636 35 0
./0908.txt
	+, -, 0
	132 11 0
./0909.txt
	+, -, 0
	157 3 0
./0910.txt
	+, -, 0
	141 1 0
./0911.txt
	+, -, 0
	51 3 0
```
