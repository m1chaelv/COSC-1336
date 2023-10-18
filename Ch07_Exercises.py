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
        print('[15]\t xxx')
        print('...\tanything else to exit\n')
        MENU=get_int('Make a selection to continue')
        if MENU==1:
            total_sales()
        elif MENU==2:
            lot_num_gen()
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
    pass

if __name__=='__main__':
    main()