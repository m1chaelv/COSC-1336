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
    # fil-infile x=list s=sumx
    # load data from the data file in to the list x
    k=0
    templist=infile.readlines()
    for k in range(N):
        # load x
        x[k]=int(templist[k].strip('\n'))

def deviation(x,dev,dev1,xbar):
    # dev, dev1, xbar
    for k in range(N):
        dev[k]=xbar-x[k]
        dev1[k]=sqr(dev[k])

def sum_of(list):
    # given an array, return sum of all numbers
    # s=summary for list both int and float
    s=0
    for y in range(N):
        s+=list[y]
    if s%1 == 0:
        return(int(s))
    else:
        return(float(s))

def sqr(number):
    # accept a number and return it's square
    number*=number
    return(number)

def standard(dev,std,sd1):
    # calculate standard score for a series of numbers
    # give dev=deviation std=standard deviation
    y=0
    for y in range(N):
        sd1[y]=dev[y]/std
        print(sd1[y])

def outdata():
    pass

def trunk(number):
    # remove the extra zeros and decimal point
    y=0.0
    y=(number).strip(0)
    pass

def main():
    import math
    # list declaration
    x=[0]*N
    dev=[0.0]*N
    dev1=[0.0]*N
    sd1=[0.0]*N
    # file declaration
    infile=open('lab04.txt','r')
    outfile=open('lab04.out','w')
    # other variable declaration
    xbar=0.0    #mean
    std=0.0
    sumx=0.0
    dev2=0.0
    sd2=0.0


    # call functions
    loaddata(infile,x)
    sumx=sum_of(x)
    # compute the mean
    xbar=float(sumx/N)
    deviation(x,dev,dev1,xbar)
    dev2=sum_of(dev1)
    # compute standard deviation
    std=math.sqrt(dev2/N)
    # call standard
    standard(dev,std,sd1)
    sd2=sum_of(sd1)

    print(x)
    print(xbar)
    print(sumx)
    print(dev)
    print(dev1)
    print(dev2)
    print(std)
    print(sd1)
    print(int(sd2))
    hold()

    # call outdata(outfile,x,dev,dev1,sd1)
    k=0
    print(f'{"STATISTICAL ANALYSIS":^80}')
    print(f'{"SCORES"}\t{"DEV":^10}{"DEV1":^12}{"SD1":^12}')
    for k in range(N):
        print(f'{x[k]}\t{dev[k]:>10.5f}{dev1[k]:>12.5f}{sd1[k]:>12.5f}')
    print(f'{sumx}\t{xbar:>10.5f}{dev2:>12.5f}{sd2:>12.5f}')
    # output the rest
    # print the rest to output file
    outfile.write('SUM :'+ str(sumx)+'\n')
    outfile.write('AVERAGE :'+ str(xbar)+'\n')
    outfile.write('SUM OF STANDARAD SCORES: '+str(sd2)+'\n')
    # hold
    hold()

main()
