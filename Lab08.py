#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Lab 8
#  File Name:         Lab08.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          11-27-2023
#  Instructor:        Onabajo
#
# Baseball program for Texas Rangers
# I will load from a data file and compute
# Batting Average and Slugging Average for
# all players..
#***************************************************************
# In baseball, a batting average is computer by
# 
# Dividing the total number of hits by the total number of times
# at bat. The slugging average is computed dividing the total number 
# of bases by the total number of times at bat. For this computation, 
# a single is counted as a base, a double as two bases etc.
# 
# Write a program that will read as input the number of singles, 
# doubles, triples, and home run, and the total number of times 
# at bat for a player. Compute and print the batting average 
# and the slugging average
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
# 1 	    5	    3	    1	    2	    70
# 2	        3	    0	    2	    1	    15
# 3	        10	    5	    3	    0	    30
# 4	        12	    5	    9	    2	    40
# 5	        6	    9	    2	    4	    34
# 6	        9	    10	    1	    6	    45
# 7	        20	    3	    5	    1	    80
# 8	        4	    0	    1	    2	    20
# 9	        7	    12	    0	    2	    40
# 
# Output
# 
# Player	Batting Average	Slugging Average
# 1	.157	.314
# 2	.400	.867
# 3	.600	.967
# 
# Restrictions:
# Must implement using Classes
#**************************************************************

import baseball

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
    print('Lab: 8')
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

#***************************************************************
#  Function:     main
#  Description:  primary function
#  Parameters:   none
#  Returns:      nothing
#**************************************************************
def main():
    # derieve class baseball
    base=baseball.baseball()

    # File declaration
    infile=open('lab08.txt','r')
    outfile=open('lab08.out','w')

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
        s1=base.single(s)
        d1=base.double(d)
        t1=base.triple(t)
        hr1=base.homerun(hr)

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
