S=input()

first_char=S[0]
unicode_value=ord(first_char)

is_lower=(97<=unicode_value and unicode_value<=122)
is_upper=(65<=unicode_value and unicode_value<=90)
is_underscore= first_char=="_"

is_valid= is_lower or is_upper or is_underscore
print(is_valid)