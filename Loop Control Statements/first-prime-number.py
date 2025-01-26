N=int(input())

for i in range(N+1):
    num=int(input())
    count=0
    for j in range(1,num+1):
        if num%j==0:
            count+=1 
    if count==2:
        print(j)
        break
        