N=int(input())

count=0
product_of_numbers=1

while count<N:
    number=int(input())
    product_of_numbers=product_of_numbers*number
    count=count+1 
print(product_of_numbers)