number=int(input())

k=int(input())

for each_number in range(number):
    if number% (number-each_number)==0:
        largest_factor=number-each_number
        k=k-1 
    if k==0:
        break
    
print(largest_factor) 