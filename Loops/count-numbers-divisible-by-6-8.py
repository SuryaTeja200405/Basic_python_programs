N=int(input())

count=0

for i in range(1,N+1):
    if((i%6)==0)and ((i%8)==0):
        count+=1 
print(count)      