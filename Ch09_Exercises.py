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
        return '0'
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
# • It should display a list of all the unique words contained in both files.
# • It should display a list of the words that appear in both files.
# • It should display a list of the words that appear in the first file but not the second.
# • It should display a list of the words that appear in the second file but not the first.
# • It should display a list of the words that appear in either the first or second file, but not both.
# Hint: Use set operations to perform these analyses.
def set2screen(the_set,title):
    # the_set=set to be processed
    # local variables
    screen=75   # width of display screen
    wid=0       # width of widest word
    col=0       # number of columns
    report=''   # report
    k=1         # loop counter
    
    # loop to calculate widest word in set
    for k1 in the_set:
        k2=str(k1)
        if len(k2)>wid:
            wid=len(k2)
    wid+=1

    # calculate how many columns will be needed
    col=screen//wid

    # generate the report
    screen=col * wid
    report+=(f'{title:-^{screen}}\n')
    for k1 in the_set:
        report+=(f'{k1:^{wid}}')
        if k<col:
            k+=1
        else:
            k=1
            report+=('\n')
    spaces(2)
    print(report)
    spaces(3)
    hold()
    return(report)

def from_file_to_set(file):
    # file=input file to be ingested
    # returns unique words from file
    # local variables
    temp_set=set()
    # open file
    infile=open(file,'r')

    for k1 in infile:
        k2=k1.replace('.','').replace(',','').replace('?','').lower().strip().split(' ')
        if len(k2)>1:
            temp_set.update(k2)
    # close file
    infile.close()
    # return set
    return(temp_set)

def the_union(set1,set2):
    # set1,set2 = sets to compare
    temp_set=set()

    # method 1
    temp_set=set1.union(set2)
    # method 2
    temp_set=set1|set2
    return(temp_set)

def the_differences(set1,set2):
    # set1,set2 = sets to compare
    temp_set=set()

    # method 1
    temp_set=set1.difference(set2)
    # method 2
    temp_set=set1-set2
    return(temp_set)

def the_sym_diff(set1,set2):
    # set1,set2 = sets to compare
    temp_set=set()

    # method 1
    temp_set=set1.symmetric_difference(set2)
    # method 2
    temp_set=set1^set2
    return(temp_set)

def file_analysis():
    # steps needed
    #x0-function to diaplay a list words in columns
    #x1-create 2 files
    # 2-function file_2_set call to process each file and populate a set
    # 3-function compare [union]
    # 4-function compare [difference x2]
    # 5-function compare [symmetric difference]

    # local variables
    file1='story_1.txt'
    file2='story_2.txt'
    file1_set=set()
    file2_set=set()

    # 2-function from_file_to_set call to process each file and populate a set
    file1_set=from_file_to_set(file1)
    file2_set=from_file_to_set(file2)

    set2screen(file1_set,'Story 1')
    set2screen(file2_set,'Story 2')

    # 3-function compare [union]
    union_set=the_union(file1_set,file2_set)
    set2screen(union_set,'Words that appear in both stories')

    # 4-function compare [difference x2]
    diff_1to2_set=the_differences(file1_set,file2_set)
    diff_2to1_set=the_differences(file2_set,file1_set)

    set2screen(diff_1to2_set,'Words that appear in story 1 but not 2')
    set2screen(diff_2to1_set,'Words that appear in story 2 but not 1')

    # 5-function compare [symmetric difference]
    sym_diff_set=the_sym_diff(file1_set,file2_set)

    set2screen(sym_diff_set,'Words that appear in either story, but not both')
    
# 7
# World Series Winners
# In this chapter's source code folder (available on the Computer Science Portal at www.pearsonhighered.com/gaddis), you will find a
# text file named WorldSeriesWinners. txt. This file contains a chronological list of the World Series' winning teams from 1903 through
# 2009. The first line in the file is the name of the team that won in 1903, and the last line is the name of the team that won in 2009. (Note
# the World Series was not played in 1904 or 1994. There are entries in the file indicating this.)
# Write a program that reads this file and creates a dictionary in which the keys are the names of the teams, and each key's associated
# value is the number of times the team has won the World Series. The program should also create a dictionary in which the keys are the
# years, and each key's associated value is the name of the team that won that year.
# The program should prompt the user for a year in the range of 1903 through 2009. It should then display the name of the team that won
# the World Series that year, and the number of times that team has won the World Series.
def from_file_to_list(file):
    # return list contents of file
    # local variables
    temp_set=set()
    temp_list=[]
    infile=open(file,'r')

    for k1 in infile:
        k2=k1.strip()
        temp_list.append(k2)
    infile.close()
    return(temp_list)

def count_wins(the_list):
    # return dictionary team:total wins
    # local variables
    temp_set=set(the_list)
    temp_dict={}

    for k1 in temp_set:
        temp_dict[k1]=0
    
    for k1 in the_list:
        temp_dict[k1]+=1
    
    return(temp_dict)

def ws_winners(the_list):
    # return dictionary year:team
    # local variables
    year=1903
    temp_dict={}

    for k1 in the_list:
        temp_dict[year]=k1
        year+=1
    
    return(temp_dict)

def world_series_winners():
    # 0-read file and create a temp list
    # 1-dictionary team:total wins
    # 2-dictionary year:team
    # 3-prompt for year return year-team-total wins
    # local variables
    dict_team={}
    dict_year={}
    data_file='WorldSeriesWinners.txt'
    list_winners=[]

    # 0-read file and create a temp list
    list_winners=from_file_to_list(data_file)

    # 1-dictionary team:total wins
    dict_team=count_wins(list_winners)

    # 2-dictionary year:team
    dict_year=ws_winners(list_winners)

    # 3-prompt for year return year-team-total wins
    while True:
        spaces(3)
        yr_selected=get_int('Enter a year between 1903 to 2008')
        if yr_selected in dict_year:
            tmp_winner=dict_year[yr_selected]
            tmp_total=dict_team[tmp_winner]
            if 'Not Played' not in tmp_winner:
                print(f'For {yr_selected}, ', end='')

            print(f'{tmp_winner}', end='')

            if 'Not Played' not in tmp_winner:
                print(f'{tmp_total}', end='')

            print('\n')
                
        elif yr_selected==0:
            break
        else:
            print('Check your input.\n')
    hold()

# 8
# Name and Email Addresses
# Write a program that keeps names and email addresses in a dictionary as key-value pairs. The program should display a menu that lets
# the user look up a person's email address, add a new name and email address, change an existing email address, and delete an existing
# name and email address. The program should pickle the dictionary and save it to a file when the user exits the program. Each time the
# program starts, it should retrieve the dictionary from the file and unpickle it.
def menu():
    # display a menu of options
    spaces(3)
    menu_items=['(1) Display all names and email adresses',
                '(2) Look up an email address',
                '(3) Add a new name and email address',
                '(4) Update an existing email address',
                '(5) Delete a name and email address',
                '(0) to Exit']
    # display menu
    for k1 in menu_items:
        print(k1)
    spaces(1)

def display_contacts(dict_list):
    # display content of dictionary in two columns
    # print(f'display contact: {dict_list}')
    # hold()
    for k1 in sorted(dict_list):
        print(f'{k1:.<25}.{dict_list[k1]:.>25}')
    # end of display_contacs function

def find_contact(dict_list):
    # search and display contact
    # local variables
    temp_list={}
    for k1 in dict_list:
        temp_list[k1]=dict_list[k1].lower()
    
    while True:
        spaces(2)
        temp_name=get_str('Enter the name')
        if temp_name.lower() in temp_list:
            print(f'\t\t{temp_list[k1]}')
        elif temp_name=='0':
            break
        else:
            print('\t\tnot found')
    # end of find_contact function

def add_contact(temp_dict):
    # temp dict to be merged in next step
    # temp_dict={}
    temp_name=''
    temp_email=''

    in_loop=True
    while in_loop:
        spaces(2)
        print('Leave blank to cancel.')
        temp_name=get_str('Enter the name')
        temp_email=get_str('Enter the email address')
        if temp_name=='0':
            in_loop=False
        elif temp_email=='0':
            in_loop=False
        else:
            temp_dict[temp_name]=temp_email
        temp_name=''
        temp_email=''

    return(temp_dict)
    # end of add_contact function

def save_binary(file,dict):
    import pickle
    # file=contacts_file
    # dict=dictionary with contacts
    outfile=open(file,'wb')
    pickle.dump(dict,outfile)
    outfile.close()

def delete_contact(temp_dict):
    # temp dict to be merged in next step
    # temp_dict={}
    temp_name=''

    in_loop=True
    while in_loop:
        spaces(2)
        print('Leave blank to cancel.')
        temp_name=get_str('Enter the name')
        if temp_name=='0':
            in_loop=False
        else:
            temp_dict.pop(temp_name,'Name not found')
        temp_name=''

    return(temp_dict)
    # end of delete_contact function

def name_email():
    # 0-generate a binary file
    # import module
    import pickle

    # local variables
    contacts={}
    contacts_file='contacts.bin'

    # load contacts from storage
    try:
        infile=open(contacts_file,'rb')
        contacts=pickle.load(infile)
        infile.close()
    except FileNotFoundError as Err:
        save_binary(contacts_file,contacts)
        print(f'The file [{contacts_file}] does not exist.  A new one will be created.')

    print('menu loop start')
    menu()
    while True:
        menu()
        selection=get_int('Make a selection')
        if selection==0:
            break
        elif selection==1:
            display_contacts(contacts)
        elif selection==2:
            find_contact(contacts)
        elif selection==3:
            contacts=add_contact(contacts)
            save_binary(contacts_file,contacts)
        elif selection==4:
            display_contacts(contacts)
            contacts=add_contact(contacts)
            save_binary(contacts_file,contacts)
        elif selection==5:
            display_contacts(contacts)
            contacts=delete_contact(contacts)
            save_binary(contacts_file,contacts)
        else:
            print('Enter a valid selection.')

    # display_contacts(contacts)

    # hold()
    
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
        print('[7]\t World Series Winners')
        print('[8]\t Name and Email Addresses')
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
            world_series_winners()
        elif MENU==8:
            name_email()
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