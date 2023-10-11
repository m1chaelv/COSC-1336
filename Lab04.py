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

def deviation1(x,dev,xbar):
    # dev, xbar
    for k in range(N):
        dev[k]=trunk(xbar-x[k])

def deviation2(dev,dev1):
    # dev, dev1
    for k in range(N):
        dev1[k]=trunk((dev[k])**2)

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

def standard(dev,std,sd1):
    # calculate standard score for a series of numbers
    # give dev=deviation std=standard deviation
    y=0
    for y in range(N):
        sd1[y]=dev[y]/std
        # print(sd1[y])

def outdata(outfile,x,dev,dev1,dev2,sd1,sd2,xbar,sumx,std):
    # set variables
    k=0
    header=''
    body=''
    footer=''
    # build up report header
    header+=(f'{"STATISTICAL ANALYSIS":-^38}\n\n')
    # build up report body
    body+=(f'{"SCORES":<8}{"DEV":>6}{"DEV1":>12}{"SD1":>12}\n')
    for k in range(N):
        body+=(f'{x[k]:<8}{dev[k]:>6}{dev1[k]:>12}{sd1[k]:>12.5f}\n')
    # build up report footer
    footer+=(f'{"Sum:":-<23}{sumx:->15}\n')
    footer+=(f'{"Average:":-<23}{xbar:->15}\n')
    footer+=(f'{"Sum Standard Deviation:":-<23}{dev2:->15}\n')
    footer+=(f'{"Sum of Standard Score:":-<23}{sd2:->15}\n')
    footer+=(f'{"Standard Deviation:":-<23}{std:->15}\n')
    # output to screen
    print(header)
    print(body)
    print(footer)
    # output to file
    outfile.write(header)
    outfile.write(body)
    outfile.write(footer)

def trunk(number):
    # remove the extra zeros and decimal point
    if number%1 == 0:
        return (int(number))
    test=f'{number:.5f}'
    test2=(test.rstrip('0').rstrip('.'))

    if float(test2)%1 == 0:
        return (int(test2))
    else:
        return(float(test2))

def main():
    # list declaration
    x=[0.0]*N
    dev=[0.0]*N
    dev1=[0.0]*N
    sd1=[0.0]*N
    # file declaration
    infile=open('lab04.txt','r')
    outfile=open('lab04.out','w')
    # other variable declaration
    xbar=std=sumx=dev2=sd2=0.0

    # call functions
    loaddata(infile,x)
    sumx=sum_of(x)
    # compute the mean
    xbar=trunk(float(sumx/N))
    deviation1(x,dev,xbar)
    deviation2(dev,dev1)
    dev2=trunk(sum_of(dev1))
    # compute standard deviation
    std=trunk((dev2/N)**.5)
    # call standard
    standard(dev,std,sd1)
    sd2=trunk(sum_of(sd1))

    # call outdata(outfile,x,dev,dev1,sd1)
    outdata(outfile,x,dev,dev1,dev2,sd1,sd2,xbar,sumx,std)

    #close files
    infile.close()
    outfile.close()
    developerInfo()
    # hold
    hold()

main()
