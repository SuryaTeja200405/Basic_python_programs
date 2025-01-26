string=input()

first_word=string[0].lower()
result=""
for i in string:
    if i==i.upper():
        result=result+"_"+i.lower()
    else:
        result+=i
print(result[1:])