#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         [xxx]
#  File Name:         [xxx].py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          [xx-xx-xxxx]
#  Instructor:        Onabajo
#  Chapter:           <Chapter x>
#  Session:           ACC Fall 2023
#
# [xxx]
#***************************************************************
#***************************************************************
#  Function:     developerInfo
#  Description:  Prints Programmer's information
#  Parameters:   Assignment to include in signature
#  Returns:      Signature w/ date and time
#**************************************************************
def developerInfo(assignment):
    # Obtain current date and time
    from datetime import datetime
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M')

    signature=''
    signature+=(f'{"Name:":>12}\tMichael Villarreal\n')
    signature+=(f'{"Course:":>12}\tProgramming Fundamentals I\n')
    signature+=(f'{"Assignment:":>12}\t{assignment}\n')
    signature+=(f'{"Generated:":>12}\t{formatted_datetime}\n')
    signature+=spaces(2)

    return(signature)
    # End of the developerInfo function

#***************************************************************
#  Function:     spaces
#  Description:  Create a multi-line space to between input/output
#                to keep screen uncluttered
#  Parameters:   None
#  Returns:      n blank lines for screen or n new lines for str
#**************************************************************
def spaces(n):
    for x in range(n):
        print()
        return('\n'*n)
    # End of the spaces function

#***************************************************************
#  Function:     hold
#  Description:  Prompt to pause the screen until ready
#  Parameters:   None
#  Returns:      Nothing
#**************************************************************
def hold():
    input('Please enter any key to continue...')    
    # End of the hold function

#***************************************************************
#  Function:     get_int
#  Description:  Request numeric input from user. Any number not
#   an integer will be returned as a 0. Useful for menu prompts
#   to cancel loop verses exception error.
#  Parameters:   Text string will be used as user prompt + ": "
#  Returns:      integer or 0 if not an integer
#**************************************************************
def get_int(text):
    x=input(f'{text} : ')
    if x=='':
        return 0
    else:
        return(int(x))
    # End of the get_int function

# 1
# Pet class
#***************************************************************
# Write a class named pet, which should have the following data attributes:
# _ _name (for the name of a pet)
# _ _animal_type (for the type of animal that a pet is. 
#       Example values are 'Dog', 'Cat', and 'Bird")
# _ _age (for the pet's age)
# The pet class should have an _ init__ method that creates these 
#       attributes. It should also have the following methods:
# • set_name
# This method assigns a value to the _ _name field.
# • set_animal_type
# This method assigns a value to the _ _animal type field.
# • set_age
# This method assigns a value to the _ _age field.
# • get_name
# This method returns the value of the _ _ name field.
# • get_animal_type
# This method returns the value of the _ _animal type field.
# • get_age
# This method returns the value of the _age field.
# Once you have written the class, write a program that creates an 
# object of the class and prompts the user to enter the name, type, and
# age of his or her pet. This data should be stored as the object's 
# attributes. Use the object's accessor methods to retrieve the pet's
# name, type, and age and display this data on the screen.
#***************************************************************
def pet_class():
    import pet

    spaces(3)
    count=get_int('How many pets do you have? ')

    if count>0:
        pets=[0]*count

        spaces(2)
        for k1 in range(count):
            temp_name=input("Enter pet's name: ")
            temp_type=''
            temp_age=0
            pets[k1]=pet.Pet(temp_name,temp_type,temp_age)

        spaces(1)
        print("Let's get some information about your family")
        # spaces(1)

        print("What type of pet? [dog],[cat],[fish],etc.")
        for k1 in range(count):
            temp_type=input(f"{pets[k1].get_name()}: ")
            pets[k1].set_animal_type(temp_type)

        spaces(1)
        print("What age?")
        for k1 in range(count):
            temp_age=get_int(f'{pets[k1].get_name()}')
            pets[k1].set_age(temp_age)

        spaces(1)
        print('--happy family--')
        for k1 in range(count):
            print(pets[k1])
        spaces(1)
        hold()

# 2
# Car class
#***************************************************************
# Car Class
# Write a class named Car that has the following data attributes:
# _ _year_model (for the car’s year model)
# _ _make (for the make of the car)
# _ _speed (for the car’s current speed)
# 
# The Car class should have an _ _init_ _ method that accepts 
# the car’s year model and make as arguments. These values should 
# be assigned to the object’s _ _year_model and _ _make data 
# attributes. It should also assign 0 to the _ _speed data attribute.
# 
# The class should also have the following methods:
# 
# accelerate
# The accelerate method should add 5 to the speed data attribute 
# each time it is called.
# 
# brake
# The brake method should subtract 5 from the speed data attribute 
# each time it is called.
# 
# get_speed
# The get_speed method should return the current speed.
# 
# Next, design a program that creates a Car object then calls the 
# accelerate method five times. After each call to the accelerate 
# method, get the current speed of the car and display it. Then 
# call the brake method five times. After each call to the brake 
# method, get the current speed of the car and display it.
#***************************************************************

def car_class():
    tmp_make=tmp_year=''
    count=0
    tmp_car=[]

    spaces(3)
    count=get_int('How many cars do you have logs on? ')

    if count>0:
        spaces(2)
        for k1 in range(count):
            spaces(1)
            k2=input('Enter the make: ')
            k3=get_int(f'Enter the year for the {k2}: ')
            tmp_car+=[[k2,k3]]
    
    print(tmp_car)
    hold()


#***************************************************************
#  Function:     main
#  Description:  orchestrate file ingestion and procesing
#  Parameters:   none
#  Returns:      final report to screen and file
#**************************************************************
# Global Variables
# [xxx]

def main():
    menu=(
        [1,'Pet class'],
        [2,'Car class'],
        [0,'exit']
        )
    
    in_menu=True
    while in_menu:
        spaces(2)
        for k1 in menu:
            print(f'{k1[0]}...{k1[1]}')
        spaces(1)
        selection=get_int('Make a selection')

        if selection==0:
            in_menu=False
        elif selection==1:
            pet_class()
        elif selection==2:
            car_class()
    # End of the developerInfo function

# Call the main function.
if __name__ == '__main__':
    main()