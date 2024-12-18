N=int(input())

for i in range(1,N+1):
    if i==1:
        spaces=(N-1)
        row = " "*spaces+"* "
    elif i==N:
        row="* "*N 
    else:
        left_spaces=(N-i)
        hallow_spaces=2*(i-2)
        row=" "*left_spaces+ "* "+" "*hallow_spaces+"* "
    print(row)    