S=input()
condition_digit= False

for i in S:
    is_valid=i.isdigit()
    if is_valid:
        condition_digit=True

if condition_digit:
    print("Valid Password")
else:
    print("Invalid Password")
    