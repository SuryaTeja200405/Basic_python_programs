X=int(input())
N=int(input())

sum_of_n=0

for i in range(1,N+1):
    term=X**(2*i-1)
    sum_of_n+=term
print(sum_of_n)    