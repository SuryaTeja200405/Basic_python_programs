M=int(input())
N=int(input())


for i in range(M,N+1):
    count=0 
    for j in range(2,i-1):
        if (i%j)==0:
            count+=i
    if count>1:
        print(i)