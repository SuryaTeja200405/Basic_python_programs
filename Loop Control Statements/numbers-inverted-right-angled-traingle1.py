N=int(input())
k=0 
for i in range(1,N+1):
    k=k+i
for row in range(N):
    each_n=""
    left_spaces=" "*(2*row)
    for col in range(N-row):
        each_n=each_n+str(k)+" "
        k=k-1 
    each_n=left_spaces+each_n 
    print(each_n)
    
        