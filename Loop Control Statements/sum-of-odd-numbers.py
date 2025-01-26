N=int(input())

count=0 

for i in range(N+1):
    if (i%2)!=0:
        count+=i 
print(count)        