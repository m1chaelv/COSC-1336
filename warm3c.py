#Program to load from a data file
#Use function to calculate
#Use function to print to screen and output file
#Michael Villarreal
#GLOBAL VARIABLES
E1=3
def main():
    #variable declaration
    a=b=c=b=d=e=f=0.0
    g=0.0
    #file delcaration
    infile=open("warm3c.txt",'r')
    outfile=open("warm3c.out",'w')
    #load from data file
    templist=infile.readline().strip('\n').split(',')
    print(templist)
    a=float(templist[0])
    b=float(templist[1])
    c=float(templist[2])
    d=float(templist[3])
    e=float(templist[4])
    f=float(templist[5])
    #call function 
    g=amarillo(b,d,e,f)
    #call a function to print
    outdata(outfile,a,b,c,d,e,f,g)
    #close files
    infile.close()
    outfile.close()
    #hold screen
    dummy=input('Please enter any key to continue')
#function
def amarillo(x,y,z,z1):
    #local variable
    z2=0.0
    z2=x+y*z*E1-z1
    return(z2)
def outdata(file,r,s,t,u,v,w,x):
    #local variable
    #r=a,s=b,t=c,u=d,v=e,w=f,x=g
    #print to the screen
    print(r,s,t,u,v,w,x)
    #print to the output file
    file.write(str(r)+str(s)+str(t)+str(u)+str(v)+\
               str(w)+str(x)+'\n')

main()
