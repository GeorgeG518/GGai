#!/bin/bash
rm ./iris/*.dat
rm ./cancer/*.dat

for i in 1 5 10 25 50 75 100 125 140 145 149 
do 
    for((x=0;x<100;x++))
    do
        echo "cat iris-data.txt | bash split.bash ${i} python id3.py >> ./iris/iris_${i}.dat";
    done;
done;

for i in 1 5 10 25 50 75 90 100 104
do 
    for((x=0;x<100;x++))
    do
        echo "cat cancer-data.txt | bash split.bash ${i} python id3.py >> ./cancer/cancer_${i}.dat";
    done;
done;