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
    while MENU > 0 and MENU <= 19:
        print('[1]\tBug Collector')
        print('[2]\tCalories Burned')
        print('[3]\tBudget Analysis')
        print('[4]\tDistance Traveled')
        print('[5]\tAverage Rainfall')
        print('[6]\tCelsius to Fahrenheit Table')
        print('[7]\tPennies for Pay')
        print('[8]\tSum of Numbers')
        print('[9]\tOcean Levels')
        print('[10]\tTuition Increase')
        print('[11]\tWeight Loss')
        print('[12]\tCalculating the Factorial of a Number')
        print('[13]\tPopulation')
        print('[14]\tPattern 1')
        print('[15]\tPattern 2')
        print('[16]\tTurtle Graphics: Repeating Squares')
        print('[17]\tTurtle Graphics: Star Pattern')
        print('[18]\tTurtle Graphics: Hypnotic Pattern')
        print('[19]\tTurtle Graphics: STOP Sign')
        print('...\tanything else to exit\n')
        MENU=int(input('Make a selection to continue: '))
        if MENU==1:
            bug_collector()
        elif MENU==2:
            calories_burned()
        elif MENU==3:
            budget_analysis()
        elif MENU==4:
            distance_traveled()
        elif MENU==5:
            average_rainfall()
        elif MENU==6:
            celsius_2_fahrenheit()
        elif MENU==7:
            pennies_for_pay()
        elif MENU==8:
            sum_of_numbers()
        elif MENU==9:
            ocean_levels()
        elif MENU==10:
            tuition_increase()
        elif MENU==11:
            weight_loss()
        elif MENU==12:
            factorial()
        elif MENU==13:
            population()
        elif MENU==14:
            pattern1()
        elif MENU==15:
            pattern2()
        elif MENU==16:
            repeating_squares()
        elif MENU==17:
            star_pattern()
        elif MENU==18:
            hypnotic_pattern()
        elif MENU==19:
            stop_sign()
        else:
            MENU=0


# Hold to review output
def hold():
    hd=input('\n\n\nPress [ENTER] to continue...')

# 1) bug collector
# A bug collector collects bugs every day for five days. Write a
# program that keeps a running total of the number of bugs
# collected during the five days. The loop should ask for the
# number of bugs collected for each day, and when the loop is
# finished, the program should display the total number of
# bugs collected.
def bug_collector():
    tot_bugs=0
    days_bugs=3
    for k in range(days_bugs):
        x=int(input(f'How many bugs were collected on day {k+1}: '))
        tot_bugs+=x
    print(f'\nThere were a total of {tot_bugs} collected in {days_bugs} days.')
    hold()

# 2) calories burned
# Running on a particular treadmill you burn 4.2 calories per
# minute. Write a program that uses a loop to display the
# number of calories burned after 10, 15, 20, 25, and 30
# minutes.
def calories_burned():
    CAL_PER_MIN=4.2
    title='Calories  Burned'
    print(f'\n\n{title:^20}')
    print(f'{"":-^20}')
    print(f'{"minutes":^10}{"calories":^10}')
    for k in range(10,31,5):
        cal=k*CAL_PER_MIN
        print(f'{k:^10}{cal:^10}')
    hold()

# 3) budget analysis
# Write a program that asks the user to enter the amount that
# he or she has budgeted for a month. A loop should then
# prompt the user to enter each of his or her expenses for the
# month and keep a running total. When the loop finishes, the
# program should display the amount that the user is over or
# under budget.
def budget_analysis():
    budget=0.0
    exp=0.0
    tot_exp=0.0
    in_exp=' '
    budget=float(input('\n\nBudget: '))
    while in_exp!='':
        in_exp=input('Expense\t: ')
        if in_exp!='':
            tot_exp+=int(in_exp)
    if tot_exp>budget:
        print(f'Overbudget by ${tot_exp-budget:,.2f} with ${tot_exp:,.2f} spent.')
    elif tot_exp<budget:
        print(f'Underbudget by ${budget-tot_exp:,.2f} with ${tot_exp:,.2f} spent.')
    else:
        print(f'On budget ${budget:,.2f}')
    hold()

# 4) distance traveled
# The distance a vehicle travels can be calculated as follows:
#   distance = speed × time
# For example, if a train travels 40 miles per hour for three
# hours, the distance traveled is 120 miles. Write a program
# that asks the user for the speed of a vehicle (in miles per
# hour) and the number of hours it has traveled. It should then
# use a loop to display the distance the vehicle has traveled for
# each hour of that time period. Here is an example of the
# desired output:
# What is the speed of the vehicle in mph?
# 40 [Enter]
# How many hours has it traveled? 3 [Enter]
# Hour     Distance Traveled
# 1         40
# 2         80
# 3         120
def distance_traveled():
    speed=int(input('\n\nWhat is the speed of the vehicle in mph? '))
    duration=int(input('How many hours has it traveled? '))
    print(f'\n\n{"Hour":^4}{"Distance Traveled":^20}')
    for x in range(duration):
        print(f'{x+1:^4}{str(speed*(x+1))+" miles":^20}')
    hold()

# 5) Average Rainfall
# Write a program that uses nested loops to collect data and
# calculate the average rainfall over a period of years. The
# program should first ask for the number of years. The outer
# loop will iterate once for each year. The inner loop will iterate
# twelve times, once for each month. Each iteration of the
# inner loop will ask the user for the inches of rainfall for that
# month. After all iterations, the program should display the
# number of months, the total inches of rainfall, and the
# average rainfall per month for the entire period.
def average_rainfall():
    avg_rain=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    yrs=int(input('\n\nhow many years? '))
    for k in range(yrs):
        print()
        for g in range(12):
            rain=int(input(f'rain fall month {g+1} in year {k+1}: '))
            avg_rain[g]+=(rain/yrs)
    print(f'\n\n{"month":^7}{"avg rain":^10}')
    for k in range(12):
        print(f'{k+1:^7}{avg_rain[k]:^10.2f}')
    hold()

# 6) Celsius to Fahrenheit Table
# Write a program that displays a table of the Celsius
# temperatures 0 through 20 and their Fahrenheit equivalents.
# The formula for converting a temperature from Celsius to
# Fahrenheit is
#       9
# F=    - C + 32
#       5
# where F is the Fahrenheit temperature, and C is the Celsius
# temperature. Your program must use a loop to display the
# table.
def celsius_2_fahrenheit():
    print(f'\n\n{"Celcius":^9}{"Fahrenheit":^10}')
    for c in range(21):
        f=(32+(9*c/5))
        print(f'{c:.^9}{f:.^10}')
    hold()

# 7) Pennies for Pay
# Write a program that calculates the amount of money a
# person would earn over a period of time if his or her salary is
# one penny the first day, two pennies the second day, and
# continues to double each day. The program should ask the
# user for the number of days. Display a table showing what
# the salary was for each day, then show the total pay at the
# end of the period. The output should be displayed in a dollar
# amount, not the number of pennies.
def pennies_for_pay():
    tot=0
    daily=0
    days=0
    rate=1
    days=int(input('\n\nEnter the number of days worked? ' ))
    print()
    spaces=len(str(2**days))
    spaces+=(spaces//3)
    print(f'day\t{"salary":>{spaces}}')
    for x in range(1,days+1):
        if daily==0:
            daily=1
        else:
            daily*=2
        print(f'{x}\t$ {daily/100:>{spaces},.2f}')
        tot+=daily
    print(f'total:\t$ {tot/100:>{spaces},.2f}')
    hold()

# 8) Sum of Numbers
# Write a program with a loop that asks the user to enter a
# series of positive numbers. The user should enter a negative
# number to signal the end of the series. After all the positive
# numbers have been entered, the program should display
# their sum.
def sum_of_numbers():
    tot=0
    cont=True
    print('\n\nEnter a series of positive numbers to be totaled.'
          '\nWhen finished, enter a negative number.\n\n')
    while cont==True:
        x=(int(input('Enter number: ')))
        if x<0:
            cont=False
        else:
            tot+=x
    print(f'\nTotal is {tot}')

    hold()

# 9) Ocean Levels
# Assuming the ocean's level is currently rising at about 1.6
# millimeters per year, create an application that displays the
# number of millimeters that the ocean will have risen each
# year for the next 25 years.
def ocean_levels():
    YRS=25
    RT=1.6
    tot=0.0
    print(f'\n\nyr\trise(mm)\n')
    for x in range(1,YRS+1):
        print(f'{x}\t{x*RT:.2f} mm')
    hold()

# 10) Tuition Increase
# At one college, the tuition for a full-time student is $8,000 per
# semester. It has been announced that the tuition will increase
# by 3 percent each year for the next 5 years. Write a program
# with a loop that displays the projected semester tuition
# amount for the next 5 years.
def tuition_increase():
    YRS=5
    BASE=8000
    #% increase per year
    RT=3
    print(f'\n\nyr\ttuition\n')
    for x in range(YRS+1):
        print(f'{x}\t${BASE:,.2f}')
        BASE+=BASE*RT/100
    hold()

# 11) Weight Loss
# If a moderately active person cuts their calorie intake by 500
# calories a day, they can typically lose about 4 pounds a
# month. Write a program that lets the user enter their starting
# weight, then creates and displays a table showing what their
# expected weight will be at the end of each month for the
# next 6 months if they stay on this diet.
def weight_loss():
    MONTHS=6
    RATE=4
    weight=int(input('\n\nEnter current weight: '))
    print(f'\nBased on a deficite of 500 calores per day.\n'
          f'This is the projected progress for the next {MONTHS} months\n'
          f'At a rate of {RATE} lbs per month.\n')
    print(f'\nmonth\tweight\n')
    for x in range(MONTHS+1):
        print(f'{x}\t{weight:.0f}')
        weight-=4
    hold()

# 12) Calculating the Factorial of a Number
# In mathematics, the notation n! represents the factorial of the
# nonnegative integer n. The factorial of n is the product of all
# the nonnegative integers from 1 to n. For example,
#       7! = 1 × 2 × 3 × 4 × 5 × 6 × 7=5,040
# and
#       4! =1 × 2 × 3 × 4=24
# Write a program that lets the user enter a nonnegative
# integer then uses a loop to calculate the factorial of that
# number. Display the factorial.
def factorial():
    fact=0
    cont=True
    while cont==True:
        get_input=int(input('\n\nEnter a nonnegative number to calculate the factorial: '))
        if get_input<0:
            print('Error: nonnegative only...')
        else:
            cont=False
    for x in range(1,get_input+1):
        if x==1:
            fact=1
        else:
            fact*=x
    print(f'\n{get_input}! = {fact:,.0f}')
    hold()

# 13) Population
# Write a program that predicts the approximate size of a
# population of organisms. The application should use text
# boxes to allow the user to enter the starting number of
# organisms, the average daily population increase (as a
# percentage), and the number of days the organisms will be
# left to multiply. For example, assume the user enters the
# following values:
#
# Starting number of organisms: 2
# Average daily increase: 30%
# Number of days to multiply: 10
#
# The program should display the following table of data:
# Day Approximate     Population
# 1                     2
# 2                     2.6
# 3                     3.38
# 4                     4.394
# 5                     5.7122
# 6                     7.42586
# 7                     9.653619
# 8                     12.5497
# 9                     16.31462
# 10                    21.209
def population():
    print('\n\n')
    start=int(input('Starting number of organisms: '))
    percent_text=input('Average daily increase: ')
    percent_int=float(percent_text.strip('%'))/100
    days=int(input('Number of days to multiply: '))
    print()
    print(f'Day Approximate\tPopulation')
    for x in range(1,days+1):
        print(f'{x}\t\t{start:.5f}'.rstrip("0").rstrip("."))
        start+=start*percent_int
    hold()

# 14) Write a program that uses nested loops to draw this pattern:
# *******
# ******
# *****
# ****
# ***
# **
# *
def pattern1():
    stars=7
    for x in range(stars,0,-1):
        for y in range(x):
            print('*', end='')
        print()
    hold()

# 15) Write a program that uses nested loops to draw this pattern:
# ##
# # #
# #  #
# #   #
# #    #
# #     #
def pattern2():
    rows=6
    for x in range(rows):
        print('#', end='')
        for y in range(x):
            print(' ', end='')
        print('#')
    hold()

# 16) Turtle Graphics: Repeating Squares
def repeating_squares():
    count=0
    import turtle
    turtle.reset()
    turtle.speed(0)
    turtle.right(180)
    turtle.penup()
    turtle.goto(200,-200)
    turtle.pendown()
    for x in range(10,510,5):
        count+=1
        for y in range(4):
            turtle.forward(x)
            turtle.right(90)
    print(count)
    hold()           

# 17) Turtle Graphics: Star Pattern
# Use a loop with the turtle graphics library to draw the design
# shown in Figure 4-14
def star_pattern():
    import turtle
    turtle.reset()
    turtle.speed(0)
    for x in range(8):
        turtle.forward(300)
        turtle.left(225)
    hold()

# 18) Turtle Graphics: Hypnotic Pattern
# Use a loop with the turtle graphics library to draw the design
# shown in Figure 4-15
def hypnotic_pattern():
    length=8
    squares=12
    import turtle
    turtle.reset()
    turtle.speed(0)
    for x in range(squares*4+2):
        turtle.forward(length*x)
        turtle.left(90)
    hold()

# 19) Turtle Graphics: STOP Sign
def stop_sign():
    import turtle
    turtle.reset()
    turtle.speed(0)
    turtle.penup()
    
    turtle.goto(-120,50)
    turtle.pendown()

    turtle.left(-135)

    for x in range(8):
        turtle.left(45)
        turtle.forward(100)

    turtle.penup()
    turtle.right(-135)
    turtle.forward(30)

    # S
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)

    turtle.right(-90)
    turtle.forward(30)

    turtle.right(90)
    turtle.forward(50)

    turtle.right(90)
    turtle.forward(30)

    turtle.penup()
    turtle.right(90)
    turtle.forward(100)

    turtle.pendown()
    turtle.right(90)
    turtle.forward(30)

    # T
    turtle.penup()
    turtle.forward(20)

    turtle.pendown()
    turtle.forward(15)

    turtle.right(90)
    turtle.forward(100)

    turtle.right(180)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(15)

    # O
    turtle.penup()
    turtle.forward(20)

    turtle.pendown()
    turtle.forward(30)

    turtle.right(90)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(30)

    turtle.right(90)
    turtle.forward(100)

    # P
    turtle.penup()
    turtle.right(90)
    turtle.forward(80)

    turtle.pendown()

    turtle.right(90)
    turtle.forward(50)

    turtle.right(90)
    turtle.forward(30)

    turtle.right(-90)
    turtle.forward(50)

    turtle.right(180)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(30)

    hold()


# Execution of program
main()
