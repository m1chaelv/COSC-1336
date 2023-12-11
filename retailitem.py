#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         RetailItem class
#  File Name:         retailitem.py
#  Date:              2023-12-08
#  Chapter:           <Chapter 10>
#  Book:              Edition Starting Out with Python, 5th
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

class RetailItem:
    
    def __init__(self,item):
        self.__item=item
        self.__desc=''
        self.__units=0
        self.__price=0.0

    def set_desc(self):
        # print(self.__desc)
        self.__desc=input('Description: ')

    def set_units(self):
        # print(self.__units)
        self.__units=int(input('Units: '))

    def set_price(self):
        # print(self.__price)
        self.__price=float(input('Price: '))

    def get_desc(self):
        return(self.__desc)

    def get_units(self):
        return(self.__units)

    def get_price(self):
        return(self.__price)

    def get_item(self):
        return(self.__item)

    def __str__(self):
        pass