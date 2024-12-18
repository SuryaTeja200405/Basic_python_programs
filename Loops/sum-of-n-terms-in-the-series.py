X=int(input())
N=int(input())

sum_of_n=0
power=1 
for i in range(N):
    if (i%2)==0:
        sum_of_n+= (X)**power
    else:
        sum_of_n-= (X)**power
    power+=2
    
print(sum_of_n)    