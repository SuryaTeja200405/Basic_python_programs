M=int(input())
N=int(input())

num=0
num_1=0
for i in range(M,N+1):
    if (i%2!=0):
        num+=1 
print(num) 
for i in range(M,N+1):
    if (i%2==0):
        num_1+=1 
print(num_1)    