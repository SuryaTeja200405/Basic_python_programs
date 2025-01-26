M=int(input())
N=int(input())
if not(M>1):
    M=2

for i in range(M,N+1):
    factor=0
    for j in range(2,i):
        if (i%j==0):
            factor+=1 
        
    if factor==0:
        print(i)
            
            
            