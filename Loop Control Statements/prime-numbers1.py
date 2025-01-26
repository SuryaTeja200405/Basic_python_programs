N=int(input())
factors=0

for i in range(2,N+1):
    factors=0
    for j in range(2,i):
        if(i%j==0):
            factors+=1 
    if factors==0:
        print(i)