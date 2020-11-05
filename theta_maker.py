fp = open('merged_aggflow_0.csv', 'r')

lines = fp.readlines()

count = 0
regions = set([])
R = {}
E = {}
theta = []
for line in lines:
    cols = line.strip().split(" ")
    if cols[2] == "0":
        #print(count)
        if cols[0] not in regions:
            R[count] = cols[0]
            count += 1
            regions.add(cols[0])
        if cols[1] not in regions:
            R[count] = cols[1]
            count += 1
            regions.add(cols[1])
        edge1 = cols[0]+","+cols[1]
        edge2 = cols[1]+","+cols[0]
        #print(edge1, edge2)
        E[edge1] = cols[3]
        E[edge2] = cols[3]
        #print(len(E))
print(len(R))
print(count)
print(len(E))
for i in range(0, len(R)):
    theta.append([])
    for j in range(0, len(R)):
        edge = R[i]+","+R[j]
        if edge in E:
            val = E[edge]
            #print(val)
            theta[i].append(val)
            #print(i,j, theta[i][j])
        else:
            theta[i].append(0)

fp.close()
fw = open('theta_matrix.csv', 'w')
for i in range(0, len(R)):
    row = ""
    for j in range(0, len(R)):
        if j == len(R)-1:
            row += str(theta[i][j])
        else:
            row += str(theta[i][j])+","
    fw.write(row+"\n")
fw.close()
        


