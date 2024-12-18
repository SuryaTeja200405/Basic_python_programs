N=int(input())

for i in range(1,N+1):
    if i==1:
        row="* "*N 
    elif i==N:
        left_space=" "*(2*(i-1))
        row=left_space+"*"
    else:
        left_space=" "*(2*(i-1))
        hallow_space=" "*(2*(N-i)-1)
        row=left_space+"*"+hallow_space+"*"
    print(row)    
        