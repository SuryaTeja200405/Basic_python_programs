N=int(input())


for i in range(1,N):
    left_spaces=" "*(N-i)
    number=""
    for j in range(1,i+1):
        number= number+str(j)+" "
    print(left_spaces+number)   
    
for k in range(1,N+1):
    i=N-(k-1)
    left_spaces=" "*(N-i)
    number=""
    for j in range(1,i+1):
        number= number+str(j)+" "
    print(left_spaces+number)