S=int(input())
N=int(input())
k=0

for num in range(1,N+1):
    each_n=""
    k=num+k 
k=k+S-1 

for i in range(N,0,-1):
    result=""
    for j in range(i):
        result+=str(k)+" "
        k-=1
    
    print(result)
    