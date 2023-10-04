#***************************************************************
#
#  Developer:         Michael Villarreal
#  Program #:         Lab 2
#  File Name:         Lab03.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          10-04-2023
#  Instructor:        Onabajo
#  Chapter:           <Chapter ?>
#
# Baseball program for Texas Rangers
# I will load from a data file and compute
# Batting Average and Slugging Average for
# all players..

# Global Variables
PLAYERS=9

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
    print('Lab: 2')
    print()
    # End of the developerInfo function

#***************************************************************
#
#  Function:     next
#  Description:  Create a multi-line space to between input/output
#                to keep screen uncluttered
#  Parameters:   None
#  Returns:      3 blank lines
#
#**************************************************************
def next():
    print ()
    print ()
    print ()

#***************************************************************
#
#  Function:     hold
#  Description:  Prompt to pause the screen until ready
#  Parameters:   None
#  Returns:      Nothing
#
#**************************************************************
def hold():
    dummy=input('Please enter any key to continue...')    

#***************************************************************
#
#  Function:     hold
#  Description:  Prompt to pause the screen until ready
#  Parameters:   None
#  Returns:      Nothing
#
#**************************************************************
def main():
    # File declaration
    infile=open('lab03.txt','r')
    outfile=open('lab03.out','w')
    # variable declarations
    p=s=d=t=hr=atbat=0
    s1=d1=t1=hr1=0
    # using a loop to yank data from file line by line
    k=0
    while (k<PLAYERS):
        # load
        templist=infile.readline().strip('\n').split(',')
        p=int(templist[0])
        s=int(templist[1])
        d=int(templist[2])
        t=int(templist[3])
        hr=int(templist[4])
        atbat=int(templist[5])
        # compute batting average 
        ba=(s+d+t+hr)/atbat
        # call function
        s1=single(s)
        d1=double(d)
        t1=triple(t)
        hr1=homerun(hr)
        # compute slugging average
        sa=(s1+d1+t1+hr1)/atbat
        # output
        print(p,ba,sa)
#        outdata(outfile,str(p)+str(ba)+str(sa)+'\n')
        outfile.write(str(p)+str(ba)+str(sa)+'\n')
        # close files
        infile.close()
        outfile.close()
        # hold
        hold()
        print(templist,ba)
        k=k+1


# functions
def single(x):
        # local variable
        x1=0
        # calculate
        x1=x*1
        return(x1)

def double(x):
        # local variable
        x1=0
        # calculate
        x1=x*2
        return(x1)

def triple(x):
        # local variable
        x1=0
        # calculate
        x1=x*3
        return(x1)

def homerun(x):
        # local variable
        x1=0
        # calculate
        x1=x*4 
        return(x1)







# Execute Main()
main()
