#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Lab07
#  File Name:         Lab07.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          [11-27-2023]
#  Instructor:        Onabajo
#  Chapter:           <Chapter ?>
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

    print(signature)
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

# LOADDATA
#***************************************************************
#  Function:     loaddata
#  Description:  open input file and parse ID & Grade array
#  Parameters:   input file name
#  Returns:      ID array as integer & Grade array as integer
#**************************************************************
def loaddata(file):
    # file=file_in
    # local variables
    temp_id=[]                  # ID array
    temp_grade=[]               # Grade array
    temp_in_file=open(file)     # open input file

    # loop through each line
    for k1 in temp_in_file:
        if k1=='\n':            # skip blank lines
            print('blank')
        else:
            temp_load=k1.strip().split(',')         # parsing each line to ID, Grade
            temp_id.append(int(temp_load[0]))       # appending ID to temp array
            temp_grade.append(int(temp_load[1]))    # appending Grade to temp array
    
    temp_in_file.close()        # close input file
    return(temp_id,temp_grade)  # return 2 arrays ID, Grade
    # End of loaddata function

# SORTDATA (insertion sort)
#***************************************************************
#  Function:     sortdata
#  Description:  sort 2 arrays using the first as key
#  Parameters:   2 arrays (ID & Grade)
#  Returns:      sorted ID array and matching Grade array
#**************************************************************
def sortdata(a,b):
    # a=ID b=grades
    # local variables
    k1=1
    # outer loop from k1[1] to end of array
    while k1<=len(a)-1:
        j1=k1
        # inner loop from current location to k1[1] 
        while (j1>=1) and (a[j1-1]>a[j1]):  # will continue repeating until item is sorted
            # swap ID records
            temp_a=a[j1-1]
            a[j1-1]=a[j1]
            a[j1]=temp_a
            # swap grade records
            temp_b=b[j1-1]
            b[j1-1]=b[j1]
            b[j1]=temp_b
            j1-=1                           # increment counter down
        k1+=1                               # increment counter up
    return(a,b)
    # End of sortdata function

# SEARCHDATA (binary search)
#***************************************************************
#  Function:     searchdata
#  Description:  retreives update file and updates array
#  Parameters:   file name of file containing corrections 
#                   and 2 arrays (ID & Grade)
#  Returns:      updated ID array and matching Grade array
#**************************************************************
def searchdata(file,a,b):
    # file=file_updates a=ID b=score
    # local variables
    temp_infile=open(file,'r')
    mid=0

    # loop once per entry in update file
    for k1 in temp_infile:
        temp_data=k1.strip().split(',')     # parsing each line to ID, Grade
        if k1!='\n':                        # processes only lines that are not empty
            temp_a=int(temp_data[0])        # convert ID to integer
            temp_b=int(temp_data[1])        # convert Grade to integer
            high=len(a)                     # set high variable to length of ID array
            low=mid=0                       # initialize mid and low values to 0
            flag=True                       # flag to indicate when to exit loop (False)
            while flag:
                mid=(low+high)//2           # set mid to halfway point
                if a[mid]==temp_a:          # if current location [mid] matches the ID then process update
                    b[mid]=temp_b           # update matching Grade
                    flag=False              # exit loop
                else:                       # if no match determine if we eliminate upper or lower half of remainder
                    if a[mid]<temp_a:       # if current location [mid] < ID (eliminate lower half)
                        low=mid+1           # move low mark to current location
                    else:                   # if current location [mid] < ID (eliminate upper half)
                        high=mid-1          # move high mark to current location
    
    temp_infile.close()                     # close file
    return(a,b)                             # return ID array and updated Grade array
    # end of searchdata function

#***************************************************************
#  Function:     column_width
#  Description:  calculate the width of a column by inspecting 
#                   each entry in an array and associated header
#  Parameters:   array to inspect, desired buffer, and related header
#  Returns:      integer with calculated column width
#**************************************************************
def column_width(a,b,c):
    # a=array, b=buffer, c=header
    # local variables
    column0=0

    if c=='#':                          # if header is # indicates this is row counter
        for k1 in a:                    # inspect each entry in the array
            column0+=1                  # increment by 1
        column0=len(str(column0))+b     # convert counter to str and calculate width plus buffer
    else:
        for k1 in a:                    # inspect each entry in the array
            if len(str(k1))>column0:    # inspect each entry in the array
                column0=len(str(k1))    # counter updated if entry has a larger width value
        column0+=b                      # update counter with buffer
    if (len(c)+b)>column0:              # test if header width exceeds data+buffer width
        column0=len(c)+b                # update if true
    return(column0)                     # return column width calclation with buffer
    # end of column_width function

#***************************************************************
#  Function:     report_out
#  Description:  generate a structred report
#  Parameters:   ID and Grade array, plus title for report
#  Returns:      formatted report as string
#**************************************************************
def report_out(a,b,c):
    # a=id, b=grade, c=header
    # initialize column variables
    column_0=column_width(a,0,'#')
    column_a=column_width(a,1,'')
    column_b=column_width(b,3,'')
    column_ab=column_a+column_b
    # initialize report
    report=spaces(1)
    
    # generate report header
    report+=(f'{"#":>{column_0}} {c:>{column_ab}}\n')
    report+=(f'{"":->{column_0}} {"":->{column_ab}}\n')

    # generate report with [row number, ID, Grade]
    for k1 in range (0,len(b)):
        report+=(f'{k1+1:>{column_0}} {a[k1]:>{column_a}}{b[k1]:.>{column_b}}\n')
    
    # finalize report
    report+=spaces(1)

    # print report to screen
    print(report)

    # return completed report as string
    return(report)
    # end of report_out function

# OUTDATA
#***************************************************************
#  Function:     outdata
#  Description:  output report to file
#  Parameters:   file name of output file and report
#  Returns:      output file
#**************************************************************
def outdata(file,a):
    # file=file_out a=report
    # local variable
    
    # if report is empty then initialize an empty file
    if a=='':
        outfile=open(file,'w')
    # if report is not empty then it appends the report to file
    else:
        outfile=open(file,'a')
        outfile.write(a)
    
    # close file
    outfile.close()
    # End of outdata function

#***************************************************************
#  Function:     main
#  Description:  orchestrate file ingestion and procesing
#  Parameters:   none
#  Returns:      final report to screen and file
#**************************************************************
# Global Variables
# n=20
assignment='Lab 07'

def main():
    # local variables
    file_in='Lab07.txt'
    file_updates='Lab07.upd'
    file_out='Lab07.out'
    id=[0]
    grades=[0]
    report=''
    outdata(file_out,report)

    # title
    report+=developerInfo(assignment)

    #call functions
    # LOADDATA
    id,grades=loaddata(file_in)
    report+=report_out(id,grades,'unsorted')
    hold()

    # SORTDATA
    id,grades=sortdata(id,grades)
    report+=report_out(id,grades,'sorted')
    hold()

    # SEARCHDATA
    id,grades=searchdata(file_updates,id,grades)
    report+=report_out(id,grades,'updated')
    hold()

    #OUTDATA
    outdata(file_out,report)

    #hold screen
    hold()
    # End of the main function

# Call the main function.
if __name__ == '__main__':
    main()