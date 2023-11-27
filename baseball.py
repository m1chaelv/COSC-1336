#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Lab 8
#  File Name:         baseball.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          11-27-2023
#  Instructor:        Onabajo
#
#***************************************************************
# In baseball, a batting average is computer by
# 
# Dividing the total number of hits by the total number of times
# at bat. The slugging average is computed dividing the total number 
# of bases by the total number of times at bat. For this computation, 
# a single is counted as a base, a double as two bases etc.
# 
# Write a class that will compute and print the batting average 
# and the slugging average
# 
# Use the following functions:
# single (to compute single)
# double (to compute doubles)
# triple (to compute triples)
# homerun (to compute the home runs)
#***************************************************************

class baseball():
    #***************************************************************
    #  Function:     single
    #  Description:  calculate single
    #  Parameters:   none
    #  Returns:      return same number
    #**************************************************************
    def single(self,x):
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
    def double(self,x):
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
    def triple(self,x):
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
    def homerun(self,x):
            # local variable
            x1=0
            # calculate
            x1=x*4 
            return(x1)