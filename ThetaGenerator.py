import sys
import random

theta = []

R = int(sys.argv[1])
T = int(sys.argv[2])
L = int(sys.argv[3])
b = int(sys.argv[4])
print(R,T)


N = []
#population of each county randomly assigned a value in range [100000, 1000000]
for i in range(0, R):
    x = random.randint(100000,1000000)
    N.append(x)

Seed = []
#each county is randomly picked with probability 0.1 to have seed infected. if picked a random
#value is assigned to the county as seed infected
for i in range(0, R):
    x = 0
    toss = random.random()
    if(toss > 0.95):
       x = int(0.001 * N[i])
    Seed.append(x)

theta = []
i = 0
fr = open('theta_matrix.csv', 'r')
lines = fr.readlines()

for line in lines:
    theta.append([])
    cols = line.strip().split(",")
    for j in range(0, len(cols)):
        val = cols[j]
        theta[i].append(val)
        print(i,j)
    i += 1

fp = open('simulatedip.csv','w')
fp.write(str(R)+","+str(T)+","+str(L)+","+str(b)+"\n")

for i in range(0,R):
    val = str(N[i])
    if(i == R-1):
       fp.write(val)
    else:
       fp.write(val+",")
fp.write("\n")

fp = open('simulatedip.csv','w') 
fp.write(str(R)+","+str(T)+","+str(L)+","+str(b)+"\n")

for i in range(0,R):
    val = str(N[i])
    if(i == R-1):
       fp.write(val)
    else:
       fp.write(val+",")
fp.write("\n")

for i in range(0,R):
    val = str(Seed[i])
    if(i == R-1):
      fp.write(val)
    else:
      fp.write(val+",")
fp.write("\n")


for i in range(0,R):
    for j in range(0,R):
        val = str(theta[i][j])
        if i==R-1 and j == R-1:
           fp.write(val)
        else:
           fp.write(val+",")
fp.write("\n")

#Budget values for each region: can be automated
for i in range(0,T):
    if(i == T-1):
      fp.write("1000")
    else:
      fp.write("1000,")
fp.write("\n")
fp.write("5000000\n")
