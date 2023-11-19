#***************************************************************
#  Developer:         Michael Villarreal
#  Program #:         Lab 6
#  File Name:         Lab06.py
#  Course:            COSC 1336 Programming Fundamentals I
#  Due Date:          [11-20-2023]
#  Instructor:        Onabajo
#  Chapter:           <Chapter 9> Dictionaries and Sets
#  Session:           ACC Fall 2023
#
# (a) Write a program segment that reads all the records into a file 
#   and prints the name of the Restaurant that accept credit cards
# (b) Write out the name of restaurants that are three stars and above
# (c) Write out the name of restaurants that serve Chinese or Thai 
#   food and are three stars or above
# (d) Write out the name of restaurants that serve HEALTH food
# (e) Write out the name of restaurants that have a one star rating, 
#   two star rating, three star rating and four star rating.
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
    x=input(f'{text} :')
    if x=='':
        return 0
    else:
        return(int(x))
    # End of the get_int function

#***************************************************************
#  Function:     loadrec
#  Description:  load dictionary values from array
#  Parameters:   array, index, type ('int','str','boolean')
#  Returns:      dictionary w/ key:value
#**************************************************************
def loadrec(temp_list,field,type):
    # temp_list=array of data
    # field=field in matrix to load dictionary
    # type=type of record

    #local variables
    temp_dict={}

    # loop thru all array entries
    for k1 in temp_list:
        # set key value
        temp_key=k1[0]
        # set value based on index parameter
        temp_value=k1[field]

        # edit value based on type parameter
        if type=='str':
            temp_dict[temp_key]=temp_value
        elif type=='int':
            temp_dict[temp_key]=int(temp_value)
        elif type=='boolean':
            if temp_value=='Yes':
                temp_value=True
            else:
                temp_value=False
            temp_dict[temp_key]=temp_value

    # return completed dictionary
    return(temp_dict)
    # end of loadrec function


#***************************************************************
#  Function:     loaddata
#  Description:  Load data file into array for processing.
#  Parameters:   file name of file to be ingested
#  Returns:      array
#***************************************************************
def loaddata(file):
    # inbound parameters
    # file=input_file

    # local variables
    temp_list=[]

    # open input file
    infile=open(file,'r')
    # read each line in file
    for k1 in infile:
        # process each line as a string of values separted by commas
        temp_list+=[k1.strip().split(',')]
    # close input file
    infile.close()

    # return populated array
    return(temp_list)
    # end of loadrec function
    
#***************************************************************
#  Function:     report_starter
#  Description:  header template to generate a new report
#  Parameters:   title of new report
#  Returns:      string with report header
#**************************************************************
def report_starter(title):
    # local variables
    temp_report=''

    # generate header in upper case and underlined
    temp_report+='\n'
    temp_report+=title.upper()
    temp_report+='\n'
    temp_report+='-'*len(title)
    temp_report+='\n'

    # return header for report
    return(temp_report)
    # end of report_starter function

#***************************************************************
#  Function:     credit_cards
#  Description:  generate report of restraurants accepting cc
#  Parameters:   credit_card dictionary
#  Returns:      string with completed report
#**************************************************************
def credit_cards(temp_dict):
    # temp_dict=credit_cards
    # local variables
    title='Accept Credit Cards'
    temp_report=report_starter(title)

    # dictionary comprehension if value == True
    temp_answer={k:v for k,v in temp_dict.items() if v}

    # generate report detail in alpha order
    for k1 in sorted(temp_answer):
        temp_report+=k1
        temp_report+='\n'

    # return report 
    return(temp_report)
    # end of credit_cards function

#***************************************************************
#  Function:     recommended
#  Description:  generate report of restaurants with 3+ stars
#  Parameters:   rating dictionary
#  Returns:      string with completed report
#**************************************************************
def recommended(temp_dict):
    # temp_dict=rating
    # local variables
    title='Restaurants with 3+ star ratings'
    temp_report=report_starter(title)

    temp_answer={k:v for k,v in temp_dict.items() if v>=3}

    # generate report detail in alpha order
    for k1 in sorted(temp_answer):
        temp_report+=k1
        temp_report+='\n'

    # return report 
    return(temp_report)
    # end of recommended function

#***************************************************************
#  Function:     recommended_asia
#  Description:  generate report of asian restaurants with 3+ stars
#  Parameters:   rating & food_type dictionaries
#  Returns:      string with completed report
#**************************************************************
def recommended_asia(temp_rate,temp_type):
    # temp_rate=rating
    # temp_type=food_type
    # local variables
    title='Chinese Restaurants with 3+ stars'
    temp_report=report_starter(title)

    temp_answer={k:v for k,v in temp_rate.items() if v>=3}

    # generate report detail in alpha order
    for k1 in sorted(temp_answer):
        if temp_type[k1]=='Chinese':
            temp_report+=k1
            temp_report+='\n'
    
    # return report 
    return(temp_report)
    # end of recommended_asia function

#***************************************************************
#  Function:     health
#  Description:  generate report of restaurants with healthy options
#  Parameters:   food_type dictionary
#  Returns:      string with completed report
#**************************************************************
def health(temp_dict):
    # temp_dict=food_type
    # local variables
    title='Restaurants with Healty Options'
    temp_report=report_starter(title)

    temp_answer={k:v for k,v in temp_dict.items() if v=='Health'}

    # generate report detail in alpha order
    for k1 in sorted(temp_answer):
        temp_report+=k1
        temp_report+='\n'

    # return report 
    return(temp_report)
    # end of health function

#***************************************************************
#  Function:     ratings
#  Description:  generate report of all the restaurants by ratings
#  Parameters:   rating dictionary
#  Returns:      string with completed report
#**************************************************************
def ratings(temp_dict):
    # temp_dict=rating
    # local variables
    title='Restaurants by Ratings'
    temp_report=report_starter(title)
    max_rate=4

    # loop through all star ratings
    for k1 in range(max_rate):
        # adjust loop variable +1
        k1+=1
        # add sub-heading to report "# Star Rating"
        temp_report+=(f'{k1} Star Rating\n')
        # Dictionary Comprehension if value== the star rating
        temp_answer={k:v for k,v in temp_dict.items() if v==k1}
        # generate report detail in alpha order
        for k2 in sorted(temp_answer):
            temp_report+=(f'\t{k2}')
            temp_report+='\n'

    # return report 
    return(temp_report)
    # end of health function
    
#***************************************************************
#  Function:     main
#  Description:  orchestrate file ingestion and procesing
#  Parameters:   none
#  Returns:      final report to screen and file
#**************************************************************
# Global Variables
input_file='Lab06.txt'

def main():
    # Local Variables
    temp_list=[]

    # LOADREC
    temp_list=loaddata(input_file)
    food_type=loadrec(temp_list,1,'str')
    reservation=loadrec(temp_list,2,'boolean')
    rating=loadrec(temp_list,3,'int')
    credit_card=loadrec(temp_list,4,'boolean')
    final_output=developerInfo('Lab06-Dictionary Activities')

    # CREDITCARDS
    final_output+=(credit_cards(credit_card))

    # 3+ stars
    final_output+=(recommended(rating))

    # CHINESETHAI
    final_output+=(recommended_asia(rating,food_type))

    # HEALTH
    final_output+=(health(food_type))

    # STAR
    final_output+=(ratings(rating))

    # Output final report to screen
    print(final_output)
    # end of main function

# Call the main function.
if __name__ == '__main__':
    main()