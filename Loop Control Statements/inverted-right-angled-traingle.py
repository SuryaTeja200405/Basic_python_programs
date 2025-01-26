N=int(input())
count=0

for i in range(1,N+1):
    stars=("* ")*(N-count)
    count+=1
    print(stars) 