# Michael Villarreal
# COSC-1336
# ACC
#

# Main menu system
def main():
    print('')
    MENU=1
    while MENU > 0 and MENU <= 26:
        print('[1]\t Total Sales')
        print('[2]\t Lottery Number Generator')
        print('[3]\t Rainfall Statistics')
        print('[4]\t Number Analysis Program')
        print('[5]\t Charge Account Validation')
        print('[6]\t Larger Than n')
        print('[7]\t Drivers License Exam')
        print('[8]\t Name Search')
        print('[9]\t Population Data')
        print('[10]\t World Series Champions')
        print('[11]\t Lo Shu Magic Square')
        print('[12]\t xxx')
        print('[13]\t xxx')
        print('[14]\t xxx')
        print('[15]\t xxx')
        print('...\tanything else to exit\n')
        MENU=get_int('Make a selection to continue')
        if MENU==1:
            total_sales()
        elif MENU==2:
            lot_num_gen()
        elif MENU==3:
            rainfall_stats()
        elif MENU==4:
            num_analysis()
        elif MENU==5:
            chrg_acct_val()
        elif MENU==6:
            larger_than()
        elif MENU==7:
            drivers_license_exam()
        elif MENU==8:
            name_search()
        elif MENU==9:
            population_data()
        elif MENU==10:
            world_series()
        elif MENU==11:
            lo_shu()
        elif MENU==12:
            hold()
        elif MENU==13:
            hold()
        elif MENU==14:
            hold()
        elif MENU==15:
            hold()
        else:
            MENU=0

# Hold to review output
def hold():
    input('\n\n\nPress [ENTER] to continue...')

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

def CP7_9():
    numbers = [1, 2, 3, 4, 5]
    my_list = numbers[1:3]
    print (my_list)
    hold()

def CP7_10():
    numbers = [1, 2, 3, 4, 5]
    my_list = numbers[1:]
    print (my_list)
    hold()

def CP7_11():
    numbers = [1, 2, 3, 4, 5]
    my_list = numbers[:1]
    print (my_list)
    hold()

def CP7_12():
    numbers = [1, 2, 3, 4, 5]
    my_list = numbers[:]
    print (my_list)
    hold()

def CP7_13():
    numbers = [1, 2, 3, 4, 5]
    my_list = numbers[-3:]
    print (my_list)
    hold()

def CP7_14():
    names = ['Jim', 'Jill', 'John', 'Jasmine']
    if 'Jasmine' not in names:
        print('Cannot find Jasmine.')
    else:
        print ("Jasmine's family:")
        print (names)

def CP7_22():
    numbers = ([1, 2], [10, 201], [100, 200], [1000, 200011])
    print(numbers)
    hold()

def CP7_23():
    infile=open('number_list.txt','r')
    k0=[1,2,3,4,5,6,7,8,9,10,11,12]
    for k in range(3):
        for k1 in range(4):
            
            print(f'{k0}-{k}:{k1}', end='\t')
        print('\n')
    hold()

# 1 Total Sales
# Design a program that asks the user to enter a store's sales for each day of the week. The amounts should
# be stored in a list. Use a loop to calculate the total sales for the week and display the result.
def total_sales():
    # variables
    days=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
    sales=[]
    ts=0.0

    try:
        spaces(3)
        for k in days:
            s=float(input(f'Enter sales for {k}: '))
            sales.append(s)
        for k in sales:
            ts+=k
        spaces(1)
        print(f'Total sales for the week: ${ts:,.2f}')
        hold()
    except Exception as err:
        print(err)
        hold()

# 2 Lottery Number Generator
# Design a program that generates a seven-digit lottery number. The program should generate seven 
# random numbers, each in the range of 0 through 9, and assign each number to a list element. (Random
# numbers were discussed in Chapter 5. Then write another loop that displays the contents of the list.
def lot_num_gen():
    
    # initialize variables
    digits=7
    x_min=0
    x_max=9
    lot_num=[0]*7

    # load the random functions
    import random

    # generate numbers based on criteria
    for k in range(digits):
        lot_num[k]=random.randrange(x_min,x_max)

    # print header
    print(f'\n\n\nLottery Numbers\n')

    # print final randomly generated lottery numbers
    for k in lot_num:
        print(f'{k}',end='')
    print()

    # pause for review before concluding function
    hold()

# 3 Rainfall Statistics
# Design a program that lets the user enter the total rainfall for each of 12 months into a list. The program
# should calculate and display the total rainfall for the year, the average monthly rainfall, the months with the
# highest and lowest amounts.
def rainfall_stats():
    # global variables
    months=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
    rf=[]
    tot_rain=0.0
    avg_rain=0.0
    min_months=''
    max_months=''
    min_rf=0.0
    max_rf=0.0

    # prompt for monthly rainfall
    spaces(3)
    for k in months:
        # input
        # k1 input of rainfall for given month
        k1=get_int(f'Enter rainfall totals for {k}')
        # store rainfall history
        rf.append(k1)
        # calculate
        # avg calc average rain for time period
        avg_rain+=k1/len(months)
        # sum of rainfall
        tot_rain+=k1

    # calculate min and max values   
    min_rf=min(rf)
    max_rf=max(rf)

    # identify the months of year with min and max values
    for k in months:
        # k1 return index from months
        k1=months.index(k)
        if rf[k1]==min_rf:
            min_months+=months[k1] + ' '
        elif rf[k1]==max_rf:
            max_months+=months[k1] + ' '

    # print inputs
    spaces(2)
    print(f'Summary')
    print(f'Total rainfall for year: {tot_rain:,.2f}')
    print(f'Average monthly rainfall: {avg_rain:,.2f}')
    print(f'Highest rainfall: {max_rf} for {max_months}')
    print(f'Lowest rainfall: {min_rf} for {min_months}')
    # print(rf,tot_rain,avg_rain,min_rf,max_rf,min_months,max_months)

    # pause for review before concluding function
    hold()

# 4 Number Analysis Program
# Design a program that asks the user to enter a series of 20 numbers. The program should store the
# numbers in a list then display the following data:
# • The lowest number in the list
# • The highest number in the list
# • The total of the numbers in the list
# • The average of the numbers in the list
def num_analysis():
    # variables
    series=20
    nums=[]
    nums_low=0
    nums_high=0
    nums_avg=0
    nums_sum=0

    spaces(3)
    print(f'Enter {series} integers for processing:')
    for k in range(series):
        tmp_one_based=k+1
        tmp_input=get_int(str(tmp_one_based))
        nums.append(tmp_input)
        nums_avg+=tmp_input/series
        nums_sum+=nums[k]
    nums_high=max(nums)
    nums_low=min(nums)

    spaces(2)
    print(f'The lowest number in the list: {nums_low}')
    print(f'The highest number in the list: {nums_high}')
    print(f'The total of the numbers in the list: {nums_sum}')
    print(f'The average of the numbers in the list: {nums_avg:,.2f}')

    hold()

# 5 Charge Account Validation
# If you have downloaded the source code from the Computer Science Portal you will find a file named
# charge_accounts.txt in the Chapter 07 ! folder. This file has a list of a company's valid charge account
# numbers. Each account number is a seven-digit number, such as 5658845.
# Write a program that reads the contents of the file into a list. The program should then ask the user to enter
# a charge account number. The program should determine whether the number is valid by searching for it in
# the list. If the number is in the list, the program should display a message indicating the number is valid. If
# the number is not in the list, the program should display a message indicating the number is invalid.
# (You can access the Computer Science Portal at www.pearsonhighered.com/gaddis.)
def chrg_acct_val():
    accts_master=open('charge_accounts.txt','r')
    accts=[]
    accts_input=0
    # k=0
    line_from_file = accts_master.readline().strip('\n')
    while line_from_file != '':
        # Append record to list as integer
        accts.append(int(line_from_file))
        # Read the next line.
        line_from_file = accts_master.readline().strip('\n')

    spaces(3)
    accts_input=get_int('Enter a charge account number: ')
    spaces(2)
    print(f'Account {accts_input} is',end=' ')
    if accts_input in accts:
        print(f'valid.')
    else:
        print(f'not valid.')

    hold()

# 6 Larger Than n
# In a program, write a function that accepts two arguments: a list, and a number n. Assume that the list 
# contains numbers. The function should display all of the numbers in the list that are greater than the
# number n.
def larger_than():
    import random
    master_count=20
    master_list=[]
    
    k=0
    while k < master_count:
        master_list.append(random.randint(1,10))
        print(k, master_list[k])
        k+=1
    
    master_start=get_int('Enter a number from 1-10')

    for k in master_list:
        if k > master_start:
            print(k)

    print(master_start)
    print(master_list)

    hold()

# 7 Driver's License Exam
# The local driver's license office has asked you to create an application that grades the written portion of
# the driver's license exam. The exam has 20 multiple-choice questions. Here are the correct answers:
# 1.    А
# 2.    C
# 3.    А
# 4.    A
# 5.    D
# 6.    В
# 7.    C
# 8.    А
# 9.    C
# 10.   B 
# 11.   А
# 12.   D
# 13.   C
# 14.   A
# 15.   D
# 16.   C
# 17.   В
# 18.   B
# 19.   D
# 20.   A
# Your program should store these correct answers in a list. The program should read the student's answers
# for each of the 20 questions from a text file and store the answers in another list. (Create your own text file
# to test the application.) After the student's answers have been read from the file, the program should
# display a message indicating whether the student passed or failed the exam. (A student must correctly
# answer 15 of the 20 questions to pass the exam.) It should then display the total number of correctly
# answered questions, the total number of incorrectly answered questions, and a list showing the question
# numbers of the incorrectly answered questions.
def drivers_license_exam():
    dl_answers=[' ','A','C','А','A','D','В','C','A','C','B','A','D','C','A','D','С','B','B','D','A']
    dl_resp_in=open('dl_test_responses.txt','r')
    # dl_record=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    dl_record=[]
    dl_graded_all=[]
    dl_graded=[]



    dl_record = dl_resp_in.readline().strip('\n').split(',')
    while '' not in dl_record:
        k1=0
        k2=k3=0
        k4=k5=k6=''
        for k in dl_record:
            if k1==0:
                dl_graded.append(k)
                k4=k
            elif k==dl_answers[k1]:
                dl_graded.append(True)
                k6+=(f'  {k1:>2}\t[{k}]\n')
                k2+=1
            else:
                dl_graded.append(False)
                k6+=(f'x {k1:>2}\t[{k}]>[{dl_answers[k1]}]\n')
                k3+=1
            k1+=1
        dl_graded_all.append(dl_graded)
        dl_graded=[]
        dl_record = dl_resp_in.readline().strip('\n').split(',')

        if k2>=15:
            k5='pass'
        else:
            k5='fail'
        print(f'{k4}\t{k2}/{k2+k3} [{k5}]')
        print(k6)
        spaces(3)

    print(dl_record)
    hold()

    dl_resp_in.close()

# 8 Name Search
# If you have downloaded the source code you will find the following files in the Chapter 07 " folder:
# • GirlNames.txt This file contains a list of the 200 most popular names given to girls born in the United
# States from the year 2000 through 2009.
# • BoyNames.txt This file contains a list of the 200 most popular names given to boys born in the United
# States from the year 2000 through 2009.
# Write a program that reads the contents of the two files into two separate lists. The user should be able to
# enter a boy's name, a girl's name, or both, and the application will display messages indicating whether the
# names were among the most popular.
# (You can access the Computer Science Portal at www.pearsonhighered.com/gaddis.)
def ns_load_names(file_name):
    ns_infile=open(file_name,'r')
    ns_line=[]
    ns_list=[]

    ns_line=ns_infile.readline().strip('\n').split(',')
    while '' not in ns_line:
        ns_list.append(ns_line[0])
        ns_line=ns_infile.readline().strip('\n').split(',')

    ns_infile.close()
    return(ns_list)

def name_search():
    ns_infiles=('BoyNames.txt','GirlNames.txt')
    ns_boys=[]
    ns_girls=[]
    names=[]

    for files in ns_infiles:
        names=(ns_load_names(files))
        for k in names:
            if 'Boy' in files:
                ns_boys.append(k)
            else:
                ns_girls.append(k)

    spaces(3)
    print('A list has been collected of the top 200 boys and 200 girls names\n',
          'between 2000 and 2009. Enter a name and I will tell you if the name\n',
          'is on these lists.')
    print()
    name=input('Enter a name: ')

    if name in ns_boys:
        ns_message="a boy's name"
    elif name in ns_girls:
        ns_message="a girl's name"
    else:
        ns_message='not'

    print(f'{name} is {ns_message} on the list.')
    hold()

# 9 Population Data
# If you have downloaded the source code you will find a file named uspopulation. txt in the Chapter 07
# folder. The file contains the midyear population of the United States, in thousands, during the years 1950
# through 1990. The first line in the file contains the population for 1950, the second line contains the
# population for 1951, and so forth.
# Write a program that reads the file's contents into a list. The program should display the following data:
# • The average annual change in population during the time period
# • The year with the greatest increase in population during the time period
# • The year with the smallest increase in population during the time period
def population_data():
    pop_infile=open('USPopulation.txt','r')
    pop_from=1950
    pop_to=1950
    pop_data=[]
    pop_avg=0.0
    pop_last_yr=[]

    pop_line=pop_infile.readline().strip('\n')
    while pop_line != '':
        pop_data.append([pop_to, int(pop_line)])
        pop_to+=1
        pop_line=pop_infile.readline().strip('\n')
        pop_inc=[]
        pop_inc_list=[]
        pop_inc_high=[]
        pop_inc_low=[]

    pop_last_yr=[pop_data[0][0],pop_data[0][1]]
    for k in pop_data:
        pop_avg+=k[1]/len(pop_data)
        pop_diff=k[1]-pop_last_yr[1]

        k1=[k[0],k[1],pop_diff]
        pop_inc_list.append(k1)
        pop_last_yr=k

    for k in pop_inc_list:
        if k[2]==0:
            pop_inc_high=[k[0],k[1],k[2]]
            pop_inc_low=[k[0],k[1],k[2]]
        elif k[2] > pop_inc_high[2]:
            pop_inc_high=[k[0],k[1],k[2]]
        elif pop_inc_low[2]==0:
            pop_inc_low=[k[0],k[1],k[2]]
        elif k[2] < pop_inc_low[2]:
            pop_inc_low=[k[0],k[1],k[2]]

    spaces(3)
    print(f'From:\t{pop_from}\nTo:\t{pop_to}')
    print(f'max increase of {pop_inc_high[2]} was in {pop_inc_high[0]} to {pop_inc_high[1]}.')
    print(f'min increase of {pop_inc_low[2]} was in {pop_inc_low[0]} to {pop_inc_low[1]}.')
    print(f'average population of {pop_avg:,.0f}')
    hold()

    pop_infile.close()

# 10 World Series Champions
# If you have downloaded the source code you will find a file
# named WorldSeriesWinners.txt in the Chapter 07 L
# folder. This file contains a chronological list of the World
# Series winning teams from 1903 through 2009. The first line
# in the file is the name of the team that won in 1903, and the
# last line is the name of the team that won in 2009. Note the
# World Series was not played in 1904 or 1994.)
# Write a program that lets the user enter the name of a team,
# then displays the number of times that team has won the
# World Series in the time period from 1903 through 2009.
# Tip:
# Read the contents of the WorldSeriesWinners.txt file
# into a list. When the user enters the name of a team,
# the program should step through the list, counting
# the number of times the selected team appears.
def world_series():
    ws_infile=open('WorldSeriesWinners.txt','r')
    ws_start=1903
    ws_except=[1904,1994]
    ws_list=[]

    ws_winners=ws_infile.readline().strip('\n')
    while ws_winners != '':
        while ws_start in ws_except:
            k2=[ws_start,'[NOT PLAYED]']
            ws_start+=1
        k2=[ws_start,ws_winners]
        ws_winners=ws_infile.readline().strip('\n')
        ws_start+=1
        ws_list.append(k2)

    ws_count=0
    ws_years=''
    while ws_years=='':

        ws_temp=[]
        for k in ws_list:
            if k[1] not in ws_temp:
                ws_temp.append(k[1])
        ws_temp.sort()
        for k in ws_temp:
            print(f'{ws_count:>2}:{k}')
            ws_count+=1
        ws_count=0

        spaces(3)
        ws_team=ws_temp[get_int('enter a team to research')]

        for k in ws_list:
            if ws_team.lower() in k[1].lower():
                ws_count+=1
                ws_years+=str(f'{k[0]} ')
        print(ws_team, ws_count, ws_years)

    hold()

# 11 Lo Shu Magic Square
# The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-21 P. The Lo Shu
# Magic Square has the following properties:
# • The grid contains the numbers 1 through 9 exactly.
# • The sum of each row, each column, and each diagonal all add up to the same number.
# This is shown in Figure 7-22
# Figure 7-21 The Lo Shu Magic Square
# +---+---+---+
# | 4 | 9 | 2 |
# +---+---+---+
# | 3 | 5 | 7 |
# +---+---+---+
# | 8 | 1 | 6 |
# +---+---+---+
# Figure 7-22 The sum of the rows, columns, and diagonals
# In a program you can simulate a magic square using a two-dimensional list. Write a function that accepts a
# two-dimensional list as an argument and determines whether the list is a Lo Shu Magic Square. Test the
# function in a program.
def lo_shu_digits(ls_nums):
    k0=str(ls_nums)
    if len(k0)!=9:
        return(False)
    for k1 in range(1,10):
        if str(k1) not in k0:
            return(False)
    return(True)
    
def lo_shu_2d(ls_nums):
    # convert to 2d list
    # k0=dimensions, r=row loop counter, c=column loop counters
    k0=3
    k1=list(str(ls_nums))
    k2=0
    k3=[[0,0,0],
        [0,0,0],
        [0,0,0]]
    for r in range(k0):
        for c in range(k0):
            # print(r,c,k1[k2])
            # hold()
            k3[r][c]=int(k1[k2])
            k2+=1
    for r in range(k0):
        for c in range(k0):
            print(k3[r][c],end=' ')
        print()
    return(k3)
    hold()

def lo_shu_test(lo_shu_nums):
    lo_answer=15
    k0=3
    k1=lo_shu_nums
    k2=[]
    r0=r1=r2=0
    c0=c1=c2=0
    d1=d2=0
    for r in range(k0):
        for c in range(k0):
            if c==0:
                c0+=k1[r][c]
            elif c==1:
                c1+=k1[r][c]
            elif c==2:
                c2+=k1[r][c]
            if r==0:
                r0+=k1[r][c]
            elif r==1:
                r1+=k1[r][c]
            elif r==2:
                r2+=k1[r][c]
            if r==c:
                d1+=k1[r][c]
            if r+c==2:
                d2+=k1[r][c]

    cx=[c0,c1,c2]
    print(f'\t\t\t/{d2}')
    for r in range(k0):
        rx=0
        for c in range(k0):
            print(k1[r][c],end='\t')
            rx+=k1[r][c]
        print(f'-{rx}')
    print(f'|\t|\t|\t\\')
    print(f'{c0}\t{c1}\t{c2}\t{d1}')

    k2=[c0,c1,c2,r0,r1,r2,d1,d2]
    for k3 in k2:
        if k3!=lo_answer:
            return(False)
    else:
        return(True)

def lo_shu():
    ls_valid_num=False
    lo_shu_nums=[]

    spaces(3)
    while ls_valid_num==False:
        spaces(1)
        ls_nums=get_int('enter a squence of number for a Lo Shu Magic Square')
        ls_valid_num=(lo_shu_digits(ls_nums))
    
    lo_shu_nums+=lo_shu_2d(ls_nums)
    print(f'\nThis is {lo_shu_test(lo_shu_nums)}')
    hold()



if __name__=='__main__':
    main()