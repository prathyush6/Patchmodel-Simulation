import sys

R = []
T = []
N = []

fr = open('sim_output.txt','w')


#set up all input data from the file (simulatedip.csv)
#======================================================
with open(sys.argv[1]) as fp:  
    lines = fp.readlines()
    
    l1 = lines[0].split(",")
    noRegions = int(l1[0])
    timePeriods = int(l1[1])
        
    for i in range(0, noRegions):
        R.append(i)
    for i in range(0, timePeriods):
        T.append(i)
    print("R: "+str(R))
    print("T: "+str(T))
    
    l2 = lines[1].strip("\n").split(",")
    k = 0

    N = []
    for i in range(0, noRegions):
        N.append(int(l2[i]))
        k = k+1

    l3 = lines[2].strip("\n").split(",")
    alpha = float(sys.argv[2])
    beta = float(sys.argv[3])
    gamma = float(sys.argv[4])
    print("alpha beta gamma "+str(alpha)+" "+str(beta)+" "+str(gamma))

    l4 = lines[3].strip("\n").split(",")
    I = []
    for i in range(0, noRegions):
        I.append([])
        I[i].append(int(l4[i]))
        for t in range(1, timePeriods):
            I[i].append(0)

    theta = []
    l6 = lines[4].strip("\n").split(",")
    k = 0
    for i in range(0, noRegions):
        theta.append([])
        for j in range(0, noRegions):
            theta[i].append(float(l6[k]))
            k = k+1

#intialize seed values for V, E, R, and S
#=======================================
E = []
R = []
S = []

for i in range(0, noRegions):
    E.append([])
    R.append([])
    S.append([])
    #V.append([])
    for t in range(0, timePeriods):
        E[i].append(0)
        R[i].append(0)
        S[i].append(0)


#initializing susceptibles as population - infected
for i in range(0, noRegions):
    S[i][0] = N[i] - I[i][0]

#Neff and Ieff Calculations
#=====================================
Neff = []
for i in range(0, noRegions):
    Neff.append(0)
    for j in range(0, noRegions):
        Neff[i] = Neff[i] + N[j] * theta[j][i]


Ieff = []
for i in range(0, noRegions):
    Ieff.append([])
    for t in range(0, timePeriods):
        Ieff[i].append(0)
        Ieff[i][t] = 0
        if t == 0:
           for j in range(0, noRegions):
               Ieff[i][0] = Ieff[i][0] + I[j][0] * theta[j][i]

print("Simulation Begins")

#equations for simulation rounds
#======================================
for i in range(0, noRegions):
    for t in range(1, timePeriods):
        R[i][t] = R[i][t-1] + gamma * I[i][t-1]
        I[i][t] = I[i][t-1] + alpha * E[i][t-1] - gamma * I[i][t-1]
    
for i in range(0, noRegions):
    for t in range(1, timePeriods):
        for j in range(0, noRegions):
            Ieff[i][t] = Ieff[i][t] + I[j][t] * theta[j][i]
    
for i in range(0, noRegions):
    for t in range(1, timePeriods):
        term = 0
        for j in range(0, noRegions):
            term = term + theta[i][j] * beta * (Ieff[j][t-1]/ Neff[j]) * S[i][t-1]
        E[i][t] = E[i][t-1] - alpha * E[i][t-1] + term
        S[i][t] = S[i][t-1] - int(0.1 * S[i][t-1]) - term  #replace 0.1*S[i][t-1] with V[i][t] when vaccination comes from input
    

for i in range(0, noRegions):
    for t in range(0, timePeriods):
        if(t == timePeriods - 1):
           fr.write(str(I[i][t])+"\n")
        else:
           fr.write(str(I[i][t])+",")

fr.close()
print("Simulation Ends")
	
