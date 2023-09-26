#***************************************************************
#
#  Developer:         Michael Villarreal
#
#  Program #:         Lab 2
#
#  File Name:         Lab02.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Due Date:          09-20-2023
#
#  Instructor:        Onabajo
#
#  Chapter:           <Chapter 3>
#
#  Description:
#	In shopping for a new house, you must consider several factors. 
#	In this problem, the initial cost of the house, the estimated 
#	annual fuel cost, and the annual tax rate are available.. Write 
#	a program that will determine the total cost of a house after a 
#	five-year period for the following set of data.. You should be 
#	able to inspect your program output to determine the best buy.
#
#	Initial cost	Annual Fuel Cost	Tax Rate
#	$167,000	$2,500			0.025
#	$175,000	$2,300			0.025
#	$162,000	$1,850			0.020
#
#	To calculate the house cost, add the initial cost to the fuel 
#	cost for five years, then add the taxes for five years. Taxes 
#	for one year are computed by multiplying the tax rate by the 
#	initial cost. Write a program segment to display instructions 
#	to the program user.
#
#***************************************************************

#***************************************************************
#
#  Function:     main
#  Description:  The main function of the program
#  Parameters:   None
#  Returns:      Nothing
#
#**************************************************************

def complex():
    # Student Header
    developerInfo()

    # Initialize variables
    H1 = 'House 1'
    H2 = 'House 2'
    H3 = 'House 3'

    # Display "Welcome" House Graphic
    house()

    # Request Inputs
    # To expedite testing pre-populated data will bypass user prompts.
    # set USE_TEST to True to use test data. Set to False before promoting to prod.
    USE_TEST = False
    
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
        House1_tax_rate = float(input('Tax rate (ex:2.5 or .025 = 2.5%): '))
        if House1_tax_rate >= 1:
            House1_tax_rate = House1_tax_rate/100
        next()

        print('Enter the following information for House 2.')
        House2_init_cost = float(input('Initial cost: '))
        House2_annual_fuel = float(input('Annual fuel cost: '))
        House2_tax_rate = float(input('Tax rate (ex:2.5 or .025 = 2.5%): '))
        # Data cleansing and validation
        # If tax rate entered is greater than 1, assumption is user is entering whole number
        # Input data is adjusted by dividing by 100
        if House2_tax_rate >= 1:
            House2_tax_rate = House2_tax_rate/100
        next()

        print('Enter the following information for House 3.')
        House3_init_cost = float(input('Initial cost: '))
        House3_annual_fuel = float(input('Annual fuel cost: '))
        House3_tax_rate = float(input('Tax rate (ex:2.5 or .025 = 2.5%): '))
        # Data cleansing and validation
        # If tax rate entered is greater than 1, assumption is user is entering whole number
        # Input data is adjusted by dividing by 100
        if House3_tax_rate >= 1:
            House3_tax_rate = House3_tax_rate/100
        next()

        cat(4,5,1,"Thank You")

    next()

    # Output
    # Calculations inline:
    # 5-Year Costs = Initial Cost + 5 * (Tax Rate * Inital Cost + Annual Fuel Costs)
    print('Summary:')
    print('House\tInitial Cost\t5-Year Costs')
    print(f'{H1}\t${House1_init_cost:,.2f}\t${House1_init_cost+(House1_tax_rate*House1_init_cost+House1_annual_fuel)*5:,.2f}')
    print(f'{H2}\t${House2_init_cost:,.2f}\t${House2_init_cost+(House2_tax_rate*House2_init_cost+House2_annual_fuel)*5:,.2f}')
    print(f'{H3}\t${House3_init_cost:,.2f}\t${House3_init_cost+(House3_tax_rate*House3_init_cost+House3_annual_fuel)*5:,.2f}')
    next()

    # Calculations inline:
    # 5-Year Fuel Costs = 5 * Annual Fuel Costs
    # 5-Year Tax Costs = 5 * (Tax Rate * Inital Cost)
    # 5-Year Overall Costs = Initial Cost + 5-Year Fuel + 5-Year Tax    
    print('Details:')
    print(f'{"":^20}{H1:^20}{H2:^20}{H3:^20}')
    print(f'{"Init Cost":<20}{House1_init_cost:^20,.2f}{House2_init_cost:^20,.2f}{House3_init_cost:^20,.2f}')
    print(f'{"5Y Fuel Cost":<20}{House1_annual_fuel*5:^20,.2f}{House2_annual_fuel*5:^20,.2f}{House3_annual_fuel*5:^20,.2f}')
    print(f'{"5Y Tax Cost":<20}{(House1_tax_rate*House1_init_cost)*5:^20,.2f}{(House2_tax_rate*House2_init_cost)*5:^20,.2f}{(House3_tax_rate*House3_init_cost)*5:^20,.2f}')
    print(f'{"Overall Cost":<20}{House1_init_cost+(House1_tax_rate*House1_init_cost+House1_annual_fuel)*5:^20,.2f}{House2_init_cost+(House2_tax_rate*House2_init_cost+House2_annual_fuel)*5:^20,.2f}{House3_init_cost+(House3_tax_rate*House3_init_cost+House3_annual_fuel)*5:^20,.2f}')
    next()

    # Data Integrity Validation: To give user confirmation of the data accepted and used
    # 1-Year Fuel Costs
    # 1-Year Tax Rate
    print('Notes:')
    print(f'{"Annual Fuel Cost":<20}{House1_annual_fuel:^20,.2f}{House2_annual_fuel:^20,.2f}{House3_annual_fuel:^20,.2f}')
    print(f'{"Tax Rate":<20}{House1_tax_rate:^20.3%}{House2_tax_rate:^20.3%}'f'{House3_tax_rate:^20.3%}')
    next()

    # Hold Screen
    hold()
    
    # End of the main function

#***************************************************************
#
#  Function:     developerInfo
#  Description:  Prints Programmer's information
#  Parameters:   None
#  Returns:      Output header
#
#**************************************************************
def developerInfo():
    print('Name:     Michael Villarreal')
    print('Course:   Programming Fundamentals I')
    print('Lab: 2')
    print()
    # End of the developerInfo function

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

#***************************************************************
#
#  Function:     house
#  Description:  Imbelishment to add related visual to program
#  Parameters:   None
#  Returns:      Home graphic
#
#**************************************************************
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

#***************************************************************
#
#  Function:     cat
#  Description:  Imbelishment to add visual and messaging to program
#  Parameters:   4 (3 customizations for graphic and 1 message)
#  Returns:      Graphic and Messege
#
#**************************************************************
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

#global variables
YEAR = 5
HOMES = 3

def main():
    next()

    #variables declaration
    init_cost=0.0
    fuel_cost=0.0
    tax_rate=0.0
    total_costs=0.0
    final_report=''
    final_report_title='          Final Report          \n------------------------------'
    best_value=''
    best_value_costs=0
    best_value_title='          Best Value          \n------------------------------'
    temp_value=''
    home='Property '

    #prompt user for input using a loop
    k=0
    while (k<HOMES):
        print(f'Please input information for house {k+1}')
        init_cost=float(input('please enter inital costs: '))
        fuel_cost=float(input('Please enter estimated fuel costs for 1 year: '))
        tax_rate=float(input('Please enter the annual tax rate: '))

        #compute the total
        total_costs=init_cost+(YEAR*(fuel_cost+(tax_rate*init_cost)))
        temp_value=(f'{home+str(k+1):^12}\n${init_cost:12,.2f}\tInitial Cost\n${fuel_cost*YEAR:12,.2f}\tFuel Costs (5y)\n${tax_rate*init_cost*YEAR:12,.2f}\tTax Costs (5y)\n${total_costs:12,.2f}\t5y Total Costs\n\n')

        if best_value_costs==0:
            best_value_costs=total_costs
            best_value=temp_value
        elif total_costs<best_value_costs:
            best_value_costs=total_costs
            best_value=temp_value

        final_report=(f'{final_report}\n{temp_value}')
        print(total_costs)
        print(final_report)
        

        #increment K
        k=k+1

    next()
    print(f'{final_report_title:^30}\n{final_report:^30}')
    next()
    print(f'{best_value_title:^30}\n{best_value:^30}')
    hold()

# Call the main function
main()

# End of Lab 02
