S=input()

upper_case=""

for i in S:
    is_upper=(i==i.upper())
    if is_upper:
        upper_case+=i 
print(upper_case)        