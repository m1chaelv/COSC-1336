x=([1,2,3],[4,5,6],[7,8,9])
y=([1,1,1],[2,2,2],[3,3,3])
out_x=out_y=''

k1=0
while k1 < 3:
    k2=0
    while k2 < 3:
        # print(x[k1][k2])
        # print(y[k1][k2])
        out_x+=(f'{x[k1][k2]}\t')
        out_y+=(f'{y[k1][k2]}\t')
        k2+=1
    out_x+='\n'
    out_y+='\n'
    k1+=1
print()
print(out_x)
print()
print(out_y)
