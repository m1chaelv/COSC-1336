#***************************************************************
#
#  Developer:         Michael Villarreal
#
#  Program #:         Lab 2
#
#  File Name:         Lab02 simple.py
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
#	$167,000	$2,300			0.025
#	$162,000	$2,500			0.025
#	$175,000	$1,850			0.020
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

#***************************************************************
#
#  Function:     main
#  Description:  The main function of the program
#  Parameters:   None
#  Returns:      Nothing
#
#**************************************************************
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
        temp_value=(f'{home+str(k+1):^12}\n${init_cost:12,.2f}\tInitial Cost\n${fuel_cost*YEAR:12,.2f}\tFuel Costs (5y)\n${tax_rate*init_cost*YEAR:12,.2f}\tTax Costs (5y)\n${total_costs:12,.2f}\tTotal Costs (5y)\n\n')

        if best_value_costs==0:
            best_value_costs=total_costs
            best_value=temp_value
        elif total_costs<best_value_costs:
            best_value_costs=total_costs
            best_value=temp_value

        final_report=(f'{final_report}\n{temp_value}')
        print(f'Total Cost (5y): ${total_costs:,.2f}')
        next()
        # print(final_report)
        

        #increment K
        k=k+1

    next()
    print(f'{final_report_title:^30}\n{final_report:^30}')
    next()
    print(f'{best_value_title:^30}\n{best_value:^30}')
    next()
    developerInfo()
    hold()

# Call the main function

main()

# End of Lab 02
