N=int(input())

count=0

for i in range(1,N+1):
    is_divisible="True"
    for j in range(2,11):
        if (i%j)==0:
            is_divisible="False"
            
    if is_divisible=="True":       
        count+=1 
print(count)        

