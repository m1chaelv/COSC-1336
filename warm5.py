# Program to load matrices
# It will also perform summation and compute the largest
# It will load rows and print out column
# Michael Villarreal
# warm5.py
#
# Global Variable
N=9
n=N**.5

def loaddata(infile,x):
    # file=infile, a=x[3][3]
    # load variables
    k=0
    k2=0
    # yank the data across
    templist=infile.readline().strip('\n').split(',')
    while (k<n):
        k1=0
        while(k1<n):
            x[k1][k]=int(templist[k2])
            k1+=1
            k2+=1
        k+=1

def summation(x):
    # local variable
    s=0
    k=0
    while (k<n):
        s=s+x[k][1]
        k+=1
    return(s)

def largest(x):
    # local variable
    k=0
    l=0
    l=x[1][k]
    k+=1
    while (k<n):
        if (l<x[1][k]):
            l=x[1][k]
        k+=1
    return(l)

def outdata(outfile,x):
    # local variable
    k=0
    print('X- MATRIX  ')
    while (k<n):
        print(x[k][0],x[k][1],x[k][2])
        k+=1

def main():
    # file declaration
    infile=open('warm5.txt','r')
    outfile=open('warm5.out','w')
    try:
        # matrix declaration
        # x[3][3]
        x=[[0,0,0],
           [0,0,0],
           [0,0,0]]
        
        # variable delcaration
        large=0
        suma=0
        
        # call function
        loaddata(infile,x)
        suma=summation(x)
        large=largest(x)
        outdata(outfile,x)

        # write the rest of the output
        print(f'SumA = {suma}')
        print(f'Largest = {large}')

        # close file
        infile.close()
        outfile.close()

        # hold screen
        input('\n\nPress enter when ready..')

    except Exception as err:
        print(err)
        input('hold...')

main()