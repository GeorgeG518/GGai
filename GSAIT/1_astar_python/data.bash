for i in 0 1 2 3
do
	echo "Heuristic $i"
	echo "V";cat ${i}.txt |grep "V="| cut -f2 -d"=" | ./stats.py 
	echo "N";cat ${i}.txt |grep "N="| cut -f2 -d"=" | ./stats.py 
	echo "d";cat ${i}.txt |grep "d="| cut -f2 -d"=" | ./stats.py 
	echo "b";cat ${i}.txt |grep "b="| cut -f2 -d"=" | ./stats.py 
	echo
done


