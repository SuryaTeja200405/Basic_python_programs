N=int(input())
first=int(input())
greatest=first

for i in range(N-1):
    number=int(input())
    
    if number>greatest:
        greatest=number
        
print(greatest)        
   