T=int(input())
M=int(input())
N=int(input())
sum_of_n=0

for i in range(M,N+1):
    if(i%T)==0:
        sum_of_n=sum_of_n+i 
print(sum_of_n)     