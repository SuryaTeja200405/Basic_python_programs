C=input()

is_digit=C.isdigit()
is_lower=C.islower()
is_upper=C.isupper()

if is_digit:
    print("Digit")
elif is_lower:
    print("Lowercase Letter")
elif is_upper:
    print("Uppercase Letter")
else:
    print("Special Character")
