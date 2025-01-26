def is_prime(num):
    if num<=1:
        return False 
    for i in range(2,int(num**0.5)+1):
        if num %i==0:
            return False 
    return True 
    
N=int(input())
sum_primes=0 
for i in range(N):
    number=int(input())
    if is_prime(number):
        sum_primes+=number 
print(sum_primes)        
        