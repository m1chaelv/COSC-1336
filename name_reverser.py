# metrix learning
# name reverser
# accept first and last name from user
# return names but in reverse order
# example: Graham Smith = maharG htimS

def rev(rev_name):
    return(rev_name[::-1])

def main():
    full_name=input('Enter your full name: ')
    names=full_name.split()

    for k1 in names:
        print(rev(k1), end=' ')
    print()
    input()

main()
