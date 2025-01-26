N=int(input())

for i in range(1,N+1):
    sum_of_digits=0
    number=str(i)
    power=len(number)
    
    for each_digit in number:
        each_digit=int(each_digit)
        sum_of_digits=sum_of_digits+(each_digit**power)
        
    number=int(number)
    is_armstrong= sum_of_digits==number
    if is_armstrong:
        print(number)