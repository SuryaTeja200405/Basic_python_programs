P=input()

contains_digit=False

for i in P:
    is_digit=i.isdigit()
    if is_digit:
        contains_digit=True
        
is_lower=P.lower()==P 
is_upper=P.upper()==P 
lower_upper=(not is_lower) and(not is_upper)

is_valid=contains_digit and lower_upper

if is_valid:
    print("Valid Password")
else:
    print("Invalid Password")