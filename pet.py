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

class Pet:

    #***************************************************************
    #  Method:          __init__
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def __init__(self, name, animal_type, age):
        self.__name=name
        self.__animal_type=animal_type
        self.__age=age

    #***************************************************************
    #  Method:      set_name
    #  Description: ???
    #  Parameters:  ???
    #  Returns:     ???
    #**************************************************************
    def set_name(self, name):
        self.__name=name

    #***************************************************************
    #  Data Attribute:  set_animal_type
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def set_animal_type(self, animal_type):
        self.__animal_type=animal_type

    #***************************************************************
    #  Method:      set_age
    #  Description: ???
    #  Parameters:  ???
    #  Returns:     ???
    #**************************************************************
    def set_age(self, age):
        self.__age=age

    #***************************************************************
    #  Method:      get_name
    #  Description: ???
    #  Parameters:  ???
    #  Returns:     ???
    #**************************************************************
    def get_name(self):
        return self.__name


    #***************************************************************
    #  Method:      get_animal_type
    #  Description: ???
    #  Parameters:  ???
    #  Returns:     ???
    #**************************************************************
    def get_animal_type(self):
        return self.__animal_type

    #***************************************************************
    #  Method:      ???
    #  Description: ???
    #  Parameters:  ???
    #  Returns:     ???
    #**************************************************************
    def get_age(self):
        return self.__age

    #***************************************************************
    #  Method:      ???
    #  Description: ???
    #  Parameters:  ???
    #  Returns:     ???
    #**************************************************************
    def __str__(self):
        return(f'{self.__name} ({self.__animal_type}): age {self.__age}')


