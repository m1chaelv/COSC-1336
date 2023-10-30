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
    try:
        if x=='':
            return(0)
        else:
            return(int(x))
    except Exception as err:
        print(err)
        return(0)
    # End of the get_int function

# 1 Initials
# Write a program that gets a string containing a person's first, middle, and last names, and displays their
# first, middle, and last initials. For example, if the user enters John William Smith, the program should display J. W. S.
def initials():
    i_words=[]
    i_init=''
    full_name=input('Enter your full name: ')
    
    i_words=full_name.split(' ')
    for k1 in i_words:
        i_init+=k1[0].upper()+'. '
    i_init=i_init[:-1]
    print(i_init)
    hold()

# 2 Sum of Digits in a String
# Write a program that asks the user to enter a series of single-digit numbers with nothing separating them.
# The program should display the sum of all the single digit numbers in the string. For example, if the user
# enters 2514, the method should return 12, which is the sum of 2, 5, 1, and 4.
def sum_of_digits():
    sod_sum=0
    sod_input=get_int('Enter a series of single-digit numbers')
    for k1 in str(sod_input):
        sod_sum+=int(k1)
    print(sod_sum)
    hold()
    # end of the sum_of_digits function

# 3 Date Printer
# Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It should print
# the date in the format March 12, 2018.
def date_printer():
    dp_split=[]
    dp_date=''
    dp_mm=('','January','February','March','April','May','June','July','August','September','October','November','December')

    dp_input=input('Enter a date in the following format mm/dd/yyyy: ')
    dp_split=dp_input.split('/')
    dp_date=dp_mm[int(dp_split[0])]+' '+str(int(dp_split[1]))+', '+str(int(dp_split[2]))
    print(dp_date)
    hold()

# 4 Morse Code Converter
# Morse code is a code where each letter of the English alphabet, each digit, and various punctuation
# characters are represented by a series of dots and dashes. Table 8-4 " shows part of the code.
# Write a program that asks the user to enter a string, then converts that string to Morse code.
# Table 8-4 Morse code
def morse_code_keygen():
    mc_val=['-','.']
    mc_char=6
    mc_char_done=0
    mc_codes=[]

    for k1 in (mc_val):
        mc_codes.append(k1)
    #mc_char_done=1
    mc_char_done+=1

    while mc_char>mc_char_done:
        mc_temp=[]
        for k1 in mc_codes:
            if len(k1)>=mc_char_done:
                for k2 in mc_val:
                    mc_temp.append(f'{k1}{k2}')
        for k1 in mc_temp:
            mc_codes.append(k1)
        mc_char_done+=1

    outfile=open('Ch08.out','w')
    for k1 in (mc_codes):
        outfile.write(k1+'\n')
    outfile.close()

def loaddata(infile,x):
    file=open(infile,'r')
    templist=file.readline().strip().split('::')
    while templist[0]!='':
        x.append(templist)
        templist=file.readline().strip().split('::')
    file.close()
    return(x)

def mc_lookup(list,key,pos,ans):
    # list=master file with converstions
    # key=entry to lookup
    # pos=position of key
    # ans=position of answer
    key=key.lower()
    for k1 in list:
        if key.lower()==k1[pos].lower():
            return(k1[ans])


def morse_code():
    mc_codes=[]
    mc_file='Ch08.txt'
    mc_codes=loaddata(mc_file,mc_codes)
    mc_answer=''

    spaces(3)
    mc_input=input('Enter text to convert to morse code: ')
    for k1 in mc_input:
        mc_answer+=(mc_lookup(mc_codes,k1,1,0)+' ')

    spaces(1)
    print(mc_answer)
    hold()

# 5 Alphabetic Telephone Number Translator
# Many companies use telephone numbers like 555-GET-
# FOOD so the number is easier for their customers to
# remember. On a standard telephone, the alphabetic letters
# are mapped to numbers in the following fashion:
# A, B, and C = 2
# D, E, and F = 3
# G, H, and I = 4
# J, K, and L = 5
# M, N, and 0 = 6
# P, Q, R, and S = 7
# T, U, and V = 8
# w, X, Y, and Z = 9
# Write a program that asks the user to enter a 10-character
# telephone number in the format XXX-XXX-XXXX. The
# application should display the telephone number with any
# alphabetic characters that appeared in the original translated
# to their numeric equivalent. For example, if the user enters
# 555-GET-FOOD, the application should display 555-438-3663.
def atn_load_master(infile):
    # infile name with master records
    x=[]
    file=open(infile,'r')
    templist=file.readline().strip('\n').split(',')
    while templist[0]!='':
        x.append(templist)
        templist=file.readline().strip('\n').split(',')
    file.close()
    return(x)


def alpha_tel_no():
    atn_file='Ch08_alpha_tel_no.txt'
    atn_master=atn_load_master(atn_file)
    atn_numeric_number=''

    spaces(3)
    atn_phone_number=input('Enter a text based phone number to convert to numeric phone number.\nFormat xxx-xxx-xxxx: ')
    for k1 in atn_phone_number:
        atn_numeric_number+=mc_lookup(atn_master,k1,0,1)
    spaces(2)
    print(atn_numeric_number)
    hold()

# 6 Average Number of Words
# If you have downloaded the source code from the Computer
# Science Portal you will find a file named text.txt in the
# Chapter 08 ! folder. The text that is in the file is stored as
# one sentence per line. Write a program that reads the file's
# contents and calculates the average number of words per
# sentence.
# You can access the Computer Science Portal at
# www.pearsonhighered.com/gaddis.)
def avg_num_of_words():
    anow_file='text.txt'
    anow_data=[]
    anow_count=[]
    anow_last_record=False
    anow_avg_count=0.0

    tempfile=open(anow_file,'r')
    anow_data=tempfile.readline().strip('\n').split(' ')
    # print(anow_data)
    # hold()
    while anow_last_record==False:
        anow_count.append(len(anow_data))
        anow_data=tempfile.readline().strip('\n').split(' ')
        if anow_data[0]=='':
            anow_last_record=True
        # else:
            # print(anow_data)
            # hold()
    for k1 in anow_count:
        anow_avg_count+=k1/len(anow_count)
    spaces(3)
    print(round(anow_avg_count,1),anow_count)
    hold()
    spaces(2)
    tempfile.close()

# 7 Character Analysis
# If you have downloaded the source code you will find a file
# named text.txt in the Chapter 08 " folder. Write a
# program that reads the file's contents and determines the
# following:
# • The number of uppercase letters in the file
# • The number of lowercase letters in the file
# • The number of digits in the file
# • The number of whitespace characters in the file
def char_analysis():
    ca_upper=ca_lower=ca_digit=ca_white=0
    ca_file='text.txt'
    tempfile=open(ca_file,'r')
    ca_data=tempfile.read().strip()
    print(ca_data)
    for k1 in ca_data:
        if k1==' ':
            ca_white+=1
        else:
            ca_digit+=1
            if k1.lower()!=k1.upper():
                if k1==k1.lower():
                    ca_lower+=1
                else:
                    ca_upper+=1
    spaces(3)
    print(f'The number of uppercase letters in the file: {ca_upper}')
    print(f'The number of lowercase letters in the file: {ca_lower}')
    print(f'The number of digits in the file: {ca_digit}')
    print(f'The number of whitespace characters in the file: {ca_white}')
    spaces(2)
    hold()

# 8 Sentence Capitalizer
# Write a program with a function that accepts a string as an
# argument and returns a copy of the string with the first
# character of each sentence capitalized. For instance, if the
# argument is "hello. my name is Joe. what is your name?" the
# function should return the string "Hello. My name is
# Joe. What is your name?" The program should let the
# user enter a string and then pass it to the function. The
# modified string should be displayed.
def sc_capitalizer(text):
    # text = paragraph to analyze and capitalize
    sc_punct=['.','?']
    sc_new_text=''
    sc_cap_next=True
    for k1 in text:
        if sc_cap_next==True:
            sc_new_text+=k1.upper()
            if k1!=' ':
                sc_cap_next=False
        else:
            sc_new_text+=k1
        if k1 in sc_punct:
            sc_cap_next=True
    return(sc_new_text)


def sent_cap():
    spaces(3)
    sc_input=input('Enter a paragraph to evaluate: ')
    spaces(2)
    print(sc_capitalizer(sc_input))
    hold()

# 9 Vowels and Consonants
# Write a program with a function that accepts a string as an
# argument and returns the number of vowels that the string
# contains. The application should have another function that
# accepts a string as an argument and returns the number of
# consonants that the string contains. The application should
# let the user enter a string, and should display the number of
# vowels and the number of consonants it contains.
def vnc_count_vowels(text):
    vnc_count=0
    vnc_letters='aeiou'
    for k1 in text:
        if k1.lower() in vnc_letters:
            vnc_count+=1
    return(vnc_count)

def vnc_count_consonants(text):
    vnc_count=0
    vnc_letters='bcdfghjklmnpqrstvwxyz'
    for k1 in text:
        if k1.lower() in vnc_letters:
            vnc_count+=1
    return(vnc_count)

def vowels_n_consonants():
    vnc_vowels=0
    vnc_consonants=0
    spaces(3)
    vnc_input=input('Enter some text to evaluate: ')
    vnc_vowels+=vnc_count_vowels(vnc_input)
    vnc_consonants+=vnc_count_consonants(vnc_input)
    print(f'The text entered contains {vnc_vowels} vowels & {vnc_consonants} consonants.')
    spaces(2)
    hold()

# 10 Most Frequent Character
# Write a program that lets the user enter a string and displays
# the character that appears most frequently in the string.
def mfc_prep(text):
    mfc_filtered_text=set(text)
    mfc_matrix=[]
    for k1 in mfc_filtered_text:
        mfc_matrix.append([k1,0])
    return(mfc_matrix)

def mfc_counter(text):
    mfc_matrix=mfc_prep(text)
    for k1 in text:
        for k2 in mfc_matrix:
            if k1==k2[0]:
                k2[1]+=1
    return(mfc_matrix)

def mfc_frequent(matrix,field):
    # matrix = to evaluate
    # field = to evaluate
    mfc_most_freq=[]
    mfc_list=[]
    for k1 in matrix:
        mfc_list.append(k1[1])   
    mfc_max=max(mfc_list)
    for k1 in matrix:
        if k1[field]==mfc_max:
            mfc_most_freq.append(k1[0])
    return(mfc_most_freq,mfc_max)

def most_freq_char():
    mfc_matrix=[]
    spaces(3)
    mfc_input=input('Enter some text to evaluate: ')
    mfc_matrix=mfc_counter(mfc_input.lower())
    mfc_most_freq=mfc_frequent(mfc_matrix,1)   

    spaces(2)
    print(f'final: {mfc_most_freq}')
    spaces(2)
    hold()

# 11 Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, but the first
# character of each word is uppercase. Convert the sentence to a string in which the words are separated by
# spaces, and only the first word starts with an uppercase letter. For example the string
# "StopAndSmellTheRoses." would be converted to "Stop and smell the roses."
def word_separator():
    ws_ignore=True
    ws_caps='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    spaces(3)
    ws_input=input('Enter text to be evaluated: ')
    ws_output=''

    for k1 in ws_input:
        if ws_ignore==True:
            ws_output+=k1
            ws_ignore=False
        else:
            if k1 not in ws_caps:
                ws_output+=k1
            else:
                ws_output+=(' '+k1.lower())
    
    spaces(2)
    print(ws_output)
    spaces(1)
    hold()

# 12 Pig Latin
# Write a program that accepts a sentence as input and converts each word to "Pig Latin." In one version, to 
# convert a word to Pig Latin, you remove the first letter and place that letter at the end of the word. Then, 
# you append the string "ay" to the word. Here is an example:
# English:      I SLEPT MOST OF THE NIGHT
# Pig Latin:    IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY
def pig_latin():
    spaces(3)
    pl_input=input('Enter text to be evaluated: ')
    pl_list=pl_input.upper().split(' ')
    pl_list_ay=[]
    pl_space=' '
    pl_output=''

    for k1 in pl_list:
        k2=k1[1:]+k1[:1]+'AY'
        pl_list_ay.append(k2)

    for k1 in pl_list_ay:
        pl_output=pl_space.join(pl_list_ay)

    spaces(2)
    print(pl_output)
    spaces(1)
    hold()

# 13 PowerBall Lottery
# To play the PowerBall lottery, you buy a ticket that has five numbers in the range of 1-69, and a
# "PowerBall" number in the range of 1-26. (You can pick the numbers yourself, or you can let the ticket
# machine randomly pick them for you.) Then, on a specified date, a winning set of numbers is randomly
# selected by a machine. If your first five numbers match the first five winning numbers in any order, and
# your PowerBall number matches the winning PowerBall number, then you win the jackpot, which is a very
# large amount of money. If your numbers match only some of the winning numbers, you win a lesser
# amount, depending on how many of the winning numbers you have matched.
# In the student sample programs for this book, you will find a file named pbnumbers.txt, containing the
# winning PowerBall numbers that were selected between February 3, 2010 and May 11, 2016 (the file
# contains 654 sets of winning numbers). Figure 8-7 I shows an example of the first few lines of the file's
# contents. Each line in the file contains the set of six numbers that were selected on a given date. The
# numbers are separated by a space, and the last number in each line is the PowerBall number for that day.
# For example, the first line in the file shows the numbers for February 3, 2010, which were 17, 22, 36, 37,
# 52, and the PowerBall number 24.
# Figure 8-7 The pbnumbers.txt file
# Write one or more programs that work with this file to perform the following:
# • Display the 10 most common numbers, ordered by frequency
# • Display the 10 least common numbers, ordered by frequency
# • Display the 10 most overdue numbers (numbers that haven't been drawn in a long time), ordered from
# most overdue to least overdue
# • Display the frequency of each number 1-69, and the frequency of each Powerball number 1-26
def pb_counter(matrix):
    pb_matrix=[]
    for k1 in range(min(matrix),max(matrix)+1):
        pb_matrix.append([k1,0])
    for k1 in matrix:
        pb_matrix[k1-1][1]+=1
    return(pb_matrix)

def pb_reset(matrix):
    for k1 in matrix:
        matrix[matrix.index(k1)]=[k1[0],0]
    return(matrix)
    
def pb_sort(matrix,key,rev):
    #key = index to sort by
    #rev = sort decending order
    # print(f'before sort: \n{matrix}')
    for k1 in matrix:
        index=matrix.index(k1)
        matrix[index].insert(0,k1[key])
    matrix.sort(reverse=rev)
    input(matrix)
    for k1 in matrix:
        index=matrix.index(k1)
        matrix[index].remove(k1[0])
    return(matrix)

def pb_top_x(matrix,how_many,key):
    #how_many = entries needed minimum
    #key = index of sort
    how_many-=1         #adjust for 0 offset
    list1=[]
    pb_10_count=0
    pb_10_done=False
    while pb_10_done==False:
        list1.append(matrix[pb_10_count])
        pb_10_count+=1
        if pb_10_count<=how_many:
            pb_10_done=False
        else:
            pb_10_done=True
            if matrix[how_many][key]==matrix[pb_10_count][key]:
                pb_10_done=False
    return(list1)

def pb_age(matrix,grp1,grp2):
    group1=[]+matrix[1]
    group2=[]+matrix[2]

    group1=pb_reset(group1)
    group2=pb_reset(group2)

    for k1 in matrix[0]:
        last_use=matrix[0].index(k1)
        for k2 in range(grp1):
            value=k1[k2]
            for k3 in group1:
                if k3[0]==value:
                    index=group1.index(k3)
            group1[index]=[value,last_use]
        for k3 in range(grp1,grp1+grp2):
            value=k1[k3]
            for k3 in group2:
                if k3[0]==value:
                    index=group2.index(k3)
            group2[index]=[value,last_use]
    # hold()

    # sort by last use. smaller are oldest
    group1=pb_sort(group1,1,False)
    group2=pb_sort(group2,1,False)

    #top 10 from pre-sorted list
    group1=pb_top_x(group1,10,1)
    group2=pb_top_x(group2,10,1)

    return(group1,group2)

def pb_loaddata(file,grp1,grp2):
    pb_data=[]
    pb_temp=[]
    Group1=[]
    Group2=[]
    Group1_count=[]
    Group2_count=[]
    pb_done=False
    tempfile=open(file,'r')
    
    while pb_done==False:
        pb_temp=tempfile.readline().strip().split(' ')
        if pb_temp[0]=='':
            pb_done=True
        else:
            k1=[]
            for k2 in pb_temp:
                k1.append(int(k2))
            pb_data.append(k1)

    tempfile.close()

    for k1 in pb_data:
        for k2 in range(grp1):
            Group1.append(k1[k2])
        for k2 in range(grp1,grp1+grp2):
            Group2.append(k1[k2])

    Group1_count=pb_counter(Group1)
    Group2_count=pb_counter(Group2)

    return(pb_data,Group1_count,Group2_count)

def pb_rmv_dupes(temp_list):
    k1=[]
    for k2 in temp_list:
        if k2 not in k1:
            k1.append(k2)
    return(k1)

def pb_10_list(matrix,list_sort):
    pb_values=[]
    pb_count=[]
    pb_top=10-1
    for k1 in matrix:
        pb_values.append(k1[0])
        pb_count.append(k1[1])
    
    if list_sort=='most':
        pb_count.sort(reverse=True)
        pb_sort=[]+pb_count
    elif list_sort=='least':
        pb_count.sort()
        pb_sort=[]+pb_count

    if list_sort=='frequency':
        matrix.sort()
        return(matrix)

    list1=[]+matrix
    list2=[]
    for k1 in pb_sort:
        for k2 in list1:
            if k2[1]==k1:
                index_old=list1.index(k2)
                list2.append(k2)
                list1.remove(k2)

    list1=[]
    pb_10_count=0
    pb_10_done=False
    while pb_10_done==False:
        list1.append(list2[pb_10_count])
        pb_10_count+=1
        if pb_10_count<=pb_top:
            pb_10_done=False
        else:
            pb_10_done=True
            if list2[pb_top][1]==list2[pb_10_count][1]:
                pb_10_done=False
    return(list1)

def power_ball():
    pb_infile='pbnumbers.txt'
    pb_data=[]
    pb_data=pb_loaddata(pb_infile,5,1)

    # print(pb_data[0])
    # print()
    # print(pb_data[1])
    # print()
    # print(pb_data[2])
    # print()
    
    # hold()

    spaces(3)
    print('Display the 10 most common numbers, ordered by frequency:')
    print(pb_10_list(pb_data[1],'most'))
    print(pb_10_list(pb_data[2],'most'))
    print('least lotto & powerball')
    print(pb_10_list(pb_data[1],'least'))
    print(pb_10_list(pb_data[2],'least'))
    print('frequency lotto & powerball')
    print(pb_10_list(pb_data[1],'frequency'))
    print(pb_10_list(pb_data[2],'frequency'))
    print('age lotto & powerball')
    aged_grp=pb_age(pb_data,5,1)
    print(f'overdue based on age for lotto numbers: {aged_grp[0]}')
    print(f'overdue based on age for powerball numbers: {aged_grp[1]}')

    hold()

# 14 Gas Prices
# In the student sample program files for this chapter, you will find a text file named GasPrices. txt. The file
# contains the weekly average prices for a gallon of gas in the United States, beginning on April 5th, 1993,
# and ending on August 26th, 2013. Figure 8-8 I shows an example of the first few lines of the file's contents:
# Figure 8-8 The GasPrices.txt file
        # 04-05-1993:1.068
        # 04-12-1993:1.079
        # 04-19-1993:1.079
        # 04-26-1993:1.086
# Figure 8-8 Full Alternative Text L
# Each line in the file contains the average price for a gallon of gas on a specific date. Each line is formatted
# in the following way:
# MM-DD-YYYY: Price
# MM is the two-digit month, dd is the two-digit day, and vyyy is the four-digit year. Price is the average
# price per gallon of gas on the specified date.
# For this assignment, you are to write one or more programs that read the contents of the file and perform
# the following calculations:

# Average Price Per Year: Calculate the average price of gas per year, for each year in the file. (The file's 
# data starts in April of 1993, and it ends in August 2013. Use the data that is present for the years 1993 and
# 2013.)

# Average Price Per Month: Calculate the average price for each month in the file.

# Highest and Lowest Prices Per Year: For each year in the file, determine the date and amount for the
# lowest price, and the highest price.

# List of Prices, Lowest to Highest: Generate a text file that lists the dates and prices, sorted from the
# lowest price to the highest.

# List of Prices, Highest to lowest: Generate a text file that lists the dates and prices, sorted from the
# highest price to the lowest.

# You can write one program to perform all of these calculations, or you can write different programs, one for
# each calculation.
def gp_loaddata(file):
    matrix=[]
    infile=open(file,'r')
    
    for k1 in infile:
        record=infile.readline().replace('-',':').strip().split(':')
        matrix.append(record)

    infile.close()
    return(matrix)

def gp_numeric(matrix):
    matrix2=[]
    for k1 in matrix:
        if k1[0].isdigit():
            k2=[]
            k2.append(int(k1[0]))
            k2.append(int(k1[1]))
            k2.append(int(k1[2]))
            k2.append(float(k1[3]))
            matrix2.append(k2)
    return(matrix2)

def gp_avg_ppm(matrix):
    gp_average=[]

    totals=[]
    for k1 in matrix:
        month=(f'{k1[0]:02}-{k1[2]}')
        year=k1[2]
        value=k1[3]

        found=False
        for k2 in totals:
            if k2[0]==month:
                k2[1]+=value
                k2[2]+=1
                found=True
                break
        if not found:
            totals.append([month,value,1])
    
    for k1 in totals:
        gp_average.append([k1[0],k1[1]/k1[2]])

    return(gp_average)

def gp_avg_ppy(matrix):
    gp_average=[]

    totals=[]
    for k1 in matrix:
        year=k1[2]
        value=k1[3]

        found=False
        for k2 in totals:
            if k2[0]==year:
                k2[1]+=value
                k2[2]+=1
                found=True
                break
        if not found:
            totals.append([year,value,1])
    
    for k1 in totals:
        gp_average.append([k1[0],k1[1]/k1[2]])

    return(gp_average)

def gp_highs_lows(matrix):
    totals=[]
    for k1 in matrix:
        year=k1[2]
        value=k1[3]

                                    # for k1 in matrix:
                                    #     index=matrix.index(k1)

        found=False
        for k2 in totals:
            if k2[0]==year:
                index=totals.index(k2)
                # print(in)
                if k2[1]>value:
                    totals[index]=[k2[0],value,k2[2]]
                if k2[2]<value:
                    totals[index]=[k2[0],k2[1],value]
                found=True
                break
        if not found:
            totals.append([year,value,value])
    print(f'\n\nhigh & lows\n\n{totals}')    
    return(totals)

def gas_prices():
    gp_inputfile='GasPrices.txt'
    gp_outputfile_low2high='GasPrices_low.out'
    gp_outputfile_high2low='GasPrices_high.out'
    gp_data_raw=gp_loaddata(gp_inputfile)
    gp_data_raw=gp_numeric(gp_data_raw)
    gp_avg_price_per_m=gp_avg_ppm(gp_data_raw)
    gp_avg_price_per_m=gp_avg_ppy(gp_data_raw)
    print(gp_data_raw)
    gp_hi_lo=gp_highs_lows(gp_data_raw)
    print(gp_hi_lo)
    gp_lo_2_hi=pb_sort(gp_data_raw,3,False)
    gp_hi_2_lo=pb_sort(gp_data_raw,3,True)
    spaces(2)
    print(gp_lo_2_hi)
    spaces(2)
    print(gp_hi_2_lo)
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
        print('[1]\t Initials')
        print('[2]\t Sum of Digits in a String')
        print('[3]\t Date Printer')
        print('[4]\t Morse Code Converter')
        print('[5]\t Alphabetic Telephone Number Translator')
        print('[6]\t Average Number of Words')
        print('[7]\t Character Analysis')
        print('[8]\t Sentence Capitalizer')
        print('[9]\t Vowels and Consonants')
        print('[10]\t Most Frequent Character')
        print('[11]\t Word Separator')
        print('[12]\t Pig Latin')
        print('[13]\t PowerBall Lottery')
        print('[14]\t Gas Prices')
        print('...\tanything else to exit\n')
        MENU=get_int('Make a selection to continue')
        if MENU==1:
            initials()
        elif MENU==2:
            sum_of_digits()
        elif MENU==3:
            date_printer()
        elif MENU==4:
            morse_code()
        elif MENU==5:
            alpha_tel_no()
        elif MENU==6:
            avg_num_of_words()
        elif MENU==7:
            char_analysis()
        elif MENU==8:
            sent_cap()
        elif MENU==9:
            vowels_n_consonants()
        elif MENU==10:
            most_freq_char()
        elif MENU==11:
            word_separator()
        elif MENU==12:
            pig_latin()
        elif MENU==13:
            power_ball()
        elif MENU==14:
            gas_prices()
        else:
            MENU=0
    # End of the developerInfo function

# Call the main function.
if __name__ == '__main__':
    main()