number=input()

if_one_digit=(len(number)==1)
if_two_digit=(len(number)==2)
if_three_digit=(len(number)==3)
if_four_digit=(len(number)==4)

if if_one_digit:
    print(number)
elif if_two_digit:
    first_number=int(number[0])
    second_number=int(number[1])
    sum_of_digits=first_number+second_number
    print(sum_of_digits)
elif if_three_digit:
    first_number=int(number[0])
    second_number=int(number[1])
    third_number=int(number[2])
    sum_of_digits=first_number+second_number+third_number
    print(sum_of_digits)
elif  if_four_digit:   
    first_number=int(number[0])
    second_number=int(number[1])
    third_number=int(number[2])
    fourth_number=int(number[3])
    sum_of_digits=first_number+second_number+third_number+fourth_number
    print(sum_of_digits)
    


