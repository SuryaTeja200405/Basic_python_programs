S=input()

is_valid=True 

for i in S:
    unicode_value=ord(i)
    valid_char=(65<=unicode_value and unicode_value<=90)or (97<=unicode_value and unicode_value<=122)or(48<=unicode_value and unicode_value<=57)
    
    if not valid_char:
        is_valid=False
        break
    
print(is_valid)    