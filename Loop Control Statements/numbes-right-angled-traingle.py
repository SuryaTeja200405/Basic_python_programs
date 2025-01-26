N=int(input())


for i in range(1,N+1):
    left_spaces= "  " * (N-i)
    each_n=""
    for j in range(1,i+1):
        each_n=str(j)+" "+each_n
        
    each_n=left_spaces+each_n
    print(each_n)