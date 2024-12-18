S=input()
S=S.lower()
reverse_string=""

for i in S:
    reverse_string=i+reverse_string
    
if S==reverse_string:
    print("True")
else:
    print("False")
    