# Michael Villarreal
# COSC1336
# Fall 2023
# Prof: Onabajo
# File: warm4b.py
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
    # call function to load list X
    loaddata(infile,x)
    # call function to calculate and to populate list y
    sumx=calculate(x,y)
    # call function write all lists
    outdata(outfile,x,y)
    #write sum
    print('Sum  =   ',sumx)
    print(sum(y))
    print(y)
    input('press enter')
    #close files
    infile.close()
    outfile.close()

# function
def loaddata(file,a):
    # fil-infile a=list x
    # load data from the data file in to the list x
    k=0
    templist=file.readline().strip('\n').split(',')
    while (k<N):
        # load a
        a[k]=int(templist[k])
        #increment k
        k=k+1

def calculate(a,b):
    # a=x b=y
    k=0
    s=0
    while (k<N):
        b[k]=a[k]*M
        # sum all elements
        s+=b[k]
        #increment counter
        k+=1
    return(s)

def outdata(file,a,b):
    # file=outfile, a=list x, b=list y
    # local variable
    k=0
    while(k<N):
        print (a[k], b[k]) #print to screen
        #print to output file
        file.write(str(a[k])+' '+str(b[k])+'\n')
        k=k+1

# Execute main()
main()

