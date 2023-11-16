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
    # end of cap_quiz_key function
        
def capital_quiz():
    import random
    response_correct=0
    response_incorrect=0

    quiz_key=cap_quiz_key()

    is_testing=True
    while is_testing:
        question=random.choice(list(quiz_key.keys()))
        response=get_str(f'What is the capital of {question}')
        if response == 0:
            is_testing=False
            break
        answer=quiz_key.pop(question)

        # Evaluate response
        if response.lower()==answer.lower():
            response_correct+=1
            print('\tCorrect: ',end='')
        else:
            response_incorrect+=1
            print('\tIncorrect: ',end='')
        print(f'The capital of {question} is {answer}.')
        spaces(2)

    print(f'Final grade: {int(response_correct/(response_correct+response_incorrect)*100)}% or {response_correct}/{response_correct+response_incorrect}')
    spaces(2)

    hold()
    # end of capital_quiz function

# 3
# File Encryption and Decryption
# Write a program that uses a dictionary to assign "codes" to each letter of the alphabet. For example:
# codes = { 'A' : '8', 'a' : '9', 'B' : '@', 'b' : '#', etc. • •}
# Using this example, the letter A would be assigned the symbol 8, the letter a would be assigned the number 9, the letter в would be
# assigned the symbol & , and so forth.
# The program should open a specified text file, read its contents, then use the dictionary to write an encrypted version of the file's
# contents to a second file. Each character in the second file should contain the code for the corresponding character in the first file.
# Write a second program that opens an encrypted file and displays its decrypted contents on the screen.
def process_message(message,crypt_key):
    processed=''
    for k in message:
        processed+=crypt_key[k]
    return(processed)
    # end of process_message function

def encryption_decryption():
    # To generate a simple key pair for encryption with a 1-to-1 mapping for all ASCII characters, 
    # we will create a pair of dictionaries: one for encryption and one for decryption.
    # ASCII characters range from 0 to 127.

    # Creating the encryption and decryption key pairs
    encryption_key = {chr(i): chr((i + 1) % 128) for i in range(128)}  # Shift each character by 1
    decryption_key = {v:k for (k,v) in encryption_key.items()}

    # local variables
    input_file='secret_see.txt'
    output_file='secret_hide.txt'
    in_file=open(input_file,'r')
    message=''

    # open file and process the encryption    
    for line in in_file:
        scrambled=process_message(line,encryption_key)
        unscrambled=process_message(scrambled,decryption_key)
        message+=scrambled

    # write output to file
    out_file=open(output_file,'w')
    out_file.write(message)

    # close files
    in_file.close()
    out_file.close()

    # open encrypted file
    in_file=open(output_file,'r')
    message=''
    for line in in_file:
        unscrambled=process_message(line,decryption_key)
        message+=unscrambled
    # close files
    in_file.close()
    # display unencrypted message
    print(message)
    spaces(3)
    hold()
    # end of encryption_decryption function

# 4
# Unique Words
# Write a program that opens a specified text file then displays a list of all the unique words found in the file.
# Hint: Store each word as an element of a set.
def unique_words():
    # local variables
    input_file='secret_see.txt'
    myset=set()
    temp_data=[]


    # read file and build set
    in_file=open(input_file,'r')
    for line in in_file:
        temp_data=line.lower().strip().replace('.','').replace(',','').split(' ')
        myset.update(temp_data)
    # print(sorted(myset))
    for k in sorted(myset):
        print(k)
    hold()

# 5
# Word Frequency
# Write a program that reads the contents of a text file. The program should create a
# dictionary in which the keys are the individual words found in the file and the values
# are the number of times each word appears. For example, if the word "the" appears 128 times, 
# the dictionary would contain an element with 'the' as the key and 128
# as the value. The program should either display the frequency of each word or create
# a second file containing a list of each word and its frequency.
def word_frequency():
    #local variables
    input_file='secret_see.txt'
    temp_set=set()
    temp_list=[]
    temp_dict={}

    # method
    # 1-create set of initial words
    # 2-create dictionary with words and set counters to 0
    # 3-process the file data and increment counts
    # 4-generate output file

    # 1-create set of initial words
    source_file=open(input_file,'r')
    for k1 in source_file:
        k2=k1.strip().replace('.','').replace(',','').replace('?','').lower().split(' ')
        temp_list+=k2
        temp_set.update(k2)

    # 2-create dictionary with words and set counters to 0
    for k1 in temp_set:
        temp_dict[k1]=0

    # 3-process the file data and increment counts
    for k1 in temp_list:
        temp_dict[k1]+=1

    # 4-generate output file
    col=5
    wid=15
    count=0
    for k1 in sorted(temp_dict):
        print(f'{k1}:{temp_dict[k1]:<{wid-len(k1)}}',end='')
        if count>=col:
            print('\n')
            count=0
        count+=1
    hold()

# 6
# File Analysis
# Write a program that reads the contents of two text files and compares them in the
# following ways:
# • It should display a list of all the unique words contained in both files. • It should display a list of the words that appear in both files.
# • It should display a list of the words that appear in the first file but not the second. • It should display a list of the words that appear in the second file but not the first.
# • It should display a list of the words that appear in either the first or second file, but not both.
# Hint: Use set operations to perform these analyses.
def file_analysis():
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
        print('[1]\t Course information')
        print('[2]\t Capital Quiz')
        print('[3]\t File Encryption and Decryption')
        print('[4]\t Unique Words')
        print('[5]\t Word Frequency')
        print('[6]\t File Analysis')
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
            encryption_decryption()
        elif MENU==4:
            unique_words()
        elif MENU==5:
            word_frequency()
        elif MENU==6:
            file_analysis()
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