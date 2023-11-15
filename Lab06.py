#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Lab 6
#  File Name:         Lab06.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          [xx-xx-xxxx]
#  Instructor:        Onabajo
#  Chapter:           <Chapter 9> Dictionaries and Sets
#  Session:           ACC Fall 2023
#
# [xxx]
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

#***************************************************************
#  Function:     loadfile
#  Description:  Load data file into list for processing.
#  Parameters:   file name
#  Returns:      populated list
#**************************************************************
def loadfile(file,a,b,c,d):
    # inbound parameters
    # a=food_type
    # b=reservation
    # c=rating
    # d=credit_card
    # file=data source file
    # 
    # variables
    matrix=[]

    # ingest data from file
    infile=open(file,'r')
    for k in infile:
        new_line=k.strip('\n').split(',')
        matrix.append(new_line)
    infile.close()

    # load data into dictionaries
    for k in matrix:
        a[k[0]]=k[1]
        b[k[0]]=k[2]
        c[k[0]]=int(k[3])
        d[k[0]]=k[4]

    # print(food_type)
    # print(reservation)
    # print(rating)
    # print(credit_card)
    # hold()

    return(a,b,c,d)
    # End of the loadfile function


#***************************************************************
#  Function:     main
#  Description:  orchestrate file ingestion and procesing
#  Parameters:   none
#  Returns:      final report to screen and file
#**************************************************************
# Global Variables
input_file='Lab06.txt'



def main():
    #initialize dictionaries
    food_type={}
    reservation={}
    rating={}
    credit_card={}

    spaces(3)
    food_type,reservation,rating,credit_card=loadfile(input_file,food_type,reservation,rating,credit_card)
    print(food_type)
    print(reservation)
    print(rating)
    print(credit_card)
    hold()


# Call the main function.
if __name__ == '__main__':
    main()