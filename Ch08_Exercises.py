#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Chapter 8 - Exercises
#  File Name:         Ch08_Exercises.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          [xx-xx-xxxx]
#  Instructor:        Onabajo
#  Chapter:           <Chapter 8>
#  Session:           ACC Fall 2023
#
#   More about strings: Basic String Operations, String Slicing, &
#   Testing, Searching, and Manipulating Strings
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

# 1 Initials
# Write a program that gets a string containing a person's first, middle, and last names, and displays their
# first, middle, and last initials. For example, if the user enters John William Smith, the program should display J. W. S.
def initials():
    # initialize variable
    i_ltrs=[]
    l_init=[]
    spaces(3)
    full_name=input('Enter your full name: ')
    
    # loop to evaluate each letter of the full name

    for k1 in full_name:
        pass



#***************************************************************
#  Function:     main
#  Description:  orchestrate file ingestion and procesing
#  Parameters:   none
#  Returns:      final report to screen and file
#**************************************************************
# Global Variables
# [xxx]
def main():
    print('')
    MENU=1
    while MENU > 0 and MENU <= 26:
        print('[1]\t Initials')
        print('[2]\t xxx')
        print('[3]\t xxx')
        print('[4]\t xxx')
        print('[5]\t xxx')
        print('[6]\t xxx')
        print('[7]\t xxx')
        print('[8]\t xxx')
        print('[9]\t xxx')
        print('[10]\t xxx')
        print('[11]\t xxx')
        print('[12]\t xxx')
        print('[13]\t xxx')
        print('[14]\t xxx')
        print('...\tanything else to exit\n')
        MENU=get_int('Make a selection to continue')
        if MENU==1:
            initials()
        elif MENU==2:
            hold()
        elif MENU==3:
            hold()
        elif MENU==4:
            hold()
        elif MENU==5:
            hold()
        elif MENU==6:
            hold()
        elif MENU==7:
            hold()
        elif MENU==8:
            hold()
        elif MENU==9:
            hold()
        elif MENU==10:
            hold()
        elif MENU==11:
            hold()
        elif MENU==12:
            hold()
        elif MENU==13:
            hold()
        elif MENU==14:
            hold()
        else:
            MENU=0
    # End of the developerInfo function

# Call the main function.
if __name__ == '__main__':
    main()