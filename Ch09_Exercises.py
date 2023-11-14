#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         [xxx]
#  File Name:         Ch09_Exercises.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          [xx-xx-xxxx]
#  Instructor:        Onabajo
#  Chapter:           <Chapter 9>
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
    x=input(f'{text}: ')
    if x=='':
        return 0
    else:
        return(int(x))
    # End of the get_int function

#***************************************************************
#  Function:     get_str
#  Description:  Request numeric input from user. Any number not
#   an integer will be returned as a 0. Useful for menu prompts
#   to cancel loop verses exception error.
#  Parameters:   Text string will be used as user prompt + ": "
#  Returns:      integer or 0 if not an integer
#**************************************************************
def get_str(text):
    x=input(f'{text}: ')
    if x=='':
        return 0
    else:
        return(x)
    # End of the get_str function

# 1
# Course information
# Write a program that creates a dictionary containing course numbers and the room numbers of the 
# rooms where the courses meet. The dictionary should have the following key-value pairs:
# The program should also create a dictionary containing course numbers and the names of the instructors 
# that teach each course. The dictionary should have the following key-value pairs:
# The program should also create a dictionary containing course numbers and the meeting times of 
# each course. The dictionary should have the following key-value pairs:
# The program should let the user enter a course number, then it should display the course's 
# room number, instructor, and meeting time.
def course_info():
    room={'CS101':3004, 'CS102':4501,'CS103':6755,'NT110':1244,'CM241':1411}
    instructor={'CS101':'Haynes', 'CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    time={'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}

    while True:
        course=get_str('Enter a course number to see course details')
        if course==0:
            break
        else:
            spaces(3)
            print(f'Course:\t')
            print(f'Room:\t{room.get(course,"TBD")}')
            print(f'Inst:\t{instructor.get(course,"TBD")}')
            print(f'Time:\t{time.get(course,"TBD")}')
            spaces(2)
    # End of the course_info function

# 2
# Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values. 
# (Use the Internet to get a list of the states and their capitals.) The program should then randomly quiz 
# the user by displaying the name of a state and asking the user to enter that state's capital. The program 
# should keep a count of the number of correct and incorrect responses. (As an alternative to the U.S. states, 
# the program can use the names of countries and their capitals.)
def cap_quiz_key():
    cap_quiz={}
    file='us-state-capitals.csv'
    in_file=open(file,'r')
    for k in in_file:
        record=k.strip().split(',')
        cap_quiz[record[0]]=record[1]
    in_file.close()
    cap_quiz.pop('name')
    return(cap_quiz)
        
# def q_n_a():
#     q,a = 

def capital_quiz():
    quiz_key=cap_quiz_key()

    while True:
        q,a=quiz_key.


    # print(quiz_key)
    hold()

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
        print('[1]\t Course information')
        print('[2]\t Capital Quiz')
        print('[3]\t xx')
        print('[4]\t xx')
        print('[5]\t xx')
        print('[6]\t xx')
        print('[7]\t xx')
        print('[8]\t xx')
        print('[9]\t xx')
        print('[10]\t xx')
        print('...\tanything else to exit\n')
        MENU=get_int('Make a selection to continue')
        if MENU==1:
            course_info()
        elif MENU==2:
            capital_quiz()
        elif MENU==3:
            developerInfo('Chapter 9')
        elif MENU==4:
            developerInfo('Chapter 9')
        elif MENU==5:
            developerInfo('Chapter 9')
        elif MENU==6:
            developerInfo('Chapter 9')
        elif MENU==7:
            developerInfo('Chapter 9')
        elif MENU==8:
            developerInfo('Chapter 9')
        elif MENU==9:
            developerInfo('Chapter 9')
        elif MENU==10:
            developerInfo('Chapter 9')
        else:
            MENU=0
    # End of the developerInfo function

# Call the main function.
if __name__ == '__main__':
    main()