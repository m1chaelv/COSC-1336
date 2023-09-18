#***************************************************************
#
#  Developer:         Michael Villarreal
#
#  Program #:         Lab 2
#
#  File Name:         Lab1.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Due Date:          09-18-2023
#
#  Instructor:        Onabajo
#
#  Chapter:           <Chapter 2>
#
#  Description:
#   A movie theater only keeps a percentage of the revenue earned from ticket
#   sales. The remainder goes to the movie company. Write a program that
#   calculates a theater's gross and net box office profit for a night. The program
#   should ask for the name of the movie, and how many adult and children
#   tickets were sold. (The price of an adult ticket is $6.00 and a child's ticket is
#   $3.00). It should display a report similar to the one below:
#
#   Note: Assume that the theatre keeps 20% of the gross box profit.
#
#***************************************************************

#***************************************************************
#
#  Function:     main
#
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing
#
#**************************************************************
def main():

    developerInfo() # Signature




    # Initialize variables
    H1 = 'House 1'
    H2 = 'House 2'
    H3 = 'House 3'

    # Request Inputs
    # To expedite testing pre-populated data will bypass user prompts.
    # set USE_TEST to True to use test data. Set to False before promoting to prod.
    USE_TEST = False

    house()

    if USE_TEST:
        House1_init_cost = 167000
        House1_annual_fuel = 2300
        House1_tax_rate = .025

        House2_init_cost = 162000
        House2_annual_fuel = 2500
        House2_tax_rate = .025

        House3_init_cost = 175000
        House3_annual_fuel = 1850
        House3_tax_rate = .02
        cat(1,1,1,"Test Data")
    else:
        print('Enter the following information for House 1.')
        House1_init_cost = float(input('Initial cost: '))
        House1_annual_fuel = float(input('Annual fuel cost: '))
        House1_tax_rate = float(input('Tax rate: '))
        if House1_tax_rate >= 1:
            House1_tax_rate = House1_tax_rate/100
        next()

        print('Enter the following information for House 2.')
        House2_init_cost = float(input('Initial cost: '))
        House2_annual_fuel = float(input('Annual fuel cost: '))
        House2_tax_rate = float(input('Tax rate: '))
        if House2_tax_rate >= 1:
            House2_tax_rate = House2_tax_rate/100
        next()

        print('Enter the following information for House 3.')
        House3_init_cost = float(input('Initial cost: '))
        House3_annual_fuel = float(input('Annual fuel cost: '))
        House3_tax_rate = float(input('Tax rate: '))
        if House3_tax_rate >= 1:
            House3_tax_rate = House3_tax_rate/100
        next()

        cat(4,5,1,"Thank You")

    next()

    # Output
    print('Summary:')
    print('House\tInitial Cost\t5-Year Costs')
    print(f'{H1}\t${House1_init_cost:,.2f}\t${House1_init_cost+(House1_tax_rate*House1_init_cost+House1_annual_fuel)*5:,.2f}')
    print(f'{H2}\t${House2_init_cost:,.2f}\t${House2_init_cost+(House2_tax_rate*House2_init_cost+House2_annual_fuel)*5:,.2f}')
    print(f'{H3}\t${House3_init_cost:,.2f}\t${House3_init_cost+(House3_tax_rate*House3_init_cost+House3_annual_fuel)*5:,.2f}')
    next()
    print('Details:')
    print(f'{"":^20}{H1:^20}{H2:^20}{H3:^20}')
    print(f'{"Init Cost":<20}{House1_init_cost:^20,.2f}{House2_init_cost:^20,.2f}{House3_init_cost:^20,.2f}')
    print(f'{"5Y Fuel Cost":<20}{House1_annual_fuel*5:^20,.2f}{House2_annual_fuel*5:^20,.2f}{House3_annual_fuel*5:^20,.2f}')
    print(f'{"5Y Tax Cost":<20}{(House1_tax_rate*House1_init_cost)*5:^20,.2f}{(House2_tax_rate*House2_init_cost)*5:^20,.2f}{(House3_tax_rate*House3_init_cost)*5:^20,.2f}')
    print(f'{"Overall Cost":<20}{House1_init_cost+(House1_tax_rate*House1_init_cost+House1_annual_fuel)*5:^20,.2f}{House2_init_cost+(House2_tax_rate*House2_init_cost+House2_annual_fuel)*5:^20,.2f}{House3_init_cost+(House3_tax_rate*House3_init_cost+House3_annual_fuel)*5:^20,.2f}')
    next()
    print('Notes:')
    print(f'{"Annual Fuel Cost":<20}{House1_annual_fuel:^20,.2f}{House2_annual_fuel:^20,.2f}{House3_annual_fuel:^20,.2f}')
    print(f'{"Tax Rate":<20}{House1_tax_rate:^20%}{House2_tax_rate:^20%}'f'{House3_tax_rate:^20%}')


    # End of the main function

#***************************************************************
#
#  Function:     developerInfo
#
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing
#
#**************************************************************
def developerInfo():
    print('Name:     Michael Villarreal')
    print('Course:   Programming Fundamentals I')
    print('Lab: 2')
    print()
    # End of the developerInfo function

def next():
    print ()
    print ()
    print ()

def house():
    next()
    
    # ASCII Art Source: https://www.asciiart.eu/buildings-and-places/houses
    # Description: ASCII representation of a house
    # Note: No author specified on the source website.

    house_art = """
          ':.
             []_____
            /\      \ 
        ___/  \__/\__\__
    ---/\___\ |''''''|__\-- ---
       ||'''| |''||''|''|
       ``"`"`"`""))""`""`
    """

    print(house_art)

# Cat graphic print with message

def cat(ears,face,feet,message):
    # Cat Ears
    earsx = ("  /\_/\   ")
    if ears == 1:
        earsx = ("  (\_/)   ")
    if ears == 2:
        earsx = ("  (\_(\   ")
    if ears == 3:
        earsx = ("  /)_/)   ")
        

    # Cat Face
    facex = (" (=^.^=)  ")
    if face == 1:
        facex = (" (='x'=)  ")
    if face == 2:
        facex = (" (=-.-=)  ")
    if face == 3:
        facex = (" (=oxo=)  ")
    if face == 4:
        facex = (" (='.'=)  ")

    # Cat Feet
    feetx = ('(") (")_/')
    if feet == 1:
        feetx = ('(") (")_/')

    print(earsx+message+"\n"+facex+"\n"+feetx)

    ImgE1 = ("  (\_/)   ")
    ImgE2 = ("  (\_(\   ")
    ImgE3 = ("  /)_/)   ")
    ImgE4 = ("  /\_/\   ")

    # Cat Face
    ImgF1 = (" (='x'=)  ")
    ImgF2 = (" (=-.-=)  ")
    ImgF3 = (" (=oxo=)  ")
    ImgF4 = (" (='.'=)  ")
    ImgF5 = (" (=^.^=)  ")

    # Cat Feet
    ImgFT1 = ('(") (")_/')
    

# Call the main function
main()

# End of Lab 01
