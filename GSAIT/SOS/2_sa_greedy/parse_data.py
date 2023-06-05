import numpy as np
import math
arr_of_ties = np.zeros((4,4))
arrCounts = np.zeros((4,4))
TOL = 1e-8
for i in range(100):
    #for i in range(100):
    filein1 = open("./greedydata/greedy"+str(i),'r')
    filein2 = open("./SAdata/sa"+str(i), 'r')

    # dim 1
    gr_data1_5 =float( filein1.readline().split()[-1])
    sa_data1_5=float(filein2.readline().split()[-1])

    if (math.isclose(sa_data1_5,gr_data1_5, abs_tol = TOL)):
        arr_of_ties[0][0]+=1
    elif sa_data1_5 > gr_data1_5:
        arrCounts[0][0]+=1

    gr_data1_10 = float(filein1.readline().split()[-1])
    sa_data1_10=float(filein2.readline().split()[-1])
    
    if (math.isclose(sa_data1_10,gr_data1_10, abs_tol = TOL)):
        arr_of_ties[0][1]+=1
    elif sa_data1_10 > gr_data1_10:
        arrCounts[0][1]+=1


    gr_data1_50 = float(filein1.readline().split()[-1])
    sa_data1_50=float(filein2.readline().split()[-1])

    if (math.isclose(sa_data1_50,gr_data1_50, rel_tol=1e-8,abs_tol = TOL)):
        arr_of_ties[0][2]+=1
    elif sa_data1_50 > gr_data1_50 :
        arrCounts[0][2]+=1


    gr_data1_100 = float(filein1.readline().split()[-1])
    sa_data1_100=float(filein2.readline().split()[-1])

    if (math.isclose(sa_data1_100,gr_data1_100, rel_tol=1e-8,abs_tol = TOL)):
        arr_of_ties[0][3]+=1
    elif sa_data1_100  > gr_data1_100:
        arrCounts[0][3]+=1


    # dim 2
    gr_data2_5 = float(filein1.readline().split()[-1])
    sa_data2_5=float(filein2.readline().split()[-1])

    if (math.isclose(sa_data2_5,gr_data2_5, rel_tol=1e-8,abs_tol = TOL)):
        arr_of_ties[1][0]+=1
    elif sa_data2_5 > gr_data2_5 :
        arrCounts[1][0]+=1

    gr_data2_10 = float(filein1.readline().split()[-1])
    sa_data2_10=float(filein2.readline().split()[-1])
    if (math.isclose(sa_data2_10,gr_data2_10, rel_tol=1e-8,abs_tol = TOL)):
        arr_of_ties[1][1]+=1
    elif sa_data2_10 >gr_data2_10:
        arrCounts[1][1]+=1

    gr_data2_50 = float(filein1.readline().split()[-1])
    sa_data2_50=float(filein2.readline().split()[-1])
    if (math.isclose(sa_data2_50,gr_data2_50, abs_tol = TOL)):
        arr_of_ties[1][2]+=1   
    elif sa_data2_50 > gr_data2_50:
        arrCounts[1][2]+=1

    gr_data2_100 = float(filein1.readline().split()[-1])
    sa_data2_100=float(filein2.readline().split()[-1])
    if (math.isclose(sa_data2_100,gr_data2_100, abs_tol = TOL)):
        arr_of_ties[1][3]+=1   
    elif sa_data2_100  > gr_data2_100 :
        arrCounts[1][3]+=1


    #dim 3
    gr_data3_5 = float(filein1.readline().split()[-1])
    sa_data3_5=float(filein2.readline().split()[-1])
    if (math.isclose(sa_data3_5,gr_data3_5, abs_tol = TOL)):
        arr_of_ties[2][0]+=1   
    elif sa_data3_5  > gr_data3_5:
        arrCounts[2][0]+=1

    gr_data3_10 = float(filein1.readline().split()[-1])
    sa_data3_10=float(filein2.readline().split()[-1])
    if (math.isclose(sa_data3_10,gr_data3_10, abs_tol = TOL)):
        arr_of_ties[2][1]+=1
    elif sa_data3_10 > gr_data3_10:
        arrCounts[2][1]+=1

    gr_data3_50 = float(filein1.readline().split()[-1])
    sa_data3_50=float(filein2.readline().split()[-1])
    if(math.isclose(sa_data3_50,gr_data3_50, abs_tol = TOL)):
        arr_of_ties[2][2]+=1
    elif sa_data3_50 > gr_data3_50:
        arrCounts[2][2]+=1

    gr_data3_100 = float(filein1.readline().split()[-1])
    sa_data3_100=float(filein2.readline().split()[-1])
    if(math.isclose(sa_data3_100,gr_data3_100, abs_tol = TOL)):
        arr_of_ties[2][3]+=1   
    elif sa_data3_100 > gr_data3_100:
        arrCounts[2][3]+=1


    #dim 4
    gr_data5_5 = float(filein1.readline().split()[-1])
    sa_data5_5=float(filein2.readline().split()[-1])
    if(math.isclose(sa_data5_5,gr_data5_5, abs_tol = TOL)):
        arr_of_ties[3][0]+=1   
    elif sa_data5_5 > gr_data5_5:
        arrCounts[3][0]+=1


    gr_data5_10 = float(filein1.readline().split()[-1])
    sa_data5_10=float(filein2.readline().split()[-1])
    if(math.isclose(sa_data5_10,gr_data5_10, abs_tol = TOL)):
        arr_of_ties[3][1]+=1   
    elif sa_data5_10 > gr_data5_10:
        arrCounts[3][1]+=1

    gr_data5_50 = float(filein1.readline().split()[-1])
    sa_data5_50=float(filein2.readline().split()[-1])
    if(math.isclose(sa_data5_50,gr_data5_50, abs_tol = TOL)):
        arr_of_ties[3][2]+=1   
    elif sa_data5_50 > gr_data5_50:
        arrCounts[3][2]+=1


    gr_data5_100 = float(filein1.readline().split()[-1])
    sa_data5_100=float(filein2.readline().split()[-1])
    if(math.isclose(sa_data5_100,gr_data5_100, abs_tol = TOL)):
        arr_of_ties[3][3]+=1   
    elif sa_data5_100 > gr_data5_100:
        arrCounts[3][3]+=1

    filein1.close()
    filein2.close()
print("SA > Greedy")
print(arrCounts)
print()

print("SA==GREEDY")
print(arr_of_ties)
print(100-arrCounts-arr_of_ties)