#***************************************************************
#
#  Developer:         Michael Villarreal
#  Program #:         Lab 4
#  File Name:         Lab04.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          10-09-2023
#  Instructor:        Onabajo
#  Chapter:           <Chapter ?>
#
# Program to manipulate 1-dimensional list
# it will compute the mean, standard deviation, and standard scores

# Global Variables
N=20

#***************************************************************
#
#  Function:     developerInfo
#  Description:  Prints Programmer's information
#  Parameters:   None
#  Returns:      Output header
#
#**************************************************************
def developerInfo():
    print('Name:     Michael Villarreal')
    print('Course:   Programming Fundamentals I')
    print('Lab: 4')
    print()
    # End of the developerInfo function

#***************************************************************
#
#  Function:     spaces
#  Description:  Create a multi-line space to between input/output
#                to keep screen uncluttered
#  Parameters:   None
#  Returns:      n blank lines
#
#**************************************************************
def spaces(n):
    for x in range(n):
        print()


#***************************************************************
#
#  Function:     hold
#  Description:  Prompt to pause the screen until ready
#  Parameters:   None
#  Returns:      Nothing
#
#**************************************************************
def hold():
    input('Please enter any key to continue...')    

def loaddata(infile,x):
    pass

def deviation(dev,dev1,xbar):
    pass

# def sqrt():
#     pass

def standard():
    pass

def main():
    import math
    # list declaration
    x=dev=dev1=sd1=[0.0]*N
    # dev=[0.0]*N
    # dev1=[0.0]*N
    # sd1=[0.0]*N
    # file declaration
    infile=open('lab4.txt','r')
    outfile=open('lab4.out','w')
    # other variable declaration
    xbar=0.0    #mean
    std=0.0
    sumx=0.0
    dev2=0.0
    sd2=0.0
    # call functions
    sumx=loaddata(infile,x)
    # compute the mean
    xbar=float(sumx/N)
    dev2=deviation(dev,dev1,xbar)
    # compute standard deviation
    std=math.sqrt(dev2/n)
    # call standard
    sd2=standard(dev1,std)
    # call outdata(outfile,x,dev,dev1,sd1)
    # output the rest
    print('                   SUM :', sumx)
    print('               AVERAGE :', xbar)
    print('SUM OF STANDARAD SCORES: ',sd2)
    # print the rest to output file
    outfile.write('SUM :'+ str(sumx)+'\n')
    outfile.write('AVERAGE :'+ str(xbar)+'\n')
    outfile.write('SUM OF STANDARAD SCORES: '+str(sd2)+'\n')
    # hold
    hold()







main()
