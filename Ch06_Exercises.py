# Michael Villarreal
# COSC-1336
# ACC
#

# Main menu system
def main():
    print('')
    MENU=1
    while MENU > 0 and MENU <= 26:
        print('[1]\t File Display')
        print('[2]\t File Head Display')
        print('[3]\t Line Numbers')
        print('[4]\t Item Counter')
        print('[5]\t Sum of Numbers')
        print('[6]\t Average of Numbers')
        print('[7]\t Random Number File Writer')
        print('[8]\t Random Number File Reader')
        print('[9]\t Exception Handing')
        print('[10]\t Golf Scores')
        print('[11]\t Personal Web Page Generator')
        print('[12]\t Average Steps Taken')
        print('...\tanything else to exit\n')
        MENU=get_int('Make a selection to continue')
        if MENU==1:
            file_display()
        elif MENU==2:
            file_head_display()
        elif MENU==3:
            line_numbers()
        elif MENU==4:
            item_counter()
        elif MENU==5:
            sum_of_numbers()
        elif MENU==6:
            avg_numbers()
        elif MENU==7:
            random_num_file_writer()
        elif MENU==8:
            random_num_file_reader()
        elif MENU==9:
            excep_hand()
        elif MENU==10:
            golf_scores()
        elif MENU==11:
            per_web_gen()
        elif MENU==12:
            avg_steps_taken()
        else:
            MENU=0

# Chapter 6 - Algorithm Workbench AW1-AW10
# Write a program that opens an output file with the filename my_name.txt, 
# writes your name to the file, then closes the file.
def AW1():
    fileout=open('my_name.txt','w')
    fileout.write('Michael\n')
    fileout.close()

# Write a program that opens the my_name.txt file that was created by the program 
# in problem 1, reads your name from the file, displays the name on the screen, 
# then closes the file.
def AW2():
    filein=open('my_name.txt','r')
    message=filein.read()
    print(message)
    input('hold...')
    filein.close()

# Write code that does the following: opens an output file with the filename 
# number_list.txt, uses a loop to write the numbers 1 through 100 to the file, 
# then closes the file.
def AW3():
    fileout=open('number_list.txt','w')
    for k in range(1,101):
        fileout.writelines(f'{str(k)}\n')
    fileout.close()

# Write code that does the following: opens the number_list.txt file that was 
# created by the code you wrote in question 3, reads all of the numbers from 
# the file and displays them, then closes the file.
def AW4():
    filein=open('number_list.txt','r')
    for k in filein:
        print(k.rstrip('\n'))
    filein.close()
    input('hold...')

# Modify the code that you wrote in problem 4 so it adds all of the numbers 
# read from the file and displays their total.
def AW5():
    filein=open('number_list.txt','r')
    s=0
    for k in filein:
        s+=int(k.rstrip('\n'))
    filein.close()
    print(s)
    input('hold...')

# Write code that opens an output file with the filename number_list.txt, 
# but does not erase the file’s contents if it already exists.
def AW6():
    fileout=open('number_list.txt','a')
    fileout.close()
    input('hold...')

# A file exists on the disk named students.txt. The file contains several 
# records, and each record contains two fields: (1) the student’s name, and 
# (2) the student’s score for the final exam. Write code that deletes the 
# record containing “John Perz” as the student name.
def AW7():
    filein=open('students.txt','r')
    fileout=open('students.tmp','w')
    for record in filein:
        record=record.rstrip('\n')
        if 'John Perz' in record:
            print('>'+record)
        else:
            print(record)
            fileout.write(f'{record}\n')
    filein.close()
    fileout.close()
    input('hold...')

# A file exists on the disk named students.txt. The file contains several records, 
# and each record contains two fields: (1) the student’s name, and (2) the student’s 
# score for the final exam. Write code that changes Julie Milan’s score to 100.
def AW8():
    filein=open('students.txt','r')
    fileout=open('students.tmp','w')
    for record in filein:
        record=record.rstrip('\n')
        if 'Julie Milan' in record:
            print('>'+record)
            fileout.write(f'Julie Milan, 100\n')
        else:
            print(record)
            fileout.write(f'{record}\n')
    filein.close()
    fileout.close()
    input('hold...')

# What will the following code display?
def AW9():
    try:
        x = float('abc123')
        print('The conversion is complete.')
    except IOError:
        print('This code caused an IOError.')
    except ValueError:
        print('This code caused a ValueError.')
    print('The end.')

# What will the following code display?
def AW10():
    try:
        x = float('abc123')
        print(x)
    except IOError:
        print('This code caused an IOError.')
    except ZeroDivisionError:
        print('This code caused a ZeroDivisionError.')
    except:
        print('An error happened.')
    print('The end.')

# Hold to review output
def hold():
    hd=input('\n\n\nPress [ENTER] to continue...')

# n spaces
def spaces(how_many):
    if how_many=='':
        print()
    else:
        for x in range(how_many):
            print()

def get_int(text):
    x=input(f'{text} :')
    if x=='':
        return 0
    else:
        return(int(x))

# 1 File Display
# Assume a file containing a series of integers is named numbers. txt and 
# exists on the computer's disk.
# Write a program that displays all of the numbers in the file. 
def file_display():
    infile=open('number_list.txt','r')
    for record in infile:
        print(record.rstrip('\n'))
    infile.close()
    hold()

# 2 File Head Display
# Write a program that asks the user for the name of a file. The program 
# should display only the first five lines of the file's contents. If the 
# file contains less than five lines, it should display the file's entire contents.
def file_head_display():
    # variables
    file_name=''
    try:
        spaces(3)
        file_name=input('Enter a file to display: ')
        infile=open(file_name,'r')
        k=0
        while k < 5:
            print(infile.readline().rstrip('\n'))
            k+=1
        hold()
    except Exception as err:
        print(err)
        hold()
    infile.close()

# 3 Line Numbers
# Write a program that asks the user for the name of a file. The program should 
# display the contents of the file with each line preceded with a line number 
# followed by a colon. The line numbering should start at 1.
def line_numbers():
    # variables
    file_name=''
    ln=1
    try:
        spaces(3)
        file_name=input('Enter a file to display: ')
        infile=open(file_name,'r')
        for record in infile:
            record=record.rstrip('\n')
            print(f'{ln}: {record}')
            ln+=1
        hold()
    except Exception as err:
        print(err)
        hold()
    infile.close()

# 4 Item Counter
# Assume a file containing a series of names (as strings) is named names. txt and exists on the computer's
# disk. Write a program that displays the number of names that are stored in the file. (Hint: Open the file and
# read every string stored in it. Use a variable to keep a count of the number of items that are read from the
# file.)
def item_counter():
    # variables
    file_name='students_2.txt'
    ln=0
    try:
        spaces(3)
        infile=open(file_name,'r')
        record=infile.readline().rstrip('\n')
        while record != '':
            ln+=1
            record=infile.readline()
        print(f'Total of {ln} records.')
        hold()
    except Exception as err:
        print(err)
        hold()
    infile.close()

# 5 Sum of Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# Write a program that reads all of the numbers stored in the file and calculates their total.
def sum_of_numbers():
    # variables
    file_name='number_list.txt'
    s=0
    try:
        spaces(3)
        infile=open(file_name,'r')
        for records in infile:
            s+=int(records)
        print(f'Summary of all the numbers is: {s}')
        hold()
    except Exception as err:
        print(err)
        hold()
    infile.close()

# 6 Average of Numbers
# Assume a file containing a series of integers is named numbers. txt and exists on the computer's disk.
# Write a program that calculates the average of all the numbers stored in the file.
def avg_numbers():
    # variables
    file_name='number_list.txt'
    s=0
    ln=0
    try:
        spaces(3)
        infile=open(file_name,'r')
        for records in infile:
            s+=int(records)
            ln+=1
        print(f'The average of all the numbers is: {s/ln:,.2f}')
        # print(s,ln)
        hold()
    except Exception as err:
        print(err)
        hold()
    infile.close()

# 7 Random Number File Writer
# Write a program that writes a series of random numbers to a file. Each random number should be in the
# range of 1 through 500. The application should let the user specify how many random numbers the file will
# hold.
def random_num_file_writer():
    import random
    # variables
    count=0
    file_name='random_num.out'
    try:
        spaces(3)
        outfile=open(file_name,'w')
        count=int(input('How many integers are needed in file: '))
        for k in range(count):
            rand_int=random.randint(1,501)
            outfile.write(str(rand_int)+'\n')
    except Exception as err:
        print(err)
        hold()
    outfile.close()

# 8 Random Number File Reader
# This exercise assumes you have completed Programming Exercise 7 , Random Number File Writer.
# Write another program that reads the random numbers from the file, displays the numbers, then displays
# the following data:
# • The total of the numbers
# • The number of random numbers read from the file
def random_num_file_reader():
    # variables
    s=0
    count=0
    file_name='random_num.out'
    try:
        spaces(3)
        infile=open(file_name,'r')
        for records in infile:
            records=records.rstrip('\n')
            s+=int(records)
            count+=1
        print(f'Total of all {count} records is {s}.')
        hold()
    except Exception as err:
        print(err)
        hold()
    infile.close()

# 9 Exception Handing
# Modify the program that you wrote for Exercise 6 ! so it handles the following exceptions:
# • It should handle any 10Error exceptions that are raised when the file is opened and data is read from it.
# • It should handle any valueError exceptions that are raised when the items that are read from the file
# are converted to a number.
def excep_hand():
    # variables
    file_name='number_list.txt'
    # file_name='my_name.txt'
    s=0
    ln=0
    try:
        spaces(3)
        infile=open(file_name,'r')
        for records in infile:
            s+=int(records)
            ln+=1
        print(f'The average of all the numbers is: {s/ln:,.2f}')
        # print(s,ln)
        hold()
    except IOError as err:
        print(f'IOError: {err}')
    except ValueError as err:
        print(f'ValueError: {err}')
    except Exception as err:
        print(err)
    hold()
    infile.close()

# 10 Golf Scores
# The Springfork Amateur Golf Club has a tournament every weekend. The club president has asked 
# you to write two programs:
# A. A program that will read each player's name and golf score as keyboard input, then save 
# these as records in a file named golf.txt. (Each record will have a field for the player's 
# name and a field for the player's score.)
# B. A program that reads the records from the golf.txt file and displays them.
def golf_scores_in(file_name):
    # variables
    name=''
    score=0
    try:
        outfile=open(file_name,'a')
        spaces(1)
        print('[leave blank to cancel]')
        name=input(f'Enter player name: ')
        if name=='':
            outfile.close()
            return()
        score=input(f'Enter {name}\'s score: ')
        outfile.write(f'{name},{score}\n')
    except Exception as err:
        print(err)
        hold()
    outfile.close()


def golf_scores_out(file_name):
    # variables
    line=['']
    try:
        infile=open(file_name,'r')
        for records in infile:
            records=records.rstrip('\n')
            line=records.rstrip('\n').split(',')
            print(f'{line[0]:.<15}{line[1]:.>5}')
    except Exception as err:
        print(err)
        hold()
    infile.close()

def golf_scores():
    # variables
    menu=0
    file_name='golf.txt'

    try:
        spaces(3)
        while menu>=0 and menu<=2:
            menu=int(input('Enter desired task:\n1] input members\n2] display players\n::'))
            if menu==1:
                golf_scores_in(file_name)
            elif menu==2:
                golf_scores_out(file_name)
            else:
                return()
    except Exception as err:
        print(err)
    hold()

    menu

# 11 Personal Web Page Generator
# Write a program that asks the user for his or her name, then asks the user to enter a sentence that
# describes himself or herself. Here is an example of the program's screen:
# Enter your name: Julie Taylor [Enter]
# Describe yourself: I am a computer science major, a member of the Jazz club, and I hope to work as a mobile
# app developer after I graduate. [Enter]
# Once the user has entered the requested input, the program should create an HTML file, containing the
# input, for a simple Web page. Here is an example of the HTML content, using the sample input previously
# shown:
        # <html>
        # <head>
        # </head>
        # <body>
        # <center>
        # <h1>Julie Taylor</h1>
        # ≤/center>
        # <hr />
        # I am a computer science major, a member of the Jazz club,
        # and I hope to work as a mobile app developer after I graduate.
        # <hr />
        # </body>
        # </html>
def per_web_gen():
    # variables
    file_template='www_template.html'
    file_name=''
    name=''
    description=''

    try:
        spaces(3)
        name=input('Enter your name: ')
        no_spaces=name.replace(' ','')
        description=input('Describe yourself: ')
        file_name=(f'www_{no_spaces}.html')
        infile=open(file_template)
        outfile=open(file_name,'w')
        for lines in infile:
            lines=lines.rstrip('\n')
            if '[NAME]' in lines:
                # print(f'Yes: {lines}')
                new_line=lines.replace('[NAME]',name)
                outfile.write(f'{new_line}\n')
            elif '[DESCRIPTION]' in lines:
                # print(f'Yes: {lines}')
                new_line=lines.replace('[DESCRIPTION]',description)
                outfile.write(f'{new_line}\n')
            else:
                # print(f'No: {lines}')
                outfile.write(f'{lines}\n')
        infile.close()
        outfile.close()
    except Exception as err:
        print(err)
        hold()
    infile.close()
    outfile.close()

# 12 Average Steps Taken
# A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories burned, heart
# rate, sleeping patterns, and so on. One common physical activity that most of these devices track is the
# number of steps you take each day.
# If you have downloaded this book's source code from the Computer Science Portal, you will find a file
# named steps.txt in the Chapter 06 ! folder. (The Computer Science Portal can be found at
# www.pearsonhighered.com/gaddis.) The steps.txt file contains the number of steps a person has
# taken each day for a year. There are 365 lines in the file, and each line contains the number of steps taken
# during a day. (The first line is the number of steps taken on January 1st, the second line is the number of
# steps taken on January 2nd, and so forth.) Write a program that reads the file, then displays the average
# number of steps taken for each month. (The data is from a year that was not a leap year, so February has
# 28 days.)
def avg_steps_taken():
    # variables
    file_name='steps.txt'
    steps=[0]*365
    avg_per_month=[0.0]*12
    days_per_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    try:
        infile=open(file_name,'r')
        for k in range(12):
            k2=0
            for k1 in range(days_per_month[k]):
                k2+=int(infile.readline().rstrip('\n'))
                avg_per_month[k]=int(k2/days_per_month[k])
            print(months[k], days_per_month[k], avg_per_month[k])
    except Exception as err:
        print(err)
    input('hold...')
    infile.close()

# Execution of program
main()