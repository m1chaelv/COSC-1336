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
        print('[7]\t Driver's License Exam')
        print('[8]\t xxx')
        print('[9]\t xxx')
        print('[10]\t xxx')
        print('[11]\t xxx')
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
            dr()
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
    k=0
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

if __name__=='__main__':
    main()