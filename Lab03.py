#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Lab 3
#  File Name:         Lab03.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          10-04-2023
#  Instructor:        Onabajo
#
# Baseball program for Texas Rangers
# I will load from a data file and compute
# Batting Average and Slugging Average for
# all players..
#***************************************************************

# Global Variables
PLAYERS=9

#***************************************************************
#  Function:     developerInfo
#  Description:  display's developer's information
#  Parameters:   none
#  Returns:      signature
#**************************************************************
def developerInfo():
    print('\n\n')
    print('Name:     Michael Villarreal')
    print('Course:   Programming Fundamentals I')
    print('Lab: 3')
    print()
    # End of the developerInfo function

#***************************************************************
#  Function:     hold
#  Description:  prompt to pause the screen until ready
#  Parameters:   none
#  Returns:      nothing
#**************************************************************
def hold():
    print('\n\n\n')
    input('Please enter any key to continue...')    


# functions
#***************************************************************
#  Function:     single
#  Description:  calculate single
#  Parameters:   none
#  Returns:      return same number
#**************************************************************
# In baseball, a batting average is computer by
# 
# Dividing the total number of hits by the total number of times at bat. The slugging
# average is computed dividing the total number of bases by the total number of times
# at bat. For this computation, a single is counted as a base, a double as two bases etc.
# 
# Write a program that will read as input the number of singles, doubles, triples, and
# home run, and the total number of times at bat for a player. Compute and print the
# batting average and the slugging average
# 
# Use the following functions:
# single (to compute single)
# double (to compute doubles)
# triple (to compute triples)
# homerun (to compute the home runs)
# 
# Use the following test data:
# 
# Player	Single	Double	Triple	Homerun	Atbat
# 1	5	3	1	2	70
# 2	3	0	2	1	15
# 3	10	5	3	0	30
# 4	12	5	9	2	40
# 5	6	9	2	4	34
# 6	9	10	1	6	45
# 7	20	3	5	1	80
# 8	4	0	1	2	20
# 9	7	12	0	2	40
# 
# Output
# 
# Player	Batting Average	Slugging Average
# 1	.157	.314
# 2	.400	.867
# 3	.600	.967
# 
# Restrictions:
# Must be user friendly:
# Lots of comments
# Must use functions
# Must use data file?

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
        # hold
        hold()
        print(templist,ba)
        k=k+1

    infile.close()
    outfile.close()


# functions
def single(x):
        # local variable
        x1=0
        # calculate
        x1=x*1
        return(x1)

#***************************************************************
#  Function:     double
#  Description:  calculate double
#  Parameters:   none
#  Returns:      multiple of 2
#**************************************************************
def double(x):
        # local variable
        x1=0
        # calculate
        x1=x*2
        return(x1)

#***************************************************************
#  Function:     triple
#  Description:  calculate triple
#  Parameters:   none
#  Returns:      multiple of 3
#**************************************************************
def triple(x):
        # local variable
        x1=0
        # calculate
        x1=x*3
        return(x1)

#***************************************************************
#  Function:     homerun
#  Description:  calculate homerun
#  Parameters:   none
#  Returns:      multiple of 4
#**************************************************************
def homerun(x):
        # local variable
        x1=0
        # calculate
        x1=x*4 
        return(x1)

#***************************************************************
#  Function:     main
#  Description:  primary function
#  Parameters:   none
#  Returns:      nothing
#**************************************************************
def main():
    
    # File declaration
    infile=open('lab03.txt','r')
    outfile=open('lab03.out','w')

    # variable declarations
    p=s=d=t=hr=atbat=0
    s1=d1=t1=hr1=0

    # print header to display
    print('\n\n\n')
    print(f'{"Player":<7}|{"Batting Avg":^13}|{"Slugging Avg":^15}')
    print(f'{" ":<7}|{" ":^13}|{" ":^15}')

    # using a loop to yank data from file line by line
    for k in range(PLAYERS):
        # load
        templist=infile.readline().strip('\n').split(',')
        p=int(templist[0])
        s=int(templist[1])
        d=int(templist[2])
        t=int(templist[3])
        hr=int(templist[4])
        atbat=int(templist[5])

        # compute batting average 
        ba=round((s+d+t+hr)/atbat,3)

        # call function
        s1=single(s)
        d1=double(d)
        t1=triple(t)
        hr1=homerun(hr)

        # compute slugging average
        sa=round((s1+d1+t1+hr1)/atbat,3)
        
        # output
        print(f'{p:<7}|{ba:^13.3f}|{sa:^15.3f}')
        outfile.write(str(p)+','+str(ba)+','+str(sa)+'\n')
    
    # close files
    infile.close()
    outfile.close()

    # signature
    developerInfo()

    # hold
    hold()

# Execute Main()
main()
