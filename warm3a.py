# Program to use Open and close statements
# Read from a data file and write to an output file
# Michael Villarreal
# COSC 1336 Fundamental of Programming
# ACC Fall 2023
# warm3a.py

def main():
    # open file declaration
    infile=open("warm3a.txt","r")
    outfile=open("warm3a.out","w")
    # variable declarations
    a=b=c=d=e=f=0
    #load from a data file
    templist=infile.readline().strip("\n").split(",")
    a=int(templist[0])
    b=int(templist[1])
    c=int(templist[2])
    d=int(templist[3])
    e=int(templist[4])
    print(templist)
    #compute sum of all numbers
    f=a+b+c+d+e
    #print to the screen
    print(a,b,c,d,e,f)
    #print to an output file
    outfile.write(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+'\n')
    #close files
    infile.close()
    outfile.close()

