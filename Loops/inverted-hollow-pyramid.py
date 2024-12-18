N=int(input())

for i in range(1,N+1):
    if i==1:
        row="* "*N 
    elif i==N:
        spaces=(N-1)
        row=" "*spaces+"* "
    else:
        left_spaces=" "*(i-1)
        middle_spaces=" "*(2*(N-i)-1)
        row=left_spaces+"*"+middle_spaces+"*"+left_spaces
    print(row)    