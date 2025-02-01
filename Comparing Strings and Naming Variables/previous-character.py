S=input()

for i in S:
    if i==" ":
        continue
    unicode_value=ord(i)
    value=unicode_value-1 
    print(chr(value))