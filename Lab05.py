#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Lab 5
#  File Name:         Lab05.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          10-24-2023
#  Instructor:        Onabajo
#  Chapter:           <Chapter ?>
#  Session:           ACC Fall 2023
#
# Program to build and manipulate matrices
# It will use functions to load, multiply matrices
# also compute summation, smallest, and print all matrices
#***************************************************************

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

#***************************************************************
#  Function:     get_dimensions
#  Description:  provided a matrix, calculate the overall dimensions
#   for use in loops or calculations
#  Parameters:   matrix
#  Returns:      matrix dimensions
#**************************************************************
def get_dimensions(matrix):
    # x=rows=column-wise
    # y=column=row-wise
    
    # reset counters
    x=0 
    y=0
    
    # loop through matrix
    for r in matrix:
        x+=1
        y=len(r)

    # return dimensions
    return(x,y)

#***************************************************************
#  Function:     computez
#  Description:  given the populated x-y matrix multiply the 
#   two to output completed z matrix
#  Parameters:   x-y matrix to evalute and empty z matrix
#  Returns:      None but z matrix populated
#**************************************************************
def computez(x,y,z):
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                z[i][j] += x[i][k] * y[k][j]

#***************************************************************
#  Function:     summation
#  Description:  given the associated row/column calculate the
#   the summary value
#  Parameters:   matrix to evalute, row or column to evaluate,
#   and row/column identity to evaluate
#  Returns:      return the calculated sum value
#**************************************************************
def summation(matrix,rc,num):
    # reset counters
    sum_r=0
    sum_c=0

    # error handling
    try:
        # sum of column
        if rc=='c':        
            for k0 in matrix:
                sum_c+=k0[num]
            return(sum_c)
        # sum of row
        elif rc=='r':
            for k0 in matrix[num]:
                sum_r+=k0
            return(sum_r)            
    except Exception as err:
        print(err)
    
#***************************************************************
#  Function:     smallest
#  Description:  given the associated row/column calculate the
#   the smallest value
#  Parameters:   matrix to evalute, row or column to evaluate,
#   and row/column identity to evaluate
#  Returns:      return the calculated smallest value
#**************************************************************
def smallest(matrix,rc,num):
    # reset counter
    small=0
    small_matrix=[]

    # error handling
    try:
        # generate subset of matrix column
        if rc=='c':        
            for k0 in matrix:
                small_matrix.append(k0[num])
        # generate subset of matrix row
        elif rc=='r':
            for k0 in matrix[num]:
                small_matrix.append(k0)

        # reset counter
        k0=0
        # evaluate list to identify smallest
        for k1 in small_matrix:
            if k0==0:
                small=k1
            else:
                if k1<small:
                    small=k1
            k0+=1

        # return smallest value
        return(small)
    except Exception as err:
        print(err)

#***************************************************************
#  Function:     print_matrix
#  Description:  Supply a populated matrix and generate a report
#   ready output for screen and file
#  Parameters:   matrix title, matrix, width or spacing between
#   variables. Allows for spacing adjustments for larger variables
#  Returns:      populated matrix with header
#**************************************************************
def print_matrix(title,matrix,width):
    # calculate width of matrix to build a header to match
    how_wide=(get_dimensions(matrix)[1])*(width+1)

    # generate a string for output to screen and file
    report=''
    report+=(f'{title:=^{how_wide}}\n')
    for r in matrix:
        for c in r:
            report+=(f'{c:>{width}}')
        report+=('\n')
    report+=(f'{"=":=^{how_wide}}\n')

    # return completed report
    return(report)

#***************************************************************
#  Function:     outdata
#  Description:  calculate summary, generate report for screen
#   and file output, output to file and screen
#  Parameters:   output file, x-y-z matrix tables
#  Returns:      None
#**************************************************************
def outdata(outfile,x,y,z):
    # calculate summary data
    sumx=summation(x,'c',2)
    sumy=summation(y,'r',2)
    small=smallest(y,'r',1)

    # build report output
    report=''
    report+=print_matrix('x-matrix',x,3)
    report+=print_matrix('y-matrix',y,3)
    report+=print_matrix('z-matrix',z,5)

    # append summary to report
    report+=(f'{"SUM X:":>20}\t{sumx}\n')
    report+=(f'{"SUM Y:":>20}\t{sumy}\n')
    report+=(f'{"SUMX + SUMY:":>20}\t{sumx+sumy}\n')
    report+=(f'{"SMALLEST:":>20}\t{small}\n')

    # output to file
    output_file=open(outfile,'w')
    output_file.write(report)
    output_file.close()

    # output report to screen
    spaces(3)
    print(report)
    spaces(2)
    # output developer info to screen
    developerInfo()

#***************************************************************
#  Function:     load_any
#  Description:  open input file and populate the provided matrix
#   given the format for loading row-wise vs column-wise
#  Parameters:   input filename, matrix to populate, orientation 
#   for loading matrix
#  Returns: fully populated matrix     
#**************************************************************
def load_any(file,matrix,rc_based):
    # rc_based 'True' is row based column-wise
    # rc_based 'False' is col based row-wise
    # open input file
    infile=open(file,'r')

    # retrieve matrix dimensions for use in loops
    r=get_dimensions(matrix)[0]
    c=get_dimensions(matrix)[1]

    # retrieve data from input file
    temp_list=infile.readline().strip('\n').split(',')

    # populate matrix
    # rest counter
    k=0
    # column-wise
    if rc_based==True:
        for rx in range(r):
            for cx in range(c):
                matrix[rx][cx]=int(temp_list[k])
                k+=1
    # row-wise
    else:
        for cx in range(c):
            for rx in range(r):
                matrix[rx][cx]=int(temp_list[k])
                k+=1
    # close input file
    infile.close()
    # return matrix
    return(matrix)

#***************************************************************
#  Function:     main
#  Description:  orchestrate file ingestion and procesing
#  Parameters:   none
#  Returns:      final report to screen and file
#**************************************************************
# Global Variables
sumx=0
sumy=0

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
        # variable declaration
        x_file='Lab05_x.txt'
        y_file='Lab05_y.txt'
        outfile='Lab05.out'

        # call function
        x=load_any(x_file,x,True)
        y=load_any(y_file,y,False)
        computez(x,y,z)
        outdata(outfile,x,y,z)

    except Exception as err:
        print(err)
        hold()

    hold()

# Call the main function.
if __name__ == '__main__':
    main()