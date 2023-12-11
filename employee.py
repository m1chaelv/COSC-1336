#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Employee class
#  File Name:         employee.py
#  Date:              2023-12-08
#  Chapter:           <Chapter 10>
#  Book:              Edition Starting Out with Python, 5th
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

class Employee:

    def __init__(self,name,id,dept,title):
        self.__name=name
        self.__id=id
        self.__dept=dept
        self.__title=title
    
    def get_name(self):
        return(self.__name)

    def get_id(self):
        return(self.__id)

    def get_dept(self):
        return(self.__dept)

    def get_title(self):
        return(self.__title)

    def set_name(self):
        print(f'Name:\t{self.__name}')
        self.__name=input('Update: ')
        return(self.__name)

    def set_id(self):
        print(f'ID:\t{self.__id}')
        self.__id=input('Update: ')
        return(self.__id)

    def set_dept(self):
        print(f'Dept:\t{self.__dept}')
        return(self.__dept)

    def set_title(self):
        print(f'Title:\t{self.__title}')
        return(self.__title)

    def label(self):
        # temp=(f'Name:\t{self.__name:<18}\nID:\t{self.__id:^7}\nDept:\t{self.__dept:<18}\nTitle:\t{self.__title:<10}\n')
        temp=(f'\nName:\t{self.__name}\nID:\t{self.__id}\nDept:\t{self.__dept}\nTitle:\t{self.__title}\n')
        return(temp)