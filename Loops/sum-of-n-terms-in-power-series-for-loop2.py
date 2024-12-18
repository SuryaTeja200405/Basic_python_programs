X=int(input())
N=int(input())

sum_of_n=0
power=0

for i in range(1,N+1):
    power+=2
    term=X**power
    
    if i%2==0:
        term*= -1
    sum_of_n+=term
print(sum_of_n)        