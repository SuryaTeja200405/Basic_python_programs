M=int(input())
N=int(input())
result=""

for i in range(M,N+1):
    if(i%2)==1:
        result=result+str(i)+" "
print(result)        