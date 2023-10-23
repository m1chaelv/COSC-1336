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

def get_dimensions(matrix):
    # x=rows=column-wise
    # y=column=row-wise
    x=0 
    y=0
    for r in matrix:
        # for c in r[0]:
        #     y+=1
        x+=1
        y=len(r)
    return(x,y)
    hold()


def computez(x,y,z):
    dimensions=[]
    print(x)
    dimensions+=[get_dimensions(x)]
    print(y)
    dimensions+=[get_dimensions(y)]
    print(z)
    # dimensions+=[get_dimensions(z)]
    for rz in z:
        for cz in rz:
            print(cz,end=' ')
        print()
    print()
    print(dimensions)
    z_size=[]
    for k0 in range(2):
        for k1 in range(2):
            if k0==k1:
                # print(k0,k1)
                print(dimensions[k0][k1])
                z_size+=[dimensions[k0][k1]]
    print(z_size)
    # dimensions+=[z_size]
    print(dimensions)
    print()
    hold()

    print(z)
    test=[0]*z_size[1]
    test2=list(test)
    test=[]
    print(test)
    for k in range(z_size[0]):
        test.append(test2)
    # test=[test]*[z_size[0]]
    print(test)
    hold()

    # for k in range(z_size[0]):
    #     # xx=[]*z_size[1]
    #     # x.append(xx)
    #     x=([]*z_size[1])*z_size[0]
    # print('using calculation')
    # print(x)
    # hold()

    
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                z[i][j] += x[i][k] * y[k][j]
    for r in z:
        print(r)

    # while k0 in range(len(x)):
    #     while k1 in range(len(y))
    hold()

def summation(x,y):
    pass

def smallest(y):
    pass

def print_matrix(title,matrix,width):
    k=len(title)+6
    print(f'{title:^{k}}')
    for r in matrix:
        for c in r:
            print(f'{c:>{width}}', end=' ')
        print()

def outdata(outfile,x,y,z):
    print(f'\nOUTDATA(OUTFILE,X,Y,Z)\n')
    # x=[5][3]
    # y=[3][7]
    # local variable

    print_matrix('x-matrix',x,3)
    print_matrix('y-matrix',y,3)
    print_matrix('z-matrix',z,5)

def load_any(file,matrix,rc_based):
    # rc_based true is row based column-wise
    # rc_based false is col based row-wise
    infile=open(file,'r')

    r=len(matrix)
    for k in matrix:
        c=len(k)

    temp_list=infile.readline().strip('\n').split(',')

    k=0
    if rc_based==True:
        for rx in range(r):
            for cx in range(c):
                matrix[rx][cx]=int(temp_list[k])
                k+=1
    else:
        for cx in range(c):
            for rx in range(r):
                matrix[rx][cx]=int(temp_list[k])
                k+=1
    infile.close()
    return(matrix)

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
        outfile=open('Lab05.out','w')

        # variable declaration
        small=0
        x_file='Lab05_x.txt'
        y_file='Lab05_y.txt'

        # call function
        print('load any x')
        x=load_any(x_file,x,True)
        print('load any y')
        y=load_any(y_file,y,False)

        print('compute z')
        computez(x,y,z)
        # summation(x,y)
        # small=smallest(y)
        print('outdata')
        outdata(outfile,x,y,z)
        print('print x\n',x)
        print('print y\n',y)
        hold()
        

        #write the rest of the output
        print(f'SUM X\t{sumx}')
        print(f'SUM Y\t{sumy}')
        print(f'SUMX + SUMY\t{sumx+sumy}')
        print(f'SMALLEST\t{small}')

        #close files

        outfile.close()
    except Exception as err:
        print(err)
        hold()

    hold()



# Call the main function.
if __name__ == '__main__':
    main()