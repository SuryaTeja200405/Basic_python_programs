S=input()


reverse_string=""

for i in S:
    reverse_string=i+reverse_string
    
if_palindrome=(S==reverse_string)
print(if_palindrome)