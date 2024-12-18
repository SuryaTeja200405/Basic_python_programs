N=int(input())

for i in range(1,N+1):
    if i==1:
        left_spaces=" "*2*(N-1)
        row=left_spaces+"*"
    elif i==N:
        row="* "*N 
    else:
        left_spaces=(" ")*2*(N-i)
        middle_spaces=" "*(2*(i-1)-1)
        row=left_spaces+"*"+middle_spaces+"*"
    print(row)    