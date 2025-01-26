N=int(input())
K=int(input())

initial_number=N+int((K*(K+1))/2)-1
for i in range(1,K+1):
    row_out=""
    
    for j in range(1,i+1):
        row_out+=str(initial_number)+" " 
        initial_number-=1 
    print(row_out)    