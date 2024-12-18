M=int(input())
N=int(input())

sum_of_n=1

for i in range(M,N+1):
    if(i%2)==1:
        sum_of_n=sum_of_n*i 
print(sum_of_n) 