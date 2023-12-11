#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Patient class
#  File Name:         patient.py
#  Date:              2023-12-10
#  Chapter:           <Chapter 10>
#  Book:              Edition Starting Out with Python, 5th
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
class Patient:
    
    def __init__(self,name,address,phone,e_contact):
        self.__name=name
        self.__address=address
        self.__phone=phone
        self.__e_contact=e_contact

    def label(self):
        print(f'{self.__name[0]} {self.__name[1]} {self.__name[2]}')
        print(f'{self.__address[0]}\n{self.__address[1]}, {self.__address[2]} {self.__address[3]}')
        print(f'{self.__phone[0]} {self.__phone[1]}')
        print(f'Emergency contact: {self.__e_contact[0]}: {self.__e_contact[1]}')
        
    def __str__(self):
        pass