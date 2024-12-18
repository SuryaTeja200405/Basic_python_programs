M=int(input())
N=int(input())

product=1 

for i in range(M,N+1):
    if(i%3)==0:
        product=product*i 
print(product) 
    