X=int(input())
N=int(input())

sum_of_n=0

for i in range(1,N+1):
    term=(str(X)*i)
    sum_of_n+=int(term)
print(sum_of_n)    