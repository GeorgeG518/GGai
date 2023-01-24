#!/bin/bash

# da clean rue teen
rm ./greedydata/greedy?;
rm ./greedydata/greedy??;
rm ./SAdata/sa?;
rm ./SAdata/sa??;

for dims in 1 2 3 5
    do
    for((x=0;x<100;x++))
        do 
        echo "./greedy.py ${x} ${dims} 5  >> ./greedydata/greedy${x}"; 
        echo "./greedy.py ${x} ${dims} 10 >> ./greedydata/greedy${x}"; 
        echo "./greedy.py ${x} ${dims} 50 >> ./greedydata/greedy${x}";
        echo "./greedy.py ${x} ${dims} 100 >> ./greedydata/greedy${x}";
        
        echo "./sa.py ${x} ${dims} 5  >> ./SAdata/sa${x}";
        echo "./sa.py ${x} ${dims} 10 >> ./SAdata/sa${x}";
        echo "./sa.py ${x} ${dims} 50 >> ./SAdata/sa${x}";
        echo "./sa.py ${x} ${dims} 100 >> ./SAdata/sa${x}";

    done;
done;
