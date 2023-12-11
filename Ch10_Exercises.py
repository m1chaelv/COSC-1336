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
    while True:
        try:
            x=input(f'{text}: ')
            if x=='':
                return 0
            else:
                return(int(x))
        except:
            print('try again')
            hold()
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
    count=get_int('How many pets do you have')

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
    import car
    import random
    tmp_make=tmp_year=''
    count=tmp_car=0
    # tmp_car=0
    speed={}



    spaces(3)
    count=get_int('How many cars do you have logs on')

    if count>0:
        inventory=[0]*count
        spaces(2)
        for k1 in range(count):
            spaces(1)
            k2=input('Enter the make: ')
            if k2=='':
                break
            else:
                k3=get_int(f'Enter the year for the {k2}')
                tmp_car+=1
                inventory[k1]=car.Car(k3,k2)
        
        for k1 in range(tmp_car):
            k2=random.randint(1, 20)
            for k3 in range(k2):
                inventory[k1].accelorate()
            k2=random.randint(1, k2)
            for k3 in range(k2):
                inventory[k1].brake()

        spaces(2)
        print('Car final speed')
        for k1 in range(tmp_car):
            k2=inventory[k1].get_make()
            k3=inventory[k1].get_year_model()
            k4=inventory[k1].get_speed()
            print(f'{k3} {k2}\t:{k4}')
        
    spaces(1)
    hold()

# 3
# Personal Information Class
#***************************************************************
# Design a class that holds the following personal data: 
# 
# name, 
# address, 
# age, and 
# phone number. 
# 
# Write appropriate accessor and mutator methods. 
# 
# Also, write a program that creates three instances of the class. 
#   One instance should hold your information, and the other 
#   two should hold your friends' or family members' information.
#***************************************************************
def personal_info():
    import p_info
    count=3
    contacts=[0]*count

    for k1 in range(count):
        if k1==0:
            k_prompt='your'
        else:
            k_prompt='your friend or family contact'

        k_name=input(f'Enter {k_prompt} name: ')
        contacts[k1]=p_info.P_info(k_name)

    print('Provide the following contact information')
    for k1 in range(count):
        # k_address=input(f'Address:\t')
        # k_age=get_int(f'Age:\t')
        # k_phone_num=input(f'Phone:\t')
        # contacts[k1].set_address(k_address)
        # contacts[k1].set_age(k_age)
        # contacts[k1].set_phone_num(k_phone_num)
        spaces(1)
        print(contacts[k1].get_name())
        contacts[k1].set_address()
        contacts[k1].set_age()
        contacts[k1].set_phone_num()

    for k1 in range(count):
        spaces(1)
        print(contacts[k1].get_name())
        print(contacts[k1].get_address())
        print(contacts[k1].get_age())
        print(contacts[k1].get_phone_num())
        print('---')
    
    hold()

# 4
# Employee Class
#***************************************************************
# Write a class named Employee that holds the following data about 
# an employee in attributes: 
# 
# name, 
# ID number, 
# department, and 
# job title.
# 
# Once you have written the class, write a program that creates 
# three Employee objects to hold the following data:
#
# Name          ID Number   Department      Job Title
# Susan Meyers  47899       Accounting      Vice President
# Mark Jones    39119       IT              Programmer
# Joy Rogers    81774       Manufacturing   Engineer
# 
# The program should store this data in the three objects, then 
# display the data for each employee on the screen.
#***************************************************************
def emp_class():
    import employee

    emp=[0]*3
    emp[0]=employee.Employee('Susan Meyers',47899,'Accounting','Vice President')
    emp[1]=employee.Employee('Mark Jones',39119,'IT','Programmer')
    emp[2]=employee.Employee('Joy Rogers',81774,'Manufacturing','Engineer')

    spaces(2)
    print(f'{"Name":<18}{"ID":^7}{"Department":<18}{"Title":<10}')
    for k1 in range(len(emp)):
        a=emp[k1]
        print(a)

    hold()

# 5
# RetailItem Class
#***************************************************************
# Write a class named RetailItem that holds data about an item 
# in a retail store. The class should store the following data 
# in attributes: 
# 
# item description, 
# units in inventory, and 
# price.

# Once you have written the class, write a program that creates 
# three RetailItem objects and stores the following data in them:

#           Description     Units in Inventory  Price
# Item #1   Jacket          12                  59.95
# Item #2   Designer Jeans  40                  34.95
# Item #3   Shirt           20                  24.95
#***************************************************************
def retailitem_class():
    import retailitem

    items=[0]
    count=0

    print('Enter inventory\n'
          '----------------')
    while True:
        spaces(2)
        item=input('Item: ')
        if item=='':
            # count-=1
            break
        items[count]=retailitem.RetailItem(item)
        items[count].set_desc()
        items[count].set_units()
        items[count].set_price()
        items+=[0]
        count+=1

    for k1 in range(count):
        print(f'{items[k1].get_item()}\t{items[k1].get_desc()}\t{items[k1].get_units()}\t{float(items[k1].get_price()):>10,.2f}')

    hold()

# 6
# Patient Charges
#***************************************************************
# Write a class named Patient that has attributes for the 
# following data:

# • First name, middle name, and last name
# • Address, city, state, and ZIP code
# • Phone number
# • Name and phone number of emergency contact
#
# The Patient class's _ _init_ _ method should accept an argument 
# for each attribute. The Patient class should also have accessor
# and mutator methods for each attribute.
#
# Next, write a class named Procedure that represents a medical 
# procedure that has been performed on a patient. The Procedure 
# class should have attributes for the following data:
#
# • Name of the procedure
# • Date of the procedure
# • Name of the practitioner who performed the procedure
# • Charges for the procedure
#
# The Procedure class's _ _init__ method should accept an argument 
# for each attribute. The Procedure class should also have accessor 
# and mutator methods for each attribute.
# 
# Next, write a program that creates an instance of the Patient class, 
# initialized with sample data. Then, create three instances of the
# Procedure class, initialized with the following data:

# Procdure #1                   Procedure #2        Procedure #3
# Procure name: Physical Exam   X-ray               Blood test
# Date: Today's date            Today's date        Today's date
# Practitioner: Dr. Irvine      Dr. Jamison         Dr. Smith
# Charge: 250.00                500.00              200.00
#
# The program should display the patient's information, information 
# about all three of the procedures, and the total charges of the 
# three procedures.
#***************************************************************
def patient_charges():
    import procedure
    import patient

    spaces(3)
    print('Patient information')

    p_name=['John','Adam','Smith']
    # print(f'first:\t{p_name[0]}\nmiddle:\t{p_name[1]}\nlast:\t{p_name[2]}')
    p_address=['1919 main st','Austin','TX',12345]
    p_phone=['+1','123-456-7890']
    p_e_contact=['able smith','123-456-7891']

    patients=[0]
    patients[0]=patient.Patient(p_name,p_address,p_phone,p_e_contact)
    # patients[0].label()

    count=0
    cont=True
    procedures=[0]

    spaces(1)
    while cont:
        k_name=input('Procedure: ')
        if k_name=='':
            cont=False
            break
        k_date=input('Date: ')
        k_practitioner=input('Practitioner: ')
        k_charge=float(input('Charge: '))
        procedures[count]=procedure.Procedure(k_name,k_date,k_practitioner,k_charge)
        count+=1
        procedures+=[0]

    spaces(2)
    patients[0].label()

    spaces(1)
    print(f" {'PROCEDURE':<15}{'DATE':^12}{'PRACTITIONER':<12}{'CHARGE':>12}")
    for k1 in range(count):
        procedures[k1].summary()

    spaces(1)
    hold()

# 7
# Employee Management System
#***************************************************************
# This exercise assumes you have created the Employee class for 
# Programming Exercise 4. Create a program that stores Employee
# objects in a dictionary. Use the employee ID number as the key. 
# 
# The program should present a menu that lets the user perform the
# following actions:
# 
# • Look up an employee in the dictionary
# • Add a new employee to the dictionary
# • Change an existing employee's name, department, and job title 
#   in the dictionary
# • Delete an employee from the dictionary
# • Quit the program
# 
# When the program ends, it should pickle the dictionary and save 
# it to a file. Each time the program starts, it should try to 
# load the pickled dictionary from the file. If the file does not 
# exist, the program should start with an empty dictionary.
#***************************************************************
def lookup_emp(dict):
    employee_id=get_int('Enter employee ID:')

    if employee_id in dict:
        print(dict[employee_id].label())
    else:
        print('Invalid')
        hold()

    return(employee_id)

def change_emp(dict):
    import employee

    spaces(1)
    employee_id=get_int('Enter employee ID:')

    if employee_id in dict:
        print(dict[employee_id].label())

        new_employee_id=get_int('Emp ID:\t')
        new_name=input('Name:\t')
        new_department=input('Dept:\t')
        new_title=input('Title:\t')

        employee_id=dict[employee_id].get_id()
        name=dict[employee_id].get_name()
        department=dict[employee_id].get_dept()
        title=dict[employee_id].get_title()

        del dict[employee_id]

        if new_name=='':
            new_name=name
        if new_department=='':
            new_department=department
        if new_title=='':
            new_title=title
        
        emp=employee.Employee(new_name,new_employee_id,new_department,new_title)
        dict[new_employee_id]=emp
        return(dict)

    else:
        print('Invalid')
        hold()

    return(employee_id)


def add_emp(dict):
    import employee

    spaces(1)
    print('ADD EMPLOYEE\n')
    employee_id=get_int('Emp ID:\t')
    name=input('Name:\t')
    department=input('Dept:\t')
    title=input('Title:\t')

    emp=employee.Employee(name,employee_id,department,title)
    dict[employee_id]=emp
    return(dict)

def del_emp(dict):
    employee_id=get_int('Enter employee ID:')

    if employee_id in dict:
        print(dict[employee_id].label())
        del dict[employee_id]
        print('-deleted-')
    else:
        print('Invalid')
        hold()

    return(employee_id)

def emp_mgmt_sys():
    import pickle
    import employee

    file='emp_mgmt_sys.pickle'
    ems={}

    try:
        infile=open(file,'rb')
        ems=pickle.load(infile)
        infile.close()
    except FileNotFoundError as Err:
        outfile=open(file,'wb')
        pickle.dump(ems,outfile)
        outfile.close()

    menu=(
        [1,'Look up an EMPLOYEE'],
        [2,'Add an EMPLOYEE'],
        [3,'Change an existing EMPLOYEE'],
        [4,'Delete an existing EMPLOYEE'],
        [0,'quit']
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
            lookup_emp(ems)
        elif selection==2:
            dict=add_emp(ems)
        elif selection==3:
            dict=change_emp(ems)
        elif selection==4:
            dict=del_emp(ems)

    outfile=open(file,'wb')
    pickle.dump(ems,outfile)
    outfile.close()

    # End of the developerInfo function

# 8
# Cash Register
#***************************************************************
# This exercise assumes you have created the RetailItem class for 
# Programming Exercise 5 . Create a CashRegister class that
# can be used with the RetailItem class. The CashRegister class 
# should be able to internally keep a list of RetailItem objects. 
# The class should have the following methods:

# • A method named purchase _item that accepts a RetailItem object
#   as an argument. Each time the purchase_item method is called, 
#   the RetailItem object that is passed as an argument should be 
#   added to the list.
# • A method named get_total that returns the total price of all 
#   the RetailItem objects stored in the CashRegister object's 
#   internal list
# • A method named show items that displays data about the 
#   RetailItem objects stored in the CashRegister object's internal 
#   list.
# • A method named clear that should clear the Cashregister object's 
#   internal list.
#
# Demonstrate the CashRegister class in a program that allows the 
# user to select several items for purchase. When the user is ready 
# to check out, the program should display a list of all the items 
# he or she has selected for purchase, as well as the total price.
#***************************************************************

def cash_register():
    import retailitem
    import cashregister
    pass

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
        [3,'Personal Information class'],
        [4,'Employee class'],
        [5,'RetailItem class'],
        [6,'Patient Charges class'],
        [7,'Employee Management System'],
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
        elif selection==3:
            personal_info()
        elif selection==4:
            emp_class()
        elif selection==5:
            retailitem_class()
        elif selection==6:
            patient_charges()
        elif selection==7:
            emp_mgmt_sys()
    # End of the developerInfo function

# Call the main function.
if __name__ == '__main__':
    main()