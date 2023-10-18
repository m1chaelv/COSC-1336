#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Lab 5
#  File Name:         Lab05.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          10-18-2023
#  Instructor:        Onabajo
#  Chapter:           <Chapter ?>
#  Session:           ACC Fall 2023
#
# Program to build and manipulate matrices
# It will use functions to load, multiply matrices
# also compute summation, smallest, and print all matrices
#***************************************************************

# Global Variables
sumx=0
sumy=0

#***************************************************************
#  Function:     developerInfo
#  Description:  Prints Programmer's information
#  Parameters:   None
#  Returns:      Output signature
#**************************************************************
def developerInfo():
    print('Name:     Michael Villarreal')
    print('Course:   Programming Fundamentals I')
    print('Lab: 5')
    print()
    # End of the developerInfo function

#***************************************************************
#  Function:     spaces
#  Description:  Create a multi-line space to between input/output
#                to keep screen uncluttered
#  Parameters:   None
#  Returns:      n blank lines
#**************************************************************
def spaces(n):
    for x in range(n):
        print()


#***************************************************************
#  Function:     hold
#  Description:  Prompt to pause the screen until ready
#  Parameters:   None
#  Returns:      Nothing
#**************************************************************
def hold():
    input('Please enter any key to continue...')    

# def load_x(infile_x,x):
#     pass
def load_x(infile,x):
    # file=infile, a=x[5][3]
    # load variables
    k=0
    k2=0
    # yank the data across
    templist=infile.readline().strip('\n').split(',')
    # loading rows
    while (k<5):
        k1=0
        # loading columns
        while(k1<3):
            x[k][k1]=int(templist[k2])
            k1+=1
            k2+=1
        k+=1
    print(templist)
    hold()

# def load_y(infile_y,y):
#     pass
def load_y(infile,x):
    # file=infile, a=x[3][7]
    # load variables
    k=0
    k2=0
    # yank the data across
    templist=infile.readline().strip('\n').split(',')
    # loading row
    while (k<3):
        k1=0
        # loading columns
        while(k1<5):
            x[k][k1]=int(templist[k2])
            k1+=1
            k2+=1
        k+=1
    print(templist)
    hold()

def computez(x,y,z):
    pass

def summation(x,y):
    pass

def smallest(y):
    pass

# def outfile(outfile,x,y,z):
#     pass
def outdata(outfile,x,y,z):
    # x=[5][3]
    # y=[3][7]
    # local variable
    k=0
    print('X- MATRIX  ')
    while (k<5):
        print(x[k][0],x[k][1],x[k][2],x[k][3],x[k][4])
        k+=1

    k=0
    print('Y- MATRIX  ')
    while (k<3):
        print(y[k][0],y[k][1],y[k][2],y[k][3],y[k][4],y[k][5],y[k][6])
        k+=1

#***************************************************************
#  Function:     main
#  Description:  orchestrate file ingestion and procesing
#  Parameters:   none
#  Returns:      final report to screen and file
#**************************************************************
def main():
    # matrices declaration
    # x[5][3], y[3][7], z[5][7]
    x=[[0,0,0],
       [0,0,0],
       [0,0,0],
       [0,0,0],
       [0,0,0]]
    
    y=[[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]
    
    z=[[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]
    
    try:
        # file declaration
        infile_x=open('Lab05_x.txt','r')
        infile_y=open('Lab05_y.txt','r')
        outfile=open('Lab05.out','w')

        # variable declaration
        small=0

        # call function
        load_x(infile_x,x)
        load_y(infile_y,y)
        computez(x,y,z)
        summation(x,y)
        small=smallest(y)
        outdata(outfile,x,y,z)

        #write the rest of the output
        print(f'SUM X\t{sumx}')
        print(f'SUM Y\t{sumy}')
        print(f'SUMX + SUMY\t{sumx+sumy}')
        print(f'SMALLEST\t{small}')

        #close files
        infile_x.close()
        infile_y.close()
        outfile.close()
    except Exception as err:
        print(err)
        hold()

    hold()



# Call the main function.
if __name__ == '__main__':
    main()