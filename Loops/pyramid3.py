N=int(input())


for i in range(1,N+1):
    num=(str(i)+" ")*i 
    print(num)
for i in range(1,N):
    num=(str(N-i)+" ")*(N-i)
    print(num)