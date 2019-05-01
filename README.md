# Patchmodel-Simulation

The simulation has two steps:

Step 1. Creation of an input file for the simulation. For this we use the 'ThetaGenerator.py' code as following:

$>>$ python ThetaGenerator.py R T L b

where, 

R: Number of regions

T: Number of time periods (weeks/days)

L: not relevant for the simulation (can be provided a value like 20 indicating number of power of base 2 in which the integers are to 
represented)

b: not relevant for the simulation (can be provided a value 2 indicating integers will be represented by base 2)

Output file: simulatedip.csv

Line 1: R, T, L, b

Line 2: N[0],..., N[R-1]        (#N[i] corresponds to population in each region i.)

Line 3: Seed[0],..., Seed[R-1]   (#Seed infected in each region at time step 0.)

Line 4: Theta[0][0],..., Theta[R-1][R-1] (#Theta matrix with values Theta[i][j] for each pair of region i,j.)

Line 5: B[0], ..., B[T-1]  (Budget B[t] at time t.)

Line 6: ub (upper bound on the total number of infected.)

Step 2. Use the outputfile generated in the first step as input for the simulation code 'Simulate.py':

$>>$ python Simulate.py simulatedip.csv alpha beta gamma

Output file:

Line 1: I[0][0], ..., I[0][T-1]

Line 2: I[[1][0], ..., I[1][T-1]

.

.

.

Line R-1: I[R-1][0], ..., I[R-1][T-1]

These are the simulated values generated for number of infected in each region for all time steps.
