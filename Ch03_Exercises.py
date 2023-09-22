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
# where weight is measured in pounds and height is measured in inches. 
# The program should ask the user to enter his or her weight and height, 
# then display the user’s BMI. The program should also display a message 
# indicating whether the person has optimal weight, is underweight, or 
# is overweight. A person’s weight is considered to be optimal if his 
# or her BMI is between 18.5 and 25. If the BMI is less than 18.5, the 
# person is considered to be underweight. If the BMI value is greater 
# than 25, the person is considered to be overweight.

def exercise14():
    next()

def exercise15():
    import turtle
    turtle.goto(50,0)
    turtle.goto(0,50)
    turtle.goto(-50,0)
    turtle.goto(50,0)
    turtle.goto(0,100)
    turtle.goto(-50,0)


def main():
    next()
#    exercise01()
#    next()
#    exercise02()
#    next()
#    exercise03()
#    next()
#    exercise04()
#    next()
#    exercise05()
#    next()
#    exercise06()
#    next()
#    exercise07()
#    next()
#    exercise08()
#    next()
#    exercise09()
#    next()
#    exercise10()
#    next()
#    exercise11()
#    next()
#    exercise12()
#    next()
#    exercise13()
#    next()
    exercise14()
#    next()
#    exercise15()

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
    print ()
    print ()
    print ()

main()
