# Program to call a function
# Michael Villarreal
# COSC 1336 Fundamentals of Programming
# warm3b.py
def main():
    #variable delcaration
    a=2
    b=3
    c=5
    d=0
    #call a function
    d=holland(a,b,c)
    #print output
    print(a,b,c,d)
#function
def holland(r,s,t):
    #local variable
    v=0
    #calculate
    v=r*s%t
    return(v)

main()
