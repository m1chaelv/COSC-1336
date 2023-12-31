#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Lab07
#  File Name:         Lab07.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          [xx-xx-xxxx]
#  Instructor:        Onabajo
#  Chapter:           <Chapter x>
#  Session:           ACC Fall 2023
#
# Perform the following operations on a set of records
# 1. Pick a sort method (Insertion Sort)
# 2. Sort the records using the ID as the Key
# 3. Pick a Search Method (Binary Search)
# 4. Search the records and make appropriate modifications
#
# Restrictions:
# Must be user friendly
# Lots of comments
# Must be structured
# Must use array
# Must use function LOADDATA, OUTDATA, SORTDATA, SEARCHDATA
# 
# 
# Program to code bubble sort to sort a set of data to develop
# Binary Search to modify the data. It will call functions to
# load, sort, and modify
#***************************************************************

#***************************************************************
#  Function:     developerInfo
#  Description:  Prints Programmer's information
#  Parameters:   Assignment to include in signature
#  Returns:      Signature w/ date and time
#**************************************************************
def developerInfo(assignment):
    # Obtain current date and time
    from datetime import datetime
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M')

    signature=''
    signature+=(f'{"Name:":>12}\tMichael Villarreal\n')
    signature+=(f'{"Course:":>12}\tProgramming Fundamentals I\n')
    signature+=(f'{"Assignment:":>12}\t{assignment}\n')
    signature+=(f'{"Generated:":>12}\t{formatted_datetime}\n')
    signature+=spaces(2)

    return(signature)
    # End of the developerInfo function

#***************************************************************
#  Function:     spaces
#  Description:  Create a multi-line space to between input/output
#                to keep screen uncluttered
#  Parameters:   None
#  Returns:      n blank lines for screen or n new lines for str
#**************************************************************
def spaces(n):
    for x in range(n):
        print()
        return('\n'*n)
    # End of the spaces function

#***************************************************************
#  Function:     hold
#  Description:  Prompt to pause the screen until ready
#  Parameters:   None
#  Returns:      Nothing
#**************************************************************
def hold():
    input('Please enter any key to continue...')    
    # End of the hold function

#***************************************************************
#  Function:     get_int
#  Description:  Request numeric input from user. Any number not
#   an integer will be returned as a 0. Useful for menu prompts
#   to cancel loop verses exception error.
#  Parameters:   Text string will be used as user prompt + ": "
#  Returns:      integer or 0 if not an integer
#**************************************************************
def get_int(text):
    x=input(f'{text} :')
    if x=='':
        return 0
    else:
        return(int(x))
    # End of the get_int function

# LOADDATA
def loaddata():
    pass
    # End of loaddata function

# OUTDATA
def outdata(file,a,b):
    # file=outfile a=x b=score
    # local variable
    k=0
    while (k<n):
        print (a[k],' ',b[k])
        file.write(str(a[k])+' '+str(b[k])+'\n')
        k+=1
    # End of outdata function

# SORTDATA
def sortdata():
    pass
    # End of sortdata function

# SEARCHDATA
def searchdata():
    pass
    # End of searchdata function

# bubble
def bubble(a,b):
    # a=x/ID b=score
    # local variable
    flag=1  # replace k=0
    i=n-1
    j=0
    while (i >= 1) and (flag==1):
        flag=0
        j=0
        while (j <= i-1) :
            if a[j] > a[j+1]:
                # swapping id
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                # swapping scores
                temp1=b[j]
                b[j]=b[j+1]
                b[j+1]=temp1
                # reset flag
                flag=1
                j+=1
            else:
                j+=1
            # j+=1
        i-=1
    return(a,b)


    # End of bubble function

# loadrec
def loadrec(file,a,b):
    # file=infile a=x b=score
    # local variables
    k=0
    while (k < n):
        templist=file.readline().strip('\n').split(',')
        a[k]=int(templist[0])
        b[k]=int(templist[1])
        k+=1
    # End of loadrec function

# binary
def binary(file,a,b):
    # file=infiley a=x b=score
    k=0
    idn=0
    scn=0
    mid=0
    high=n

    # load data to be modified
    while k<5:
        templist=file.readline().strip('\n').split(',')
        idn=int(templist[0])
        scn=int(templist[1])
        # using the data
        low=0
        high=n
        flag=0  # i=0
        while (low<=high)and(flag==0):
            mid=int((low+high)/2)
            if (a[mid] == idn):
                # reset flag
                flag=1
                # replace the score
                b[mid]=scn
                print('Search modify successful')
            elif (a[mid] < idn):
                low=mid+1
            else:
                high=mid-1
        k+=1


#***************************************************************
#  Function:     main
#  Description:  orchestrate file ingestion and procesing
#  Parameters:   none
#  Returns:      final report to screen and file
#**************************************************************
# Global Variables
n=20

def main():
    # file declaration
    infile=open('Lab07.txt','r')
    infiley=open('Lab07.upd','r')
    outfile=open('Lab07.out','w')
    # local variables
    x=[0]*n
    score=[0]*n
    #call functions
    loadrec(infile,x,score)

    print('Unsorted data')
    outdata(outfile,x,score)

    # x,score=bubble(x,score)
    bubble(x,score)
    print('Sorted data')
    outdata(outfile,x,score)

    binary(infiley,x,score)
    print('Modified Data')
    outdata(outfile,x,score)

    # close file
    infile.close()
    infiley.close()
    outfile.close()

    #hold screen
    hold()



    # End of the developerInfo function

# Call the main function.
if __name__ == '__main__':
    main()