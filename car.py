#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Pet class
#  File Name:         pet.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          [xx-xx-xxxx]
#  Instructor:        Onabajo
#  Chapter:           <Chapter 10>
#  Session:           ACC Fall 2023
#
# [xxx]
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

class Car:


    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def __init__(self,year_model,make):
        self.__year_model=year_model
        self.__make=make
        self.__speed=0
        
    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def accelorate(self):
        self.__speed+=5
        # print(f'{self.__year_model} {self.__make}\t:{self.__speed}')

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def brake(self):
        self.__speed-=5
        # print(f'{self.__year_model} {self.__make}\t:{self.__speed}')

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def get_speed(self):
        # print(self.__speed)
        return(self.__speed)

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def get_make(self):
        # print(self.__make)
        return(self.__make)

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def get_year_model(self):
        # print(self.__year_model)
        return(self.__year_model)
