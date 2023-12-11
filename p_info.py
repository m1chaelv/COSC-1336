#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Personal Information class
#  File Name:         p_info.py
#  Date:              2023-12-08
#  Chapter:           <Chapter 10>
#  Book:              Edition Starting Out with Python, 5th
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

class P_info:

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def __init__(self,name):
        self.__name=name
        self.__address=''
        self.__age=0
        self.__phone_num=''

    #***************************************************************
    #  Function:     spaces
    #  Description:  Create a multi-line space to between input/output
    #                to keep screen uncluttered
    #  Parameters:   None
    #  Returns:      n blank lines for screen or n new lines for str
    #**************************************************************
    def spaces(self,n):
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
    def hold(self):
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
    def get_int(self,text):
        while True:
            try:
                x=input(f'{text}: ')
                if x=='':
                    return 0
                else:
                    return(int(x))
            except:
                print('try again')
                self.hold()
        # End of the get_int function

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def set_address(self):
        print(f'Current Address: {self.__address}')
        self.__address=input('Enter a new address: ')

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def get_address(self):
        # print(self.__address)
        return(self.__address)

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def set_age(self):
        print(f'Current Age: {self.__age}')
        self.__age=input('Enter age: ')

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def get_age(self):
        # print(self.__age)
        return(self.__age)

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def set_phone_num(self):
        print(f'Current Address: {self.__phone_num}')
        self.__phone_num=input('Enter a new phone number: ')

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def get_phone_num(self):
        # print(self.__phone_num)
        return(self.__phone_num)

    #***************************************************************
    #  Method:          ???
    #  Description:     ???
    #  Parameters:      ???
    #  Returns:         ???
    #**************************************************************
    def get_name(self):
        # print(self.__name)
        return(self.__name)
