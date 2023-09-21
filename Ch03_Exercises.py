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



# Miles-per-Gallon
# A car’s miles-per-gallon (MPG) can be calculated with the following formula:
# MPG = Milesdriven ÷ Gallonsofgasused
# Write a program that asks the user for the number of miles driven and the
# gallons of gas used. It should calculate the car's MPG and display the result.

def exercise07():
    miles = int(input('How many miles have been driven: '))
    gallons = int(input('How many gallons of gas have been consumed: '))

    print(f'Your vehicle is averaging {miles / gallons} MPG')

# Tip, Tax, and Total
# Write a program that calculates the total amount of a meal purchased at a
# restaurant. The program should ask the user to enter the charge for the
# food, then calculate the amounts of a 18 percent tip and 7 percent sales
# tax. Display each of these amounts and the total.

def exercise08():
    TAX = .07
    TIP = .18

    food = float(input('Enter cost of meal: '))
    next()
    print(f'${food:15,.2f}'+' : Meal Total')
    print(f'${food * TAX:15,.2f}'+' : Tax')
    print(f'${food * TIP:15,.2f}'+' : Tip')
    print(f'${food * (1 + TAX + TIP):15,.2f}'+' : Grand Total')

# Celsius to Fahrenheit Temperature Converter
# Write a program that converts Celsius temperatures to Fahrenheit temperatures.
# The formula is as follows:
# F = ((9/5) * C) + 32)
# The program should ask the user to enter a temperature in Celsius, then
# display the temperature converted to Fahrenheit.

def exercise09():
    C_temp = int(input('Enter a tempurture in degree Celcius: '))
    next()
    print(((9/5) * C_temp) + 32)

# Ingredient Adjuster
# A cookie recipe calls for the following ingredients:
#
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour
#
# The recipe produces 48 cookies with this amount of the ingredients.
# Write a program that asks the user how many cookies he or she wants to make,
# then displays the number of cups of each ingredient needed for the
# specified number of cookies.

def exercise10():
    BASE_COUNT = 48
    SUGAR = 1.5
    BUTTER = 1
    FLOUR = 2.75

    target_count = int(input('Enter the number of cookies desired: '))
    next()
    print(str(target_count)+' cookie ingredients needed')
    print(f'sugar {SUGAR * target_count / BASE_COUNT:<,.2f} cups')
    print(f'butter {BUTTER * target_count / BASE_COUNT:<,.2f} cups')
    print(f'flour {FLOUR * target_count / BASE_COUNT:<,.2f} cups')

# Male and Female Percentages
# Write a program that asks the user for the number of males and the number
# of females registered in a class. The program should display the percentage
# of males and females in the class.
#
# Hint: Suppose there are 8 males and 12 females in a class. There are
# 20 students in the class. The percentage of males can be calculated as
# 8÷20=0.4, or 40%. The percentage of females can be calculated as
# 12÷20=0.6, or 60%.

def exercise11():
    males = 0
    females = 0

    males=int(input('how many males in class: '))
    females=int(input('how many females in class: '))
    next()
    print(f'Males: {100 * (males / (males + females)):.1f}%')
    print(f'Females: {100 * (females / (males + females)):.1f}%')

# Stock Transaction Program
# Last month, Joe purchased some stock in Acme Software, Inc. Here are the
# details of the purchase:
#
# The number of shares that Joe purchased was 2,000.
#
# When Joe purchased the stock, he paid $40.00 per share.
#
# Joe paid his stockbroker a commission that amounted to 3 percent of the
# amount he paid for the stock.
#
# Two weeks later, Joe sold the stock. Here are the details of the sale:
#
# The number of shares that Joe sold was 2,000.
#
# He sold the stock for $42.75 per share.
#
# He paid his stockbroker another commission that amounted to 3 percent of
# the amount he received for the stock.
#
# Write a program that displays the following information:
#
# The amount of money Joe paid for the stock.
#
# The amount of commission Joe paid his broker when he bought the stock.
#
# The amount for which Joe sold the stock.
#
# The amount of commission Joe paid his broker when he sold the stock.
#
# Display the amount of money that Joe had left when he sold the stock and
# paid his broker (both times). If this amount is positive, then Joe made
# a profit. If the amount is negative, then Joe lost money.

def exercise12():
    SB_COMMISSION = .03
    BOUGHT = 2000
    BOUGHT_RATE = 40
    SOLD = 2000
    SOLD_RATE = 42.75

    print(f'Stock purchased ({BOUGHT}) for ${BOUGHT * BOUGHT_RATE:,.2f}')
    print(f'Commission paid ${BOUGHT * BOUGHT_RATE * SB_COMMISSION:,.2f}')
    print(f'Stock sold ({SOLD}) for ${SOLD * SOLD_RATE:,.2f}')
    print(f'Commission paid ${SOLD * SOLD_RATE * SB_COMMISSION:,.2f}')
    next()
    print(f'Profit/Loss: ${(SOLD * SOLD_RATE)-(SOLD * SOLD_RATE * SB_COMMISSION) - (BOUGHT * BOUGHT_RATE * SB_COMMISSION)-(BOUGHT * BOUGHT_RATE):,.2f}')

# Planting Grapevines
# A vineyard owner is planting several new rows of grapevines, and needs to
# know how many grapevines to plant in each row. She has determined that
# after measuring the length of a future row, she can use the following
# formula to calculate the number of vines that will fit in the row,
# along with the trellis end-post assemblies that will need to be
# constructed at each end of the row:
# V = (R - 2 * E)/S
#
# The terms in the formula are:
#
# V is the number of grapevines that will fit in the row.
#
# R is the length of the row, in feet.
#
# E is the amount of space, in feet, used by an end-post assembly.
#
# S is the space between vines, in feet.
#
# Write a program that makes the calculation for the vineyard owner. The
# program should ask the user to input the following:
#
# The length of the row, in feet
#
# The amount of space used by an end-post assembly, in feet
#
# The amount of space between the vines, in feet
#
# Once the input data has been entered, the program should calculate and
# display the number of grapevines that will fit in the row.

def exercise13():
    R = int(input('length of th row in feet: ')) # Length
    E = int(input('amount of space used by an end-post assembly in feet: ')) # End-Post
    S = int(input('amount of space between vines in feet: ')) # Space
    next()
    print(f'Number of grapevines that will fit: {int((R - 2 * E)/S):,}')


#

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
    exercise06()
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
#    exercise11()
#    next()
#    exercise12()
#    next()
#    exercise13()
#    next()
#    exercise14()
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
