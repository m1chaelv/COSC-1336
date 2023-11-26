def insertionSort(ID):
    print(ID)
    for index in range(1, len(ID)):
        print(index,ID)
        currentvalue = ID[index]
        position = index
        
        while position>0 and ID[position-1]>currentvalue:
            print(position,index,currentvalue,ID)
            ID[position]=ID[position-1]
            position = position-1
        
        ID[position]=currentvalue

def insertion(ID):
    N=len(ID)-1
    
    k=1
    while k<=N-1:
        print(k)
        if ID[k] == ID[k+1]:
            print('break: ',k,ID[k],ID[k+1])
            break
        else:
            print('else: ',k,ID[k],ID[k+1])
            temp=ID[k+1]
            j=k
            while j>0:
                print('while j: ',j,ID[j],temp,ID[j+1])
                if ID[j]>temp:
                    ID[j+1]=ID[j]
                    j-=1
                else:
                    j=-1
            ID[j+1]=temp
        k+=1

def my_sort(ID):
    k1=1
    while k1<=len(ID)-1:
        j1=k1
        while (j1>=1) and (ID[j1-1]>ID[j1]):
            temp=ID[j1-1]
            ID[j1-1]=ID[j1]
            ID[j1]=temp
            j1-=1
        print(k1,ID)
        k1+=1
    print(ID)
    
ID = [14,46,43,27,57,41,45,21,2]
# print(ID[1])
# insertion(ID)
# insertionSort(ID)
my_sort(ID)
print(ID)