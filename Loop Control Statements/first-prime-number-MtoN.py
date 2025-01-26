M=int(input())
N=int(input())


if not(M>1):
    M=2
    
no_primes=True 

for i in range(M,N+1):
    if_prime=True 
    for j in range(2,i):
        if i%j==0:
            if_prime=False 
            break
    if if_prime:
        print(i)
        no_primes=False
        break
if no_primes:
    print("No prime numbers in the given range")