N=int(input())

for i in range(1,N+1):
    if i==1:
        spaces=(N-i)
        row=" "*spaces+"*"
    else:
        left_spaces=(N-i)
        hollow_spaces=2*(i-2)
        row= " "*left_spaces+"* "+" "*hollow_spaces+"* "
    print(row)    
    
for i in range(2,N+1):
    if i==N:
        spaces=(N-1)
        row=" "*spaces+"* "
    else:
        left_spaces=" "*(i-1)
        hollow_spaces=" "*(2*(N-i)-1)
        row=left_spaces+"*"+hollow_spaces+"*"
    print(row)    