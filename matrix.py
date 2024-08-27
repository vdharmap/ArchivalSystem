
# add to matrix 

M1 = [[1,2,4],[1,1,3],[2,23,4]]
M2 = [[2,5,7],[5,7,8],[5,5,5]]
M3 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(M1)):
    for j in range(len(M2)):
        M3[i][j] = M1[i][j] + M2[i][j]


for k in M3:
    print(k)