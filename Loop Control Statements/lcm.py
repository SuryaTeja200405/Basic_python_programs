m=int(input())
n=int(input())

if m>n:
    greatest_number=m 
else:
    greatest_number=n 
    
for number in range(greatest_number,(m*n+1)):
    if ((number%m)==0)and ((number%n)==0):
        lcm=number
        break
print(lcm)        