#***************************************************************
#
#  Developer:         Michael Villarreal
#
#  Program #:         Lab 1
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
#  Parameters:   Nonex
#
#  Returns:      Nothing
#
#**************************************************************
def main():

    developerInfo()

    # Bunny Ears
    ImgE1 = ("(\_/)   ")
    ImgE2 = ("(\(\    ")
    ImgE3 = (" /)/)   ")
    ImgE4 = ("()_()   ")

    # Bunny Face
    ImgF1 = ("('x')   ")
    ImgF2 = ("(-.-)   ")
    ImgF3 = ("(oxo)   ")
    ImgF4 = ("('.')   ")
    ImgF5 = ("(^.^)   ")

    # Bunny Feet
    ImgFT1 = ('o_(")(")')


    # Initialize variables
    ADULT = 6.0
    CHILD = 3.0
    KEEP = .2
    PAID = (1 - KEEP)


    MovieName = ""
    AdultTix = 0
    ChildTix = 0
    Gross = 0.0
    Net = 0.0
    Amt = 0.0
    X = "\""

    # Request Inputs
    spaces()
    
    print(f"{ImgE1:>10}" + "  HI!")
    print(f"{ImgF1:>10}" + "  Enter the")
    MovieName = input(f"{ImgFT1:>10}" + "  Movie Title: ")
    spaces()

    print(f"{ImgE2:>10}")
    print(f"{ImgF4:>10}" + "  Enter the")
    AdultTix = int(input(f"{ImgFT1:>10}" + "  Adult tickets sold: "))
    spaces()

    print(f"{ImgE4:>10}")
    print(f"{ImgF5:>10}" + "  Enter the")
    ChildTix = int(input(f"{ImgFT1:>10}" + "  Child tickets sold: "))
    spaces()
    
    # Calculations
    Gross = (AdultTix * ADULT) + (ChildTix * CHILD)
    Net = (KEEP * Gross)
    Amt = (PAID * Gross)

    # Output
    print(f"Movie Name {X + MovieName + X:>24}")
    print(f"Adult Tickets Sold:        {AdultTix}")
    print(f"Child Tickets Sold:        {ChildTix}")
    print(f"Gross Box Office Profit:   ${Gross:>7.2f}")    
    print(f"Net Box Office Profit:     ${Net:>7.2f}")    
    print(f"Amount Paid to Movie Co:   ${Amt:>7.2f}")
    


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
    print('Lab: 1')
    print()
    # End of the developerInfo function

def spaces():
    print ()
    print ()
    print ()
    print ()
    print ()
    

# Call the main function
main()

# End of Lab 01
