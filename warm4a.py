# Michael Villarreal
# COSC1336
# Fall 2023
# Prof: Onabajo
# File: warm4a.py
#
# Program to process a list
# it will load a list and populate another list
# It will print out both lists
# 

# GLOBAL VARIABLES
N=10    # rows needed
M=3

# Define main()
def main():
    # list declaration
    x=[0]*N     #[0] integer w/ N entries
    y=[0]*N
    # file declaration
    infile=open('warm4a.txt','r')
    outfile=open('warm4a.out','w')
    # variable declaration
    sumx=0
    # load data from the data file in to the list x
    k=0
    templist=infile.readline().strip('\n').split(',')
    while (k<N):
        # load x
        x[k]=int(templist[k])
        # populate y with x
        y[k]=int(x[k]*M)
        #add all the elements in list y
        sumx=sumx+y[k]
        #increment k
        k=k+1
    #write lists x & y
    k=0
    while (k<N):
        print(x[k], y[k])
        k=k+1
    #write sum
    print('Sum  =   ',sumx)
    #close files
    infile.close()
    outfile.close()

# Execute main()
main()

