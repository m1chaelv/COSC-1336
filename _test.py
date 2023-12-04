def main():
    infile=open('_test.txt','r')
    outfile=open('_test.out','w')

    print()
    for k1 in infile:
        k2=k1.strip()
        if k2!='':
            print(k2)
    print()
    infile.close()
    outfile.close()
main()