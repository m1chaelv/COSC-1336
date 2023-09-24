#***************************************************************
#
#  Developer:       Michael Villarreal
#
#  Program #:       Exercise
#
#  File Name:       Ch02_Exercises.py
#
#  Course:          COSC 1336 Programming Fundamentals I
#
#  Due Date:        09-20-2023
#
#  Instructor:      Onabajo
#
#  Chapter:         <Chapter 3>
#
#  Exercise:        <Exercise>
#
#  Description:
#
#
#***************************************************************

# Day of the Week
# Write a program that asks the user for a number in the range of
# 1 through 7. The program should display the corresponding day of
# the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday,
# 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display
# an error message if the user enters a number that is outside the
# range of 1 through 7.

def exercise01():
    Numb_1to7 = int(input('Enter a number between 1-10: '))
    if(Numb_1to7==1):
        print('Monday')
    elif(Numb_1to7==2):
        print('Tuesday')
    elif(Numb_1to7==3):
        print('Wednesday')
    elif(Numb_1to7==4):
        print('Thursday')
    elif(Numb_1to7==5):
        print('Friday')
    elif(Numb_1to7==6):
        print('Saturday')
    elif(Numb_1to7==7):
        print('Sunday')
    else:
        print('Error: Incorrect input.')

# Areas of Rectangles
# The area of a rectangle is the rectangle’s length times its width.
# Write a program that asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater
# area, or if the areas are the same.

def exercise02():
    rectangle1=0
    rectangle2=0

    # input rectangle1
    side1=int(input('enter length of shape: '))
    side2=int(input('enter width of shape: '))
    rectangle1=side1*side2
    next()

    # input rectangle1
    side1=int(input('enter length of shape: '))
    side2=int(input('enter width of shape: '))
    rectangle2=side1*side2
    next()

    if (rectangle1>rectangle2):
        print('Rectangle 1 is larger than 2.')
    elif (rectangle2>rectangle1):
        print('Rectangle 2 is larger than 1.')
    elif (rectangle1==rectangle2):
        print('both are the same size by area.')
    else:
        print('Error occurred.')

# Age Classifier
# Write a program that asks the user to enter a person’s age.
# The program should display a message indicating whether the person
# is an infant, a child, a teenager, or an adult. Following are the
# guidelines:
#
# If the person is 1 year old or less, he or she is an infant.
#
# If the person is older than 1 year, but younger than 13 years,
# he or she is a child.
#
# If the person is at least 13 years old, but less than 20 years old,
# he or she is a teenager.
#
# If the person is at least 20 years old, he or she is an adult.

def exercise03():
    Age=int(input('Enter age of the person of interest: '))
    next()
    if(Age<=1):
        print('infant')
    elif(Age<13):
        print('child')
    elif(Age<20):
        print('teenager')
    else:
        print('adult')

# Roman Numerals
# Write a program that prompts the user to enter a number within
# the range of 1 through 10. The program should display the Roman
# numeral version of that number. If the number is outside the range
# of 1 through 10, the program should display an error message. The
# following table shows the Roman numerals for the numbers 1 through 10:
#
# Number	Roman Numeral
#  1	I
#  2	II
#  3	III
#  4	IV
#  5	V
#  6	VI
#  7	VII
#  8	VIII
#  9	IX
# 10	X

def exercise04():
    Numb_2convert=int(input('Enter a number from 1-10: '))

    if(Numb_2convert==1):
        print('I')
    elif(Numb_2convert==2):
        print('II')
    elif(Numb_2convert==3):
        print('III')
    elif(Numb_2convert==4):
        print('IV')
    elif(Numb_2convert==5):
        print('V')
    elif(Numb_2convert==6):
        print('VI')
    elif(Numb_2convert==7):
        print('VII')
    elif(Numb_2convert==8):
        print('VIII')
    elif(Numb_2convert==9):
        print('IX')
    elif(Numb_2convert==10):
        print('X')
    else:
        print('Error: Number entered is out of range.')

    next()
    hold()

# Mass and Weight
# Scientists measure an object’s mass in kilograms and its weight in
# newtons. If you know the amount of mass of an object in kilograms,
# you can calculate its weight in newtons with the following formula:

# weight = mass × 9.8

# Write a program that asks the user to enter an object’s mass, then
# calculates its weight. If the object weighs more than 500 newtons,
# display a message indicating that it is too heavy. If the object
# weighs less than 100 newtons, display a message indicating that
# it is too light.

def exercise05():
    #initialize variables
    obj_mass = 0.0
    obj_weight = 0.0
    message=''
    msg_2_heavy = 'The object is too heavy.'    # > 500 newtons
    msg_2_light = 'The object is too light.'    # < 100 newtons

    # Input: request the mass of an object.
    border="----------------------------"
    print(border+'\n MASS AND WEIGHT CONVERSION \n'+border)
    obj_mass=float(input('Enter the mass of an object in kilograms: '))

    # Calculations
    obj_weight=obj_mass*9.8
    if obj_weight > 500:
        message=(f'At {obj_weight:.2f} newtons, this object is too heavy.')
    elif obj_weight < 100:
        message=(f'At {obj_weight:.2f} newtons, this object is too light.')
    else:
        message=(f'This object at {obj_weight:.2f} newtons, is just right.')


    # Output: conversion and evaluation

    print()
    print(f'Object with mass of {obj_mass:.2f} kilograms, weights {obj_weight:.2f} newtons,')
    print()
    print(f'{border+border:^50}\n{message:^50}\n{border+border:^50}')
    next()
    hold()


# Magic Dates
# The date June 10, 1960, is special because when it is written in 
# the following format, the month times the day equals the year:

# 6/10/60

# Design a program that asks the user to enter a month (in numeric 
# form), a day, and a two-digit year. The program should then determine 
# whether the month times the day equals the year. If so, it should 
# display a message saying the date is magic. Otherwise, it should 
# display a message saying the date is not magic.

def exercise06():
    # Initialize
    xmonth=0
    xday=0
    xyear=0
    border='------------------------------'

    # input
    xmonth=int(input('month 1-12: '))
    xday=int(input('enter day 1-31: '))
    xyear=int(input('enter year up to 2 digits: '))

    # calculations
    if xmonth * xday == xyear:
        print(f'{border:^60}\n{str(xmonth)+"/"+str(xday)+"/"+str(xyear)+" is MAGIC!":^60}\n{border:^60}')
    else:
        print(f'{"Sorry, "+str(xmonth)+"/"+str(xday)+"/"+str(xmonth)+" is not magic."}')



# Color Mixer
# The colors red, blue, and yellow are known as the primary colors because they cannot be made by mixing other 
# colors. When you mix two primary colors, you get a secondary color, as shown here:
# 
# When you mix red and blue, you get purple.
# 
# When you mix red and yellow, you get orange.
# 
# When you mix blue and yellow, you get green.
# 
# Design a program that prompts the user to enter the names of two primary colors to mix. If the user enters 
# anything other than “red,” “blue,” or “yellow,” the program should display an error message. Otherwise, 
# the program should display the name of the secondary color that results.
# 
# PDL
# start
#   color1=''
#   color1_true=''
#   color2=''
#   color2_true=''
#   k=0
#   while k<2 do
#       get color0
#       if color0 == 'blue' or 'red' or 'yellow'
#           then
#               color0_true=True
#           else
#               color0_true=False
#       endif
#       color2 = color1
#       color2_true = color1_true
#       color1 = color0
#       color1_true = color0_true
#       color0 = ''
#       color0_true = ''
#       k = k+1
#   endwhile
#   if color1_true and color2_true
#       then
#           if red blue
#               then
#                   purple
#           elif red yellow
#               then
#                   orange
#           elif blue yellow
#               then
#                   green
#           else
#               both are color1
#       else
#           print(1 or both are not primary colors)
#stop

def exercise07():
    # Initialize
    color0=''
    color1=''
    color2=''
    color0_true=''
    color1_true=''
    color2_true=''
    border='-------------------------'
    title='COLOR MIXER'
    print(f'{border:^50}\n{title:^50}\n{border:^50}')
    next()

    # Input
    k=0
    while k<2:
        color0=input('Enter a primary color [blue, red, yellow]: ')
        if (color0=='blue') or (color0=='red') or (color0=='yellow'):
            color0_true=True
        else:
            color0_true=False
        color2=color1
        color1=color0
        color2_true=color1_true
        color1_true=color0_true
        k=k+1
        next()
    if color1_true and color2_true:
        if (color1+color2=='redblue') or (color2+color1=='redblue'):
            print(f'{color1} & {color2} make purple')
        elif (color1+color2=='redyellow') or (color2+color1=='redyellow'):
            print(f'{color1} & {color2} make orange')
        elif (color1+color2=='blueyellow') or (color2+color1=='blueyellow'):
            print(f'{color1} & {color2} make green')
        else:
            print(f'both are {color1}')
    else:
        if (color1_true and color2_true):
            print(f'both {color1} and {color2} are',end=" ")
        elif not(color1_true):
            print(f'{color1} is',end=" ")
        else:
            print(f'{color2} is',end=" ")
        print('not a primary color')
    next()
    hold()



# Hot Dog Cookout Calculator
# Assume hot dogs come in packages of 10, and hot dog buns come in packages 
# of 8. Write a program that calculates the number of packages of hot dogs 
# and the number of packages of hot dog buns needed for a cookout, with the 
# minimum amount of leftovers. The program should ask the user for the number 
# of people attending the cookout and the number of hot dogs each person will 
# be given. The program should display the following details:
# 
# The minimum number of packages of hot dogs required
# 
# The minimum number of packages of hot dog buns required
# 
# The number of hot dogs that will be left over
# 
# The number of hot dog buns that will be left over

# start:
#     initialize
#     dog_in_pack = 10
#     bun_in_pack = 8
#     attending = 0
#     per_attending = 0
#     servings = 0
#     dog_packs = 0
#     bun_packs = 0
# 
#     get attending
#     get per_attending
# 
#     servings = attending * per_attending
#     if servings % dog_in_pack != 0
#         then
#             dog_packs = 1 + servings / dog_in_pack
#         else
#             dog_packs = servings / dog_in_pack
#     if servings % bun_in_packs != 0
#         then
#             bun_packs = 1 + servings / bun_in_pack
#         else
#             bun_packs = servings / bun_in_pack
#     print(dog_packs, servings % dog_in_pack)
#     print(bun_packs, servings % bun_in_pack)
# stop

def exercise08():
    # initialize GLOBAL
    DOG_IN_PACK = 10
    BUN_IN_PACK = 8
    BORDER = '-------------------------'
    TITLE='Hot Dog Cookout Calculator'
    # initialize COUNTERS
    attending = 0
    per_attending = 0
    # initialize CALCULATIONS
    servings = 0
    dog_packs = 0
    bun_packs = 0
    dog_remain = 0
    bun_remain = 0

    #Input
    print(f'{BORDER:^50}\n{TITLE:^50}\n{BORDER:^50}')
    next()
    attending=int(input('How many people will be attending the cookout? '))
    per_attending=int(input('How many hot dog will each attendee be given? '))

    #Calculations
    servings=attending * per_attending
    if servings % DOG_IN_PACK != 0:
        dog_packs=1
        dog_remain=servings % DOG_IN_PACK
    if servings % BUN_IN_PACK !=0:
        bun_packs=1
        bun_remain=servings % BUN_IN_PACK
    dog_packs=dog_packs + int(servings / DOG_IN_PACK)
    bun_packs=bun_packs + int(servings / BUN_IN_PACK)

    #Output

    next()
    print(f'{dog_packs} hot dog packs are needed and {dog_remain} will remain.')
    print(f'{bun_packs} hot dog bun packages are needed and {bun_remain} will remain.')
    next()
    hold()      




# Roulette Wheel Colors
# On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:
# 
# Pocket 0 is green.
# 
# For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black.
# 
# For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red.
# 
# For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black.
# 
# For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red.

# Write a program that asks the user to enter a pocket number and displays whether the pocket is green, 
# red, or black. The program should display an error message if the user enters a number that is outside 
# the range of 0 through 36.

# start
#     initialize
#     pattern=0
#     pocket_color=''
# 
#     input
#     get pocket_number
# 
#     calculations
#     if pocket_number <0 or >36
#         print(error)
#     else
#         if pocket_number == 0
#             pattern = 1
#         elif pocket_number <=10
#             pattern = 2
#         elif pocket_number <= 18
#             pattern = 3
#         elif pocket_number <= 28
#             pattern = 2
#         else:
#             pattern = 3
#     
#         if pattern==1
#             if pocket_number%2 ==0
#                 pocket_color='black'
#             else pocket_color='red'
#         elif pattern==2
#             if pocket_number%2 ==0
#                 pocket_color='red'
#             else pocket_color='black'
#         else pocket_color='green'
# 
#     output
#     print(pocket_color)
# stop

def exercise09():
    # initialize CONSTANTS
    BORDER='-------------------------'
    TITLE='Roulette Wheel Colors'
    #initialize variables
    pattern=0   # 1=green 2=black(even)/red(odd) 3=red(even)/black(odd)
    pocket_number=0
    pocket_color=''

    # input
    print(f'{BORDER:^25}\n{TITLE:^25}\n{BORDER:^25}')
    next()
    pocket_number=int(input('Enter a number between [0-36]: '))

    # calculations
    if (pocket_number<0) or (pocket_number>36):
        print('Error: The number entered is outside the range of [0-36].')
    else:
        if pocket_number==0:
            pattern=1
        elif pocket_number<=10:
            pattern=2
        elif pocket_number<=18:
            pattern=3
        elif pocket_number<=28:
            pattern=2
        else:
            pattern=3
        
        if pattern==2:
            if pocket_number%2==0:  # even
                pocket_color='black'
            else:
                pocket_color='red'
        elif pattern==3:
            if pocket_number%2==0:  # even
                pocket_color='red'
            else:
                pocket_color='black'
        else:   # pocket_number=0
            pocket_color='green'
    
    # output
    next()
    print(f'The pocket number {pocket_number} is {pocket_color}.')
    next()
    hold()

# Money Counting Game
# Create a change-counting game that gets the user to enter the number 
# of coins required to make exactly one dollar. The program should prompt 
# the user to enter the number of pennies, nickels, dimes, and quarters. 
# If the total value of the coins entered is equal to one dollar, the 
# program should congratulate the user for winning the game. Otherwise, 
# the program should display a message indicating whether the amount 
# entered was more than or less than one dollar.

# start
#     initialize
#     GOAL=100
#     PENNY_V=1
#     NICKLE_V=5
#     DIME_V=10
#     QUARTER_V=25
#     penny=0
#     nickle=0
#     dime=0
#     quarter=0
#     total=0
# 
#     input
#     pennies
#     nickles
#     dimes
#     quarters
# 
#     calculation
#     total=(penny*PENNY_V)+(nickle*NICKLE_V)+(dime*DIME_V)+(quarter*QUARTER_V)
# 
#     output
#    if total==100
#         then
#             'winner!'
#     elif total>100
#         then
#             'too high'
#     else
#         'too low'
# stop

def exercise10():
    # initialize CONSTANTS
    TITLE='Money Counting Game'
    BORDER='--------------------'
    GOAL=1
    PENNY_V=.01
    NICKLE_V=.05
    DIME_V=.10
    QUARTER_V=.25

    # initialize variables
    penny=0
    nickle=0
    dime=0
    quarter=0
    total=0

    # input
    print(f'{BORDER:^30}\n{TITLE:^30}\n{BORDER:^30}')
    next()
    print('Instructions:')
    print('Enter the number of coins required to total $1.00')
    print('Enter quantity of each coin when prompted.')
    next()
    print('coin     \tvalue\tqty')
    penny=int(input('[PENNY]  \t$.01\t'))
    nickle=int(input('[NICKLE] \t$.05\t'))
    dime=int(input('[DIME]   \t$.10\t'))
    quarter=int(input('[QUARTER]\t$.25\t'))

    # calculation
    total=(penny*PENNY_V)+(nickle*NICKLE_V)+(dime*DIME_V)+(quarter*QUARTER_V)

    # output
    next()
    if total==1.0:
        print('WINNER! Exactly $1.00')
    elif total>1.0:
        print(f'Too high at ${total:,.2f}.')
    else:
        print(f'Too low at ${total:,.2f}.')
    next()
    hold()

# Book Club Points
# Serendipity Booksellers has a book club that awards points 
# to its customers based on the number of books purchased 
# each month. The points are awarded as follows:
# 
# If a customer purchases 0 books, he or she earns 0 points.
# If a customer purchases 2 books, he or she earns 5 points.
# If a customer purchases 4 books, he or she earns 15 points.
# If a customer purchases 6 books, he or she earns 30 points.
# If a customer purchases 8 or more books, he or she earns 60 points.
# 
# Write a program that asks the user to enter the number of 
# books that he or she has purchased this month, then displays 
# the number of points awarded.

# start
#     initialize
#     books=0
#     points=0
# 
#     input
#     books
# 
#     calculation
#     if books>=8
#         60 points
#     elif books>=6
#         30 points
#     elif books>=4
#         15 points
#     elif books>=2
#         5 points
#     else
#         0 points
# 
#     output
#     points
# stop

def exercise11():
    # initialize CONSTANT
    TITLE='Book Club Points'
    BORDER='---------------------'
    
    # initialize variables
    books=0
    points=0

    # input
    print(f'{BORDER:^30}\n{TITLE:^30}\n{BORDER:^30}')
    next()
    print('Instructions:')
    print('Enter the number of books purchased in a month.')
    print('The earned Book Club points will be returned.')
    next()
    books=int(input('How many books were purchased in a month? '))

    # calculations
    if books>=8:
        points=60
    elif books>=6:
        points=30
    elif books>=4:
        points=15
    elif books>=2:
        points=5
    else:
        points=0
    
    # output
    next()
    print(f'Customer has earned {points} points.')
    next()
    hold()

# Software Sales
# A software company sells a package that retails for $99. 
# Quantity discounts are given according to the following table:
# 
# Quantity	    Discount
# 10–19	        10%
# 20–49	        20%
# 50–99	        30%
# 100 or more	40%
# 
# Write a program that asks the user to enter the number of 
# packages purchased. The program should then display the 
# amount of the discount (if any) and the total amount 
# of the purchase after the discount.
# 
# start
#     initialize
#     COST=0.0
#     quantity=0
#     discount=0.0
# 
#     input
#     quantity
# 
#     calculation
#     if quantity>=100
#         discount=.4
#     elif quantity>=50
#         discount=.3
#     elif quantity>=20
#         discount=.2
#     elif quantity>=10
#         discount=.1
#     else
#         discount=0.0
# 
#     output
#     print cost*quantity*discount
# stop

def exercise12():
    # initialize CONSTANT
    TITLE='Software Sales'
    BORDER='---------------------'

    # initialize variables
    COST=99.0
    quantity=0
    discount=0.0
    total=0.0
    savings=0.0
    grand_total=0.0

    # input
    print(f'{BORDER:^30}\n{TITLE:^30}\n{BORDER:^30}')
    next()
    print('Instructions:')
    print('Enter the number of packages purchased.')
    print('The cost and related discounts will be provided.')
    next()
    quantity=int(input('Software Packages:\t'))

    # calculations
    if quantity>=100:
        discount=.4
    elif quantity>=50:
        discount=.3
    elif quantity>=20:
        discount=.2
    elif quantity>=10:
        discount=.2
    else:
        discount=0.0
    total=COST*quantity
    savings=COST*quantity*discount
    grand_total=total-savings

    # output
    next()
    print('Description     \tQty\tAmount')
    print(f'Software Package\t{quantity}\t${total:,.2f}')
    if discount>0.0:
        print(f'Discount        \t{discount:.0%}\t${savings:,.2f}')
    print(f'TOTAL           \t\t${grand_total:,.2f}')
    next()
    hold()

# Shipping Charges
# The Fast Freight Shipping Company charges the following rates:
# 
# Weight of Package	Rate per Pound
# 2 pounds or less	$1.50
# Over 2 pounds but not more than 6 pounds	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# 
# Write a program that asks the user to enter the weight of a 
# package then displays the shipping charges.

# start
#     initialize
#     weight=0.0
#     charges=0.0
# 
#     input
#     weight
# 
#     calculation
#     if weight>10.0
#         charges=4.75
#     elif weight>6.0
#         charges=4.0
#     elif weight>2.0
#         charges=3.0
#     else
#         charges=1.5
# 
#     output
#     print charges
# stop

def exercise13():
    # initialize CONSTANT
    TITLE='Shipping Charges'
    BORDER='---------------------'

    # initialize variables
    weight=0.0
    charges=0.0

    # input
    print(f'{BORDER:^30}\n{TITLE:^30}\n{BORDER:^30}')
    next()
    print('Instructions:')
    print('Enter the weight of the package.')
    print('The related costs will be provided.')
    next()
    weight=float(input('Enter the weight of the package: '))

    # calculations
    if weight>10:
        charges=4.75
    elif weight>6:
        charges=4.0
    elif weight>2:
        charges=3.0
    else:
        charges=1.5

    # output
    next()
    print(f'Cost ${charges:,.2f}.')
    next()
    hold()


# Body Mass Index
# Write a program that calculates and displays a person’s body 
# mass index (BMI). The BMI is often used to determine whether a 
# person is overweight or underweight for his or her height. A 
# person’s BMI is calculated with the following formula:
# 
# BMI = weight * 703 / (height**2)
#
# where weight is measured in pounds and height is measured in inches. 
# The program should ask the user to enter his or her weight and height, 
# then display the user’s BMI. The program should also display a message 
# indicating whether the person has optimal weight, is underweight, or 
# is overweight. A person’s weight is considered to be optimal if his 
# or her BMI is between 18.5 and 25. If the BMI is less than 18.5, the 
# person is considered to be underweight. If the BMI value is greater 
# than 25, the person is considered to be overweight.
# 
# start
#     init
#     weight=0.0
#     height=0.0
#     bmi=0.0
#     state='' (optimal=18.5-25, overweight>25, underweight<18.5)
# 
#     input
#     weight
#     height
# 
#     calc
#     bmi = weight * 703 / (height**2)
#     if bmi<18.5
#         then
#             state='underweight'
#     elif bmi<=25
#         then
#             state='optimal'
#     else
#         state='overweight'
# 
#     output
#     print(bmi)
#     print(state)
# stop

def exercise14():
    # initialize CONSTANT
    TITLE='Body Mass Index'
    BORDER='---------------------'

    # initialize variables
    weight=0.0
    height=0.0
    bmi=0.0
    state=''    #optimal=18.5-25, overweight>25, underweight<18.5)

    # input
    print(f'{BORDER:^30}\n{TITLE:^30}\n{BORDER:^30}')
    next()
    print('Instructions:')
    print('Enter the patients weight in pounds (lbs) and')
    print('height in inches (in.) to calculate their BMI')
    print('and report on their current state [Underweight, Optimal, Overweight].')
    next()
    weight=float(input("Patient's weight in pounds: "))
    height=float(input("Patient's height in inches: "))

    # calculations
    bmi=weight*703/(height**2)
    if bmi>25:
        state='overweight'
    elif bmi<18.5:
        state='underweight'
    else:
        state='optimal'

    # output
    next()
    print(f"The patient's bmi is:           {bmi:>15,.1f}")
    print(f"The patient's is classified as: {state:>15}")
    next()
    hold()

# Time Calculator
# Write a program that asks the user to enter a number of seconds and works as follows:
# 
# There are 60 seconds in a minute. If the number of seconds entered by the user is 
# greater than or equal to 60, the program should convert the number of seconds to minutes and seconds.
# 
# There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater 
# than or equal to 3,600, the program should convert the number of seconds to hours, minutes, and seconds.
# 
# There are 86,400 seconds in a day. If the number of seconds entered by the user is greater 
# than or equal to 86,400, the program should convert the number of seconds to days, hours, minutes, and seconds.

# start
#     init
#     SECONDS_IN_MINUTE=60
#     SECONDS_IN_HOUR=3600
#     SECONDS_IN_DAY=86400
#     seconds=0
#     seconds_remain=0
#     minutes=0
#     hours=0
#     days0
# 
#     input
#     seconds
#     seconds_remain=seconds
# 
#     calc
#     days=int(seconds_remain/SECONDS_IN_DAY)
#     seconds_remain=seconds_remain%SECONDS_IN_DAY
#     hours=int(seconds_remain/SECONDS_IN_HOUR)
#     seconds_remain=seconds_remain%SECONDS_IN_HOUR
#     minutes=int(seconds_remain/SECONDS_IN_MINUTE)
#     seconds_remain=seconds_remain%SECONDS_IN_MINUTE# 
# 
#     output
#     print(days, mintes,seconds_remain)
# stop

def exercise15():
    # initialize CONSTANT
    TITLE='Time Calculator'
    BORDER='---------------------'
    D='[Days]'
    H='[Hours]'
    M='[Minutes]'
    S='[Seconds]'
    U='-------'
    SECONDS_IN_MINUTE=60
    SECONDS_IN_HOUR=3600
    SECONDS_IN_DAY=86400

    # initialize variables     
    seconds=0
    seconds_remain=0
    minutes=0
    hours=0
    days=0

    # input
    print(f'{BORDER:^30}\n{TITLE:^30}\n{BORDER:^30}')
    next()
    print('Instructions:')
    print('Enter a whole number to represents seconds.')
    print('The number will be divided in days, hours, minutes, seconds.')
    next()
    seconds=int(input("Seconds: "))
    seconds_remain=seconds

    # calculations
    days=int(seconds_remain/SECONDS_IN_DAY)
    seconds_remain=seconds_remain%SECONDS_IN_DAY
    hours=int(seconds_remain/SECONDS_IN_HOUR)
    seconds_remain=seconds_remain%SECONDS_IN_HOUR
    minutes=int(seconds_remain/SECONDS_IN_MINUTE)
    seconds_remain=seconds_remain%SECONDS_IN_MINUTE

    # output
    next()
    print(f'{D:^10}{H:^10}{M:^10}{S:^10}')
    print(f'{U:^10}{U:^10}{U:^10}{U:^10}')
    print(f'{days:^10}{hours:^10}{minutes:^10}{seconds_remain:^10}')
    next()
    hold()



# February Days
# The month of February normally has 28 days. But if it is a leap year, 
# February has 29 days. Write a program that asks the user to enter a 
# year. The program should then display the number of days in February 
# that year. Use the following criteria to identify leap years:
# 
# Determine whether the year is divisible by 100. If it is, then it 
# is a leap year if and only if it is also divisible by 400. For 
# example, 2000 is a leap year, but 2100 is not.
# 
# If the year is not divisible by 100, then it is a leap year if and 
# only if it is divisible by 4. For example, 2008 is a leap year, 
# but 2009 is not.
# 
# Here is a sample run of the program:
# 
# Enter a year: 2008  [Enter]
#  In 2008 February has 29 days.

# start
#     init
#     year=0
#     days=0
# 
#     input
#     year
# 
#     calc
#     if year/100
#         then
#             if year/400
#                 then
#                     days=29
#             else
#                 days=28
#     else
#         if year/4
#             then
#                 days=29
#         else
#             days=28
# 
#     output
#     year, days
# stop

def exercise16():
    # initialize CONSTANT
    TITLE='February Days'
    BORDER='---------------------'

    # initialize variables     
    year=0
    days=0

    # input
    print(f'{BORDER:^30}\n{TITLE:^30}\n{BORDER:^30}')
    next()
    print('Instructions:')
    print('Enter a year and the number of days in February')
    print('will be returned to identify the Leap Years.')
    next()
    year=int(input("Enter a year: "))
    
    # calculations
    days=28
    if year%100==0:
        if year%400==0:
            days=29
    else:
        if year%4==0:
            days=29

    # output
    next()
    print(f'In {year} February has {days} days.')
    next()
    hold()

# Wi-Fi Diagnostic Tree
# Figure 3-19 shows a simplified flowchart for troubleshooting a bad Wi-Fi 
# connection. Use the flowchart to create a program that leads a person 
# through the steps of fixing a bad Wi-Fi connection. Here is an example of the 
# program’s output:
# 
# Reboot the computer and try to connect.
#  Did that fix the problem? no [Enter]
#  Reboot the router and try to connect.
#  Did that fix the problem? yes [Enter]
# Notice the program ends as soon as a solution is found to the problem. Here is another example of the program’s output:
# 
# Reboot the computer and try to connect.
#  Did that fix the problem? no  [Enter]
#  Reboot the router and try to connect.
#  Did that fix the problem? no  [Enter]
#  Make sure the cables between the router and modem are plugged in firmly.
#  Did that fix the problem? no  [Enter]
#  Move the router to a new location.
#  Did that fix the problem? no  [Enter]
#  Get a new router.

# start
#     init
#     repair_step=0
#     fixed=''
#     message=''
# 
#     input_calc_output
#     while repair_step<4 and fixed=='':
#         if repair_step==0
#             then
#                 message='Reboot comp'
#         elif repair_step==1
#             then
#                 message='Reboot router'
#         elif repair_step==2
#             then
#                 message='check cable'
#         elif repair_step==3
#             then
#                 message='move router'
#         print(message)
#         fixed=input('Did that fix the problem? [y/n]')
#         if fixed=='n'
#             then
#                 repair_step=repair_step+1
#         if fixed!='y'
#             then
#                 fixed=''
#     endwhile
#     if fixed!='y'
#         then
#             print('get new router')
# stop

def exercise17():
    # initialize CONSTANT
    TITLE='Wi-Fi Diagnostic Tree'
    BORDER='---------------------'

    # initialize variables     
    repair_step=0
    fixed=''
    message='Reboot the computer and try to connect.'

    # input
    print(f'{BORDER:^30}\n{TITLE:^30}\n{BORDER:^30}')
    next()
    print('Instructions:')
    print('Follow the steps to troubleshooting a bad Wi-Fi.')
    print('After each step answer with y or n.')
    next()
    
    # calculations
    # 1st step is required
    print(message)
    while repair_step<4 and fixed=='':
        # input answer to repair step
        fixed=input(' Did that fix the problem? [y/n] ')
        # repair instructions passed as variable
        if repair_step==0:
            message=' Reboot the router and try to connect.'
        elif repair_step==1:
            message=' Make sure the cables between the router and modem are plugged in firmly.'
        elif repair_step==2:
            message=' Move the router to a new location.'
        else:
            message=' Get a new router.'
        # filter out when repaired
        if fixed=='y':
            print()
        # if not successful then sequence to next step and reset answer
        elif fixed=='n':
            print(message)
            repair_step=repair_step+1
            fixed=''
        # rest answer assume bad data entry
        else:
            fixed=''

    # output
    next()
    hold()


# Restaurant Selector
# You have a group of friends coming to visit for your high school reunion, 
# and you want to take them out to eat at a local restaurant. You aren’t sure 
# if any of them have dietary restrictions, but your restaurant choices are as follows:
# 
# Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
# 
# Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
# 
# Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# 
# Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
# 
# The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# 
# Write a program that asks whether any members of your party are vegetarian, 
# vegan, or gluten-free, to which then displays only the restaurants to which 
# you may take the group. Here is an example of the program’s output:
# 
# Is anyone in your party a vegetarian? yes  [Enter]
#  Is anyone in your party a vegan? no  [Enter]
#  Is anyone in your party gluten-free? yes  [Enter]
#  Here are your restaurant choices:
#     Main Street Pizza Company
#     Corner Cafe
#     The Chef's Kitchen
# Here is another example of the program’s output:
# 
# Is anyone in your party a vegetarian? yes  [Enter]
#  Is anyone in your party a vegan? yes [Enter]
#  Is anyone in your party gluten-free? yes  [Enter]
#  Here are your restaurant choices:
#     Corner Cafe
#     The Chef's Kitchen

# start
#     init
#     vegetarian=''
#     vegan=''
#     gluten_free=''
#     a=False #vegetarian
#     b=False #vegan
#     c=False #gluten-free
# 
#     input
#     vegetarian
#     vegan
#     gluten_free
# 
#     calc_output
#     if ('n'==vegetarian) and ('n'==vegan) and ('n'==gluten_free)
#         then
#             print ('Joe’s Gourmet Burgers')
#     if (True or vegetarian) and ('n'==vegan) and (True or gluten_free)
#         then
#             print('Main Street Pizza Company')
#     if (True or vegetarian) and (True or vegan) and (True or gluten_free) 
#         then
#             print('Corner Café')
#     if (True or vegetarian) and ('n'==vegan) and ('n'==gluten_free) 
#         then
#             print('Mama’s Fine Italian')
#     if (True or vegetarian) and (True or vegan) and (True or gluten_free) 
#         then
#             print('The Chef’s Kitchen')
# stop

def exercise18():
    # initialize CONSTANT
    TITLE='Restaurant Selector'
    BORDER='---------------------'

    # initialize variables     
    vegetarian=''
    vegan=''
    gluten_free=''
    a=False #vegetarian
    b=False #vegan
    c=False #gluten-free
    get_restrictions=0
    restrictions=''

    # input
    # header and intro
    print(f'{BORDER:^30}\n{TITLE:^30}\n{BORDER:^30}')
    next()
    print('Instructions:')
    print('Answer a few questions and a list of')
    print('appropriate restaurants will be listed.')
    next()

    # loop to collect 3 answers.
    while get_restrictions<3:
        print('Is anyone in your party',end=' ')
        if get_restrictions==0:
            restrictions=input('a vegetarian? [y/n] ')
        elif get_restrictions==1:
            restrictions=input('a vegan? [y/n] ')
        else:
            restrictions=input('gluten-free? [y/n] ')
        # validate input will repeat the loop until a match is made
        if restrictions=='y' or restrictions=='n':
            vegetarian=vegan
            vegan=gluten_free
            gluten_free=restrictions
            restrictions=''
            get_restrictions=get_restrictions+1

    # output
    next()
    # If restaurant does not meet a restriction the inputs will be analized
    if ('n'==vegetarian) and ('n'==vegan) and ('n'==gluten_free):
        print ("Joe’s Gourmet Burgers")
    if (True or vegetarian) and ('n'==vegan) and (True or gluten_free):
        print('Main Street Pizza Company')
    if (True or vegetarian) and (True or vegan) and (True or gluten_free):
        print('Corner Café')
    if (True or vegetarian) and ('n'==vegan) and ('n'==gluten_free):
        print("Mama’s Fine Italian")
    if (True or vegetarian) and (True or vegan) and (True or gluten_free):
        print("The Chef’s Kitchen")

    # output
    next()
    hold()

# Turtle Graphics: Hit the Target Modification
# Enhance the hit_the_target.py program that you saw in Program 3-9 so that, 
# when the projectile misses the target, it displays hints to the user indicating 
# whether the angle and/or the force value should be increased or decreased. 
# For example, the program should display messages such as 'Try a greater angle' 
# and 'Use less force.'

def exercise19():
    # Hit the Target Game 
    import turtle

    # Named constants
    SCREEN_WIDTH = 600     # Screen width
    SCREEN_HEIGHT = 600    # Screen height
    TARGET_LLEFT_X = 75   # Target's lower-left X
    TARGET_LLEFT_Y = -200   # Target's lower-left Y
    TARGET_WIDTH = 25      # Width of the target
    FORCE_FACTOR = 30      # Arbitrary force factor
    PROJECTILE_SPEED = 1   # Projectile's animation speed
    NORTH = 90             # Angle of north direction
    SOUTH = 270            # Angle of south direction
    EAST = 0               # Angle of east direction
    WEST = 180             # Angle of west direction

    # Setup the window.
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Draw the target.
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    turtle.pendown()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()

    # Center the turtle.
    turtle.goto(0, 0)
    turtle.setheading(EAST)
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED)

    # Get the angle and force from the user.
    import math
    TARGET_X = TARGET_LLEFT_X+(TARGET_WIDTH/2)
    TARGET_Y = TARGET_LLEFT_Y+(TARGET_WIDTH/2)
    TARGET_DISTANCE = ((TARGET_Y**2 + TARGET_X**2)**.5)/FORCE_FACTOR
    TARGET_ANGLE = math.atan2(TARGET_Y,TARGET_X)*180/math.pi

    # Test output
    # print(f'{TARGET_DISTANCE*.9}\t{TARGET_DISTANCE}\t{TARGET_DISTANCE*1.05}')
    # print(f'{TARGET_ANGLE*.95}\t{TARGET_ANGLE}\t{TARGET_ANGLE*1.05}')

    angle = float(input("Enter the projectile's angle: "))
    force = float(input("Enter the launch force (1−10): "))

    # Calculate the distance.
    distance = force * FORCE_FACTOR

    # Set the heading.
    turtle.setheading(angle)

    # Launch the projectile.
    turtle.pendown()
    turtle.forward(distance)

    # Did it hit the target?
    if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
            print('Target hit!')
    else:
        print('You missed the target.')
        VARIANCE=.05

        if distance<TARGET_DISTANCE*(1-VARIANCE):
            print('Try more force.')
        elif distance>TARGET_DISTANCE*(1+VARIANCE):
            print('Try less force.')

        if abs(angle)<abs(TARGET_ANGLE*(1-VARIANCE)):
            print('Try more angle.')
        elif abs(angle)>abs(TARGET_ANGLE*(1+VARIANCE)):
            print('Try less angle.')

    next()
    hold()


def main():
    # initialize CONSTANT
    TITLE='Chapter 2 - Exercises'
    BORDER='---------------------'
    EXERCISE=0

    # input
    print(f'{BORDER:^30}\n{TITLE:^30}\n{BORDER:^30}')
    next()
    print('Chapter 2:')
    print('Inputs, Processing, and Output (pg 31-118)')
    print('Programming Exercises')
    next()

    while EXERCISE!='0':
        next()
        EXERCISE=int(input('Chapter 2 includes 19 exercises. Select [1-19 or 0=quit]: '))
        next()

        if EXERCISE==1:
            exercise01()
        elif EXERCISE==2:
            exercise02()
        elif EXERCISE==3:
            exercise03()
        elif EXERCISE==4:
            exercise04()
        elif EXERCISE==5:
            exercise05()
        elif EXERCISE==6:
            exercise06()
        elif EXERCISE==7:
            exercise07()
        elif EXERCISE==8:
            exercise08()
        elif EXERCISE==9:
            exercise09()
        elif EXERCISE==10:
            exercise10()
        elif EXERCISE==11:
            exercise11()
        elif EXERCISE==12:
            exercise12()
        elif EXERCISE==13:
            exercise13()
        elif EXERCISE==14:
            exercise14()
        elif EXERCISE==15:
            exercise15()
        elif EXERCISE==16:
            exercise16()
        elif EXERCISE==17:
            exercise17()
        elif EXERCISE==18:
            exercise18()
        elif EXERCISE==19:
            exercise19()
        else:
            EXERCISE='0'

#***************************************************************
#
#  Function:     hold
#  Description:  Prompt to pause the screen until ready
#  Parameters:   None
#  Returns:      Nothing
#
#**************************************************************
def hold():
    dummy=input('Please enter any key to continue...')

#***************************************************************
#
#  Function:     next
#  Description:  Create a multi-line space to between input/output
#                to keep screen uncluttered
#  Parameters:   None
#  Returns:      3 blank lines
#
#**************************************************************
def next():
    print ('\n\n\n')

main()
