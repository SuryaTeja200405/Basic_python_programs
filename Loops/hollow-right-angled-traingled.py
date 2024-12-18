N=int(input())

for i in range(1,N+1):
    if i==1:
        row=("# "*N)
    elif i==N:
        row="+"
    else:
        hallow_spaces=2*(N-i)-1
        hallow_spaces_count=" "*hallow_spaces
        row= "+"+hallow_spaces_count+"+"
    print(row)    