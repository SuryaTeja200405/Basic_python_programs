string=input()

length=len(string)
result_string=string[0]

for each_number in range(1,length):
    each_character=string[each_number]
    upper_case_character=each_character.upper()
    lower_case_character=each_character.lower()
    
    if each_character == upper_case_character:
        result_string = result_string+"-"+lower_case_character
    else:
        result_string = result_string+each_character
print(result_string)        
    