M=int(input())
N=int(input())
result=""
count=0


for i in range(M,N+1):
    if(i%9)==0:
        count+=1
        result=result+str(i)+" "

if count==0:
    print("No Numbers found")
else:
    print(result)