M=int(input())
N=int(input())

result=''

for i in range(M,N+1):
    str_i=str(i)
    
    power=len(str_i)
    sum_of_digits=0 
    for digit in str_i:
        sum_of_digits+=int(digit)**power
        
    if i== sum_of_digits:
        result+=str(i)+" "
        
if result:
    print(result.strip())
else:
    print("-1")