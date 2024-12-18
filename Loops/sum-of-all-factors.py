N=int(input())

sum_of_n=1+N

for i in range(2,N):
    if (N%i)==0:
        sum_of_n+=i 
print(sum_of_n)     