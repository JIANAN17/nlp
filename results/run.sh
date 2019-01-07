rm -f all.txt
for i in `seq 0 7` 
do
    cat _$i.txt >> all.txt
done

#sed ,n '2, 5p' all.txt
#2       6,5437
#3       5438,11584
#4       11585 , 12276
#5       12277, 12702
#6       12703,15684
#7       15685,16355
#8       16356 , 16498
#9       16499 , 16658
#10      16659 , 16800
#11      16801 , 16854
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
