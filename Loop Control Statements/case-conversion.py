S=input()

length=len(S)
first_char=S[0].lower()
result_string=first_char

for i in range(1,length):
    uppercase_char=S[i].upper()
    if S[i]==uppercase_char:
        lowercase_char=S[i].lower()
        result_string=result_string+("-")+lowercase_char
    else:
        result_string+=S[i]

print(result_string)        