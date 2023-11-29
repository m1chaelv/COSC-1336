# Program to build a structure Dictionary
# will load a database of restaurants
# will Query based on many criteria 
# print out Query results
# Global variable
# CLASS
# lab6dictionary.py
# ACC SPRING 2023
# CISC 1336 PYTHON PROGRAMMING
# PROFESSOR ONABAJO
n=10
def main():
    # create an empty dictionary
    restaurant = {}
    # File declaration
    outfile=open("temp666.out",'w')
    # Variable declaration
   

    # call function to load the dictionary
    loadrec(restaurant)
    # Query
    creditcards(outfile,restaurant)
    
    stars(outfile,restaurant)
    chinese(outfile,restaurant)
    health(outfile,restaurant)
    starss(outfile,restaurant)
    # close files
    #infile.close()
    outfile.close()
    
#function loadrec
def loadrec(aDict):
    
    # a=restname,b=foodtype,c=reservation,d=rating,e=creditcard
    # local variable
    k=0
     # list of Structure Dictionary declaration
    restname=" " #string
    foodtype="  "# string
    reservation= False # boolean type
    rating=0 # integer
    creditcard= False # boolean type
    # file declaration
    infile=open("lab6AA.txt",'r')
    #load data using a loop
    while( k < n):
        templist=infile.readline().strip('\n').split(',')
        # print(templist)
        restname=templist[0]
        foodtype=templist[1]
        if (templist[2].upper()== "YES"):
            reservation= True
        rating=int(templist[3])
        if (templist[4].upper() == "YES"):
            creditcard = True

        # load them into a Dictionary
        aDict[restname]=[foodtype,reservation,rating,creditcard]
        
        # temporary print to test loading
        # print(restname,creditcard)
        # reset the intial state of the Dictionary for those two fileds
        reservation=creditcard=False
        k=k+1
        #dummy=input("Press anykey to continue")
    infile.close()
def creditcards(file,aDict):
    # a=restname,b=creditcard
    # aDict[restname]=[foodtype=0,reservation=1,rating=2,creditcard=3]
    # local Variable
    print ("Restuarant that accept Credit cards")
    file.write("Restaurant that accept credit cards"+'\n')
    index=3 # rating
    key=0 # restname
    for key in aDict:
        if (aDict[key][index]):
            print (key) 
            file.write(key+'\n')
    #dummy=input("Press anykey to continue")     
def stars(file,aDict):
    # # aDict[restname]=[foodtype=0,reservation=1,rating=2,creditcard=3]
    # local Variable
    print ("Restuarant that are three stars or above")
    file.write("Restaurant that are three stars or above")
    key=0
    index=2
    for key in aDict:
        if (aDict[key][index] >= 3):
            print (key)
            file.write(key+'\n') 
        
def chinese(file,aDict):
    # a=restname,b=foodtype,c=rating
   # # aDict[restname]=[foodtype=0,reservation=1,rating=2,creditcard=3 
    # local Variable
    print ("Restuarant that serve CHINESE and three stars or above")
    file.write("Restaurant that serve CHINESE and three stars or above"+'\n')
    key=0
    index=0
    indexx=2
    for key in aDict:
        if ((aDict[key][index] == "chinese") and (aDict[key][indexx]>=3 )):
            print (key)
            file.write(key+'\n')
    #dummy=input("Press anykey to continue")
def health(file,aDict):
    # a=restname,b=foodtype,c=rating
   # # aDict[restname]=[foodtype=0,reservation=1,rating=2,creditcard=3 
    # local Variable
    print ("Restuarant that serve HEALTH FOOD")
    file.write("Restaurant that serve HEALTH FOOD"+'\n')
    key=0
    index=0
    for key in aDict:
        if ((aDict[key][index] == "health") ):
            print (key)
            file.write(key+'\n')
    # dummy=input("Press anykey to continue")
def starss(file,aDict):
    # a=restname,b=foodtype,c=rating
   # # aDict[restname]=[foodtype=0,reservation=1,rating=2,creditcard=3 
    # local Variable
    print ("Restuarants LISTED BY STARS")
    file.write("Restaurant LISTED BY STARSS"+'\n')
    key=0
    index=2
    indexx1=1
    for indexx1 in range (1,5):
        print (indexx1,"STAR RESTAURANTS")
        key=0
        for key in aDict:
            if ((aDict[key][index] == indexx1) ):
                print (key)
                file.write(key+'\n')
    #dummy=input("Press anykey to continue") 
main()














