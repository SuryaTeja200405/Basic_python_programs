N=int(input())
K=int(input())

sum_of_n=0

for i in range(1,N+1):
    power=i**K 
    sum_of_n=sum_of_n+power
print(sum_of_n)