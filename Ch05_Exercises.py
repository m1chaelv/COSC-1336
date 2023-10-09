# Michael Villarreal
# COSC-1336
# ACC
#
# GLOBAL VARIABLES
#MENU=0

# Main menu system
def main():
    print('')
    MENU=1
    while MENU > 0 and MENU <= 26:
        print('[1]\t Kilometer Converter')
        print('[2]\t Sales Tax Program Refactoring')
        print('[3]\t How Much Insurance?')
        print('[4]\t Automobile Costs')
        print('[5]\t Property Tax')
        print('[6]\t Calories from Fat and Carbohydrates')
        print('[7]\t Stadium Seating')
        print('[8]\t Paint Job Estimator')
        print('[9]\t Monthly Sales Tax')
        print('[10]\t Feet to Inches')
        print('[11]\t Math Quiz')
        print('[12]\t Maximum of Two Values')
        print('[13]\t Falling Distance')
        print('[14]\t Kinetic Energy')
        print('[15]\t Test Average and Grade')
        print('[16]\t Odd/Even Counter')
        print('[17]\t Prime Numbers')
        print('[18]\t Prime Number List')
        print('[19]\t Future Value')
        print('[20]\t Random Number Guessing Game')
        print('[21]\t Rock, Paper, Scissors Game')
        print('[22]\t xxx')
        print('[23]\t xxx')
        print('[24]\t xxx')
        print('[25]\t xxx')
        print('[26]\t xxx')
        print('...\tanything else to exit\n')
        MENU=get_int('Make a selection to continue')
        if MENU==1:
            km_conv()
        elif MENU==2:
            sales_tax()
        elif MENU==3:
            how_much_ins()
        elif MENU==4:
            automobile_costs()
        elif MENU==5:
            property_tax()
        elif MENU==6:
            cal_from()
        elif MENU==7:
            stadium_seating()
        elif MENU==8:
            paint_job_est()
        elif MENU==9:
            monthly_sales_tax()
        elif MENU==10:
            ft_2_in()
        elif MENU==11:
            math_quiz()
        elif MENU==12:
            max_of_2_values()
        elif MENU==13:
            falling_dist_table()
        elif MENU==14:
            kinetic_energy_prog()
        elif MENU==15:
            test_avg_n_grade()
        elif MENU==16:
            odd_even_counter()
        elif MENU==17:
            prime_nums()
        elif MENU==18:
            prime_number_list()
        elif MENU==19:
            future_value()
        elif MENU==20:
            rand_num_guess_game()
        elif MENU==21:
            rock_paper_scissors()
        elif MENU==22:
            hold()
        elif MENU==23:
            hold()
        elif MENU==24:
            hold()
        elif MENU==25:
            hold()
        elif MENU==26:
            hold()
        else:
            MENU=0


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

# 1) Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles. The conversion formula is as follows:
# Miles = Kilometers × 0.6214
def km_conv():
    KM2M=.6214
    dist_m=0.0
    dist_km=float(input('\n\nEnter a distance in km: '))
    dist_m=dist_km*KM2M
    print(f'\n{dist_km:.2f} km converts to {dist_m:.2f} miles.')
    hold()

# 2) Sales Tax Program Refactoring
# Programming Exercise #6 in Chapter 2 I was the Sales Tax program. For that exercise, you were asked
# to write a program that calculates and displays the county and state sales tax on a purchase. If you have
# already written that program, redesign it so the subtasks are in functions. If you have not already written
# that program, write it using functions.
#
# Sales Tax
# Write a program that will ask the user to enter the amount of a purchase.
# The program should then compute the state and county sales tax. Assume
# the state sales tax is 5 percent and the county sales tax is 2.5 percent.
# The program should display the amount of the purchase, the state sales tax,
# the county sales tax, the total sales tax, and the total of the sale
# (which is the sum of the amount of purchase plus the total sales tax).
#
# Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to
# represent 5 percent.
def state_tx(sale):
    TAX = .05
    return sale*TAX

def county_tx(sale):
    TAX = .025
    return sale*TAX

def sales_tax():
    purchase_amt=float(input('Enter purchase amount: '))
    spaces(1)
    print(f'${purchase_amt:10,.2f}',' :Total')
    print(f'${state_tx(purchase_amt):10,.2f}',' :State Tax')
    print(f'${county_tx(purchase_amt):10,.2f}',' :County Tax')
    print(f'${purchase_amt + state_tx(purchase_amt) + county_tx(purchase_amt):10,.2f}',' :Grand Total')

    hold()

# 3) How Much Insurance?
# Many financial experts advise that property owners should insure their homes or buildings for at least 80
# percent of the amount it would cost to replace the structure. Write a program that asks the user to enter
# the replacement cost of a building, then displays the minimum amount of insurance he or she should buy
# for the property
def how_much_ins():
    RECOMMENDED_PERCENT=.8
    spaces(3)
    costs=float(input('Enter the cost to replace the structure: $'))
    spaces(1)
    replacement_costs = costs*RECOMMENDED_PERCENT
    print(f'Recommended insurance is ${replacement_costs:,.2f}.')
    hold()

# 4) Automobile Costs
# Write a program that asks the user to enter the monthly costs for the following expenses incurred from
# operating his or her automobile: loan payment, insurance, gas, oil, tires, and maintenance. The program
# should then display the total monthly cost of these expenses, and the total annual cost of these expenses.
def get_input(x):
    y=input(f'Monthly {x}: $')
    if y=='':
        return 0.0
    else:
        return int(y)

def automobile_costs():
    loan=ins=gas=oil=tires=maint=0.0
    tot_annual=tot_monthly=0.0
    spaces(3)

    loan+=get_input('loan payment')
    ins+=get_input('insurance premium')
    gas+=get_input('fuel costs')
    oil+=get_input('tires costs')
    maint+=get_input('maintenance expenses')

    tot_monthly=loan+ins+gas+oil+tires+maint
    tot_annual=tot_monthly*12

    spaces(2)
    print(f'{"Cost Summary":^30}')
    print(f"Monthly\t{f'${tot_monthly:,.2f}':->20}")
    print(f"Annual\t{f'${tot_annual:,.2f}':->20}")

    hold()

# 5) Property Tax
# A county collects property taxes on the assessment value of property, which is 60 percent of the property's
# actual value. For example, if an acre of land is valued at $10,000, its assessment value is $6,000. The
# property tax is then $.72 for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $43.20. 
# Write a program that asks for the actual value of a piece of property and displays the
# assessment value and property tax.
def property_tax():
    taxable_percent=.6
    tax_rate=.72/100
    actual_value=assess_value=prop_tax=0.0
    spots=0

    spaces(2)
    actual_value=float(input('Enter the market value for the property: $'))

    assess_value=actual_value*taxable_percent
    prop_tax=assess_value*tax_rate
    spots=len(str(f'${actual_value:,.2f}'))
    head=spots+len("assessment value: ")
    print(spots)

    spaces(2)
    print(f'{"tax statement":^{head}}')
    print(f'{"market value:     "}{f"${actual_value:,.2f}":>{spots}}')
    print(f'{"assessment value: "}{f"${assess_value:,.2f}":>{spots}}')
    print(f'{"property tax:     "}{f"${prop_tax:,.2f}":>{spots}}')

    hold()

# 6) Calories from Fat and Carbohydrates
# A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her
# evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in
# a day. Then, she calculates the number of calories that result from the fat, using the following formula:
#           calories from fat = fat grams × 9
# Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
#           calories from carbs = carb grams × 4
# The nutritionist asks you to write a program that will make these calculations.
def from_fat(grams):
    rate=9
    cal_from_fat=rate*grams
    return cal_from_fat

def from_carb(grams):
    rate=4
    cal_from_carb=rate*grams
    return cal_from_carb

def cal_question(text):
    cal_answer=int(input(f'how many {text} grams consumed: '))
    return cal_answer

def cal_from():
    spaces(2)
    fat=from_fat(cal_question('fat'))
    carbs=from_carb(cal_question('carbs'))

    spaces(2)
    print('nutritional evaluation')
    print(f'calories from fat:   {fat}')
    print(f'calories from carbs: {carbs}')
    print(f'total calories:      {fat+carbs}')

    hold()

# 7) Stadium Seating
# There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost $15, and Class
# C seats cost $10. Write a program that asks how many tickets for each class of seats were sold, then
# displays the amount of income generated from ticket sales.
def get_seats(text):
    x=int(input(f'How many {text} seats sold:\t'))
    return x

def stadium_seating():
    class_a_cost=20.0
    class_b_cost=15.0
    class_c_cost=10.0
    tot_a_income=0.0
    tot_b_income=0.0
    tot_c_income=0.0
    tot_income=0.0
    income_statement=(f'{"income statement":^40}')
    
    spaces(2)
    tot_a_income=class_a_cost*int(get_seats('Class A'))
    tot_b_income=class_b_cost*int(get_seats('Class B'))
    tot_c_income=class_c_cost*int(get_seats('Class C'))

    tot_income+=tot_a_income
    tot_income+=tot_b_income
    tot_income+=tot_c_income
    
    spaces(2)
    print(f'{"income statement":^30}')
    print(f'Class A:\t${tot_a_income:,.2f}')
    print(f'Class B:\t${tot_b_income:,.2f}')
    print(f'Class C:\t${tot_c_income:,.2f}')
    print(f'Total income:\t${tot_income:,.2f}')

    hold()

# 8) Paint Job Estimator
# A painting company has determined that for every 112 square feet of wall space, one gallon of paint and
# eight hours of labor will be required. The company charges $35.00 per hour for labor. Write a program that
# program should display the following data: asks the user to enter the square feet of wall space to be painted 
# and the price of the paint per gallon. The
# • The number of gallons of paint required
# • The hours of labor required
# • The cost of the paint
# • The labor charges
# • The total cost of the paint job
def get_int(text):
    x=input(f'{text} :')
    if x=='':
        return 0
    else:
        return(int(x))

def get_float(text):
    x=input(f'{text} :')
    if text=='':
        return 0.0
    else:
        return(float(x))

def paint_job_est():
    import math

    labor_rate=35.0
    # for every gallon of paint, [base_labor] hrs, [base_wall_space] sq ft painted
    base_wall_space=112
    base_labor=8

    tot_wall_space=0
    paint_cost=0.0

    tot_paint=0.0
    tot_paint_int=0
    tot_labor=0
    tot_paint_cost=0.0
    tot_labor_cost=0.0

    spaces(2)
    tot_wall_space=get_float('Enter the wall space in sq ft being painted')
    paint_cost=get_int('Enter cost per gallon of paint')

    tot_paint=tot_wall_space/base_wall_space
    tot_paint_int=math.ceil(tot_wall_space/base_wall_space)
    tot_paint_cost=tot_paint_int*paint_cost
    tot_labor=tot_paint*base_labor
    tot_labor_cost=tot_labor*labor_rate
    tot_job=tot_labor_cost+tot_paint_cost

    spaces(2)
    print(f'The number of gallons of paint required {tot_paint_int}')
    print(f'The hours of labor required {tot_labor}')
    print(f'The cost of the paint ${tot_paint_cost:,.2f}')
    print(f'The labor charges ${tot_labor_cost:,.2f}')
    print(f'The total cost of the paint job ${tot_job:,.2f}')

    hold()

# 9) Monthly Sales Tax
# A retail company must file a monthly sales tax report listing the total sales for the month, and the amount
# of state and county sales tax collected. The state sales tax rate is 5 percent and the county sales tax rate
# is 2.5 percent. Write a program that asks the user to enter the total sales for the month. From this figure,
# the application should calculate and display the following:
# • The amount of county sales tax
# • The amount of state sales tax
# • The total sales tax (county plus state)
def monthly_sales_tax():
    monthly_sales=0.0
    county_tx_collect=0.0
    state_tx_collect=0.0
    tot_sales_tax=0.0

    spaces(2)
    monthly_sales=get_float('Enter the total sales for the month')
    county_tx_collect=county_tx(monthly_sales)
    state_tx_collect=state_tx(monthly_sales)
    tot_sales_tax=county_tx_collect+state_tx_collect
    spaces(2)
    print(f'{"monthly sales tax report":^37}')
    print(f'Total sales:               {f"${monthly_sales:,.2f}":>10}')
    print(f'County tax collected:      {f"${county_tx_collect:,.2f}":>10}')
    print(f'State tax collected:       {f"${state_tx_collect:,.2f}":>10}')
    print(f'Total sales tax collected: {f"${tot_sales_tax:,.2f}":>10}')

    hold()

# 10) Feet to Inches
# One foot equals 12 inches. Write a function named feet_to_inches that accepts a number of feet as an
# argument and returns the number of inches in that many feet. Use the function in a program that prompts
# the user to enter a number of feet then displays the number of inches in that many feet.
def feet_to_inches(ft):
    # 12 inch in a foot
    return 12*ft

def ft_2_in():
    ft=0

    spaces(2)
    ft=get_int('Enter a measurment in feet')

    spaces(1)
    print(f'Total of {feet_to_inches(ft):,} inches.')

    hold()

# 11) Math Quiz
# Write a program that gives simple math quizzes. The program should display two random numbers that are
# to be added, such as:
#     247
#   + 129
# The program should allow the student to enter the answer. If the answer is correct, a message of
# congratulations should be displayed. If the answer is incorrect, a message showing the correct answer should be displayed.
def get_num(max):
    import random
    
    return random.randint(0,max)

def math_quiz():
    # a + b = c
    # max size of numbers
    max=1000
    a=get_num(max)
    b=get_num(max)

    spaces(3)
    print(f'  {a}')
    print(f'+ {b}')
    print(f'------')
    c=get_int('')

    spaces(1)
    if c==a+b:
        print('congratulations')
    else:
        print(f'correct answer was {a+b}.')
    
    hold()

# 12) Maximum of Two Values
# Write a function named max that accepts two integer values as arguments and returns the value that is the greater of the two. 
# For example, if 7 and 12 are passed as arguments to the function, the function should return 12. Use the function in a program 
# that prompts the user to enter two integer values. The program should display the value that is the greater of the two.
def max_of_2(x, y):
    if x > y:
        return x
    else:
        return y

def max_of_2_values():
    int_1=0
    int_2=0

    spaces(2)
    int_1=get_int('Enter an integer')
    int_2=get_int('Enter 2nd to compare')

    spaces(1)
    print(f'{max_of_2(int_1,int_2)} is the higher value.')

    hold()

# 13) Falling Distance
# When an object is falling because of gravity, the following formula can be used to determine the distance
# the object falls in a specific time period:
#           d = ½gt^2
# The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the amount of time,
# in seconds, that the object has been falling.
# Write a function named falling distance that accepts an object's falling time (in seconds) as an argument. 
# The function should return the distance, in meters, that the object has fallen during that time
# interval. Write a program that calls the function in a loop that passes the values 1 through 10 as arguments
# and displays the return value.
def falling_dist(t):
    # d distance in meters
    # g gravity constant 9.8
    # t time in seconds
    # formula  d = g/2*t**2
    g=9.8
    d=g/2*(t**2)
    return d

def falling_dist_table():
    table_rows=10

    spaces(2)
    print('time(s)\tdist(m)')
    for x in range(table_rows):
        y=falling_dist(x+1)
        print(f'{x+1}\t{y:,.2f}')
    
    hold()

# 14) Kinetic Energy
# In physics, an object that is in motion is said to have kinetic energy. The following formula can be used to
# determine a moving object's kinetic energy 
#               KE = ½mv^2
# The variables in the formula are as follows: KE is the kinetic energy, m is the object's mass in kilograms,
# and v is the object's velocity in meters per second.
# Write a function named kinetic_energy that accepts an object's mass (in kilograms) and velocity (in
# meters per second) as arguments. The function should return the amount of kinetic energy that the object
# has. Write a program that asks the user to enter values for mass and velocity, then calls the
# kinetic_energy function to get the object's kinetic energy.
def kinetic_energy(m, v):
    # KE = kinetic energy in Joules
    # m = object's mass in kilograms
    # v = object's velocity in meters per second
    # KE =m/2*(v**2)

    KE=m/2*(v**2)
    return KE


def kinetic_energy_prog():
    m=0.0
    v=0.0
    
    spaces(2)
    m=get_float('Enter an object\'s mass in kilograms')
    v=get_float('Enter an object\'s velocity in meters per second')

    spaces(1)
    print(f'The object\'s kenetic energy is {kinetic_energy(m,v):,.2f} Joules')

    hold()

# 15) Test Average and Grade
# Write a program that asks the user to enter five test scores. The program should display a letter grade for
# each score and the average test score. Write the following functions in the program:
# • calc_average. This function should accept five test scores as arguments and return the average of the
# scores.
# • determine_grade. This function should accept a test score as an argument and return a letter grade for
# the score based on the following grading scale:
# Score Letter Grade
# 90-100    A
# 80-89     B
# 70-79     C
# 60-69     D
# Below 60  F
def grade(avg):
    # 90-100    A
    # 80-89     B
    # 70-79     C
    # 60-69     D
    # Below 60  F
    if avg < 60:
        return 'F'
    elif avg < 70:
        return 'D'
    elif avg < 80:
        return 'C'
    elif avg < 90:
        return 'B'
    else:
        return 'A'

def test_avg_n_grade():
    how_many_scores=5
    avg=0.0

    spaces(2)
    for x in range(how_many_scores):
        y=(f'Enter test score [{x+1}]')
        avg+=get_int(y)/how_many_scores
    
    spaces(1)
    print(f'Test average is {avg} earning a grade of {grade(avg)}.')

    hold()

# 16) Odd/Even Counter
# In this chapter, you saw an example of how to write an algorithm that determines whether a number is even or odd. 
# Write a program that generates 100 random numbers and keeps a count of how many of
# those random numbers are even, and how many of them are odd.
def odd_even_counter():
    import random
    odds=0
    evens=0
    how_many_int=100

    print('Odd/Even Counter')
    for x in range(how_many_int):
        y=random.randrange(100)
        if y%2==0:
            evens+=1
        else:
            odds+=1
    print(f'Evens ({evens})\tOdds ({odds})')

    hold()

# 17) Prime Numbers
# A prime number is a number that is only evenly divisible by itself and 1. For example, the number 5 is
# prime because it can only be evenly divided by 1 and 5. The number 6, however, is not prime because it
# can be divided evenly by 1, 2, 3, and 6.
# Write a Boolean function named is_prime which takes an integer as an argument and returns true if the
# argument is a prime number, or false otherwise. Use the function in a program that prompts the user to
# enter a number then displays a message indicating whether the number is prime.
# Тір:
# Recall that the % operator divides one number by another and returns the remainder
# of the division. In an expression such as num1 & num2, the & operator will return O if 
# num1 is evenly divisible by num2.
def is_prime(number):
    # return True or False
    
    for x in range(2,number):
        if number%x == 0:
            return False
    return True
    

def prime_nums():
    number=0

    spaces(3)
    number=get_int('Prime Number Evaluation: [Enter an integer]')
    if is_prime(number)==True:
        x='is'
    else:
        x='is not'

    spaces(1)
    print(f'{number} {x} a prime number.')
    hold()

# 18) Prime Number List
# This exercise assumes that you have already written the is_prime function in Programming Exercise
# 17 I. Write another program that displays all of the prime numbers from 1 to 100. The program should
# have a loop that calls the is_prime function.
def prime_number_list():
    from_1_to=100

    spaces(2)
    print('Prime Numbers')
    print(f'from 1 to {from_1_to}')
    for x in range(1,from_1_to+1):
        y=is_prime(x)
        if y==True:
            print(f'{x:^13}')
    
    hold()

# 19) Future Value
# Suppose you have a certain amount of money in a savings account that earns compound monthly interest,
# and you want to calculate the amount that you will have after a specific number of months. The formula is
# as follows:
#           F = P × (1 + i)^t
# The terms in the formula are:
# • F is the future value of the account after the specified time period.
# • P is the present value of the account.
# • i is the monthly interest rate.
# • t is the number of months.
# Write a program that prompts the user to enter the account's present value, monthly interest rate, and the
# number of months that the money will be left in the account. The program should pass these values to a
# function that returns the future value of the account, after the specified number of months. The program 
# should display the account's future value.
def future_value():
    # • F is the future value of the account after the specified time period.
    # • P is the present value of the account.
    # • i is the monthly interest rate.
    # • t is the number of months.
    #  F = P × (1 + i)^t
    F=P=i=0.0
    t=0

    spaces(3)
    P=get_float('Enter present value of the account')
    i=get_float('Enter the monthly interest rate')/100
    t=get_int('Enter number of month in future to project')
    F=P*((1+i)**t)

    spaces(1)
    print(f'Future value will be ${F:,.2f}.')

    hold()

# 20) Random Number Guessing Game
# Write a program that generates a random number in the range of 1 through 100, and asks the user to 
# guess what the number is. If the user's guess is higher than the random number, the program should
# display "Too high, try again." If the user's guess is lower than the random number, the program should
# display "Too low, try again." If the user guesses the number, the application should congratulate the user
# and generate a new random number so the game can start over.
# Optional Enhancement: Enhance the game so it keeps count of the number of guesses that the user
# makes. When the user correctly guesses the random number, the program should display the number of
# guesses.
def rand_num_guess_game():
    import random
    
    max_guess=100
    guess_count=0
    answer=random.randrange(1,max_guess+1)
    guess=0

    spaces(3)
    while guess!=answer:
        guess_count+=1
        guess=get_int(f'Enter a number from 1 to {max_guess}')
        if guess>answer:
            print('[Too high]')
        elif guess<answer:
            print('[Too low]')
    
    spaces(1)
    print('Congratulations!')
    print(f'correct in {guess_count} attempts.')

    hold()

# 21) Rock, Paper, Scissors Game
# Write a program that lets the user play the game of Rock, Paper, Scissors against the computer. The
# program should work as follows:
# 1. When the program begins, a random number in the range of 1 through 3 is generated. If the number
#   is 1, then the computer has chosen rock. If the number is 2, then the computer has chosen paper. If
#   the number is 3, then the computer has chosen scissors. (Don't display the computer's choice yet.)
# 2. The user enters his or her choice of "rock," "paper," or "scissors" at the keyboard.
# 3. The computer's choice is displayed.
# 4. A winner is selected according to the following rules:
# • If one player chooses rock and the other player chooses scissors, then rock wins. (Rock
#   smashes scissors.)
# • If one player chooses scissors and the other player chooses paper, then scissors wins. (Scissors
#   cuts paper.)
# • If one player chooses paper and the other player chooses rock, then paper wins. (Paper wraps
#   rock.)
# • If both players make the same choice, the game must be played again to determine the winner.
def rps():
    # 1 = rock
    # 2 = paper
    # 3 = scissors
    # computer will return a guess
    import random

    x=random.randrange(1,4)
    return(x)

def rps_txt(x):
    # 1 = rock
    # 2 = paper
    # 3 = scissors
    if x == 1:
        return 'rock'
    elif x == 2:
        return 'paper'
    else:
        return 'scissors'
    
def rps_wld(player1,player2):
    # player 1 = user
    # return (win, lose, or draw)
    # [1]rock [2]paper [3]scissors
    # 13,21,32=win
    # 12,23,31=lose
    # 11,22,33=draw
    key=str(player1)+str(player2)
    if key=='13' or key=='21' or key=='32':
        return 'win'
    elif key=='12' or key=='23' or key=='31':
        return 'lose'
    return 'draw'


def rock_paper_scissors():
    # game against computer till a winner is declared
    # player 1 = user
    # player 2 = computer
    player1=player2=0
    
    spaces(3)
    while player1<1 or player1>3:
        player1=get_int('Enter [1]rock / [2]paper / [3]scissors')
        player2=rps()

        spaces(2)
        print(rps_txt(player1), rps_txt(player2))
        print(rps_wld(player1,player2))

        if player1==player2:
            player1=player2=0

    hold()

# 22) 

# Execution of program
main()
