a=input()
length=len(a)
first_two_digits=a[:2]
last_two_digits=a[length-2:]
first_two_digits=int(first_two_digits)
last_two_digits=int(last_two_digits)
is_19=(first_two_digits==19)
is_greater=(30< last_two_digits <60)
result=(is_19 and is_greater)
print(result)
