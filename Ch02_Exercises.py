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
#  Due Date:        09-18-2023
#
#  Instructor:      Onabajo
#
#  Chapter:         <Chapter 2>
#
#  Exercise:        <Exercise>
#
#  Description:
#  
#
#***************************************************************

def next():
    print()
    print()
    print()

# Write a program that displays the following information:
# Your name
# Your address, with city, state, and ZIP
# Your telephone number
# Your college major

def exercise01():
    print('Michael Villarreal')
    print('1010 Main St')
    print('Round Rock, Texas  78665')
    print('512-555-0000')
    print('Associates of Applied Science in Cybersecurity') 

# Sales Prediction
# A company has determined that its annual profit is typically 23 percent
# of total sales. Write a program that asks the user to enter the projected
# amount of total sales, then displays the profit that will be made from
# that amount.
# Hint: Use the value 0.23 to represent 23 percent.

def exercise02():
  ANNUAL_PROFIT = float(.23)

  total_sales = float(input('What are the total sales reported: '))
  next()
  print(f'Expected profit is: ${total_sales * ANNUAL_PROFIT:,.2f}')

# Land Calculation
# One acre of land is equivalent to 43,560 square feet. Write a program
# that asks the user to enter the total square feet in a tract of land and
# calculates the number of acres in the tract.
#
# Hint: Divide the amount entered by 43,560 to get the number of acres.

def exercise03():
    FT_IN_ACRE = 43560

    total_ft = int(input('Enter the total number of square feet in a tract of land: '))
    next()
    print(f'The tract contains a total of {total_ft / FT_IN_ACRE:,.2f} acres')
    
# Total Purchase
# A customer in a store is purchasing five items. Write a program that asks
# for the price of each item, then displays the subtotal of the sale, the
# amount of sales tax, and the total. Assume the sales tax is 7 percent.

def exercise04():
    SALES_TAX = .07
    subtotal = 0
    price = 0

    price = float(input('Enter price number 1: '))
    subtotal = subtotal + price
    price = float(input('Enter price number 2: '))
    subtotal = subtotal + price
    price = float(input('Enter price number 3: '))
    subtotal = subtotal + price
    price = float(input('Enter price number 4: '))
    subtotal = subtotal + price
    price = float(input('Enter price number 5: '))
    subtotal = subtotal + price

    next()
    print(f'subtotal: ${subtotal:10,.2f}')
    print(f'tax:      ${subtotal * SALES_TAX:10,.2f}')
    print(f'total:    ${subtotal * (1 + SALES_TAX):10,.2f}')

# Distance Traveled
# Assuming there are no accidents or delays, the distance that a car travels
# down the interstate can be calculated with the following formula:
#
# A car is traveling at 70 miles per hour. Write a program that displays
# the following:
#
# The distance the car will travel in 6 hours
#
# The distance the car will travel in 10 hours
#
# The distance the car will travel in 15 hours

def exercise05():
    #Traveling SPEED miles per hour
    SPEED = 70
    CHECKPOINT1 = 6
    CHECKPOINT2 = 10
    CHECKPOINT3 = 15

    print('Given a speed of '+str(SPEED)+'MPH, distance traveled in:')
    print(str(CHECKPOINT1)+' hours is '+str(SPEED*CHECKPOINT1)+' miles.')
    print(str(CHECKPOINT2)+' hours is '+str(SPEED*CHECKPOINT2)+' miles.')
    print(str(CHECKPOINT3)+' hours is '+str(SPEED*CHECKPOINT3)+' miles.')

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
    
def exercise06():
    STATE_TAX = .05
    COUNTY_TAX = .025

    purchase_amt=float(input('Enter purchase amount: '))
    next()
    print(f'${purchase_amt:10,.2f}',' :Total')
    print(f'${purchase_amt * STATE_TAX:10,.2f}',' :State Tax')
    print(f'${purchase_amt * COUNTY_TAX:10,.2f}',' :County Tax')
    print(f'${purchase_amt * (1 + STATE_TAX + COUNTY_TAX):10,.2f}',' :Grand Total')
    
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
    exercise01()
    next()
    exercise02()
    next()
    exercise03()
    next()
    exercise04()
    next()
    exercise05()
    next()
    exercise06()
    next()
    exercise07()
    next()
    exercise08()
    next()
    exercise09()
    next()
    exercise10()
    next()
    exercise11()
    next()
    exercise11()
    next()
    exercise12()
    next()
    exercise13()
    next()
    exercise14()
    next()
    exercise15()

main()
