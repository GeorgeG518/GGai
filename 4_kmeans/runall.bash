#!/bin/bash
# da clean roo teen
rm ./iris/*.dat
rm ./cancer/*.dat
rm temp.*.*

for num_cluster in {1..140}; do 
    for i in {0..100}; do 
        echo "cat iris-data.txt | ./split.bash 10 python kmeans.py $num_cluster >> ./iris/iris_${num_cluster}.dat";
    done ;
done ;

for num_cluster in {1..95}; do 
    for i in {0..100}; do 
        echo "cat cancer-data.txt | ./split.bash 10 python kmeans.py $num_cluster >> ./cancer/cancer_${num_cluster}.dat";
    done ;
done ;