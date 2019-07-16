mat = [[ 1, 2, 3, 4, 5],
       [ 6, 7, 8, 9,10],
       [11,12,13,14,15],
       [16,17,18,19,20],
       [21,22,23,24,25]]

columnend = len(mat[0])
rowend = len(mat)
cstart=0
rstart=0

while (rstart<rowend and cstart<columnend):
    for i in range (cstart,columnend):
        print(mat[rstart][i])
    rstart  =rstart+1

    for i in range (rstart,rowend):
        print(mat[i][columnend-1])
    columnend = columnend-1

    if rstart < rowend:
        for i in range (columnend-1,cstart-1,-1):
            print(mat[rowend-1][i])
            #if rstart<rowend:
        rowend = rowend-1

    if cstart < columnend:
        for i in range(rowend-1,rstart-1,-1):
            print(mat[i][cstart])
        cstart =cstart+1