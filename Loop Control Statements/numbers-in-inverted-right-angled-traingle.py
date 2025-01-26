N=int(input())


for i in range(N):
    each_n=""
    row_1=N-i
    for j in range(1,row_1+1):
        each_n=each_n+str(j)+" "
        
    print(each_n)    