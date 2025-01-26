S=input() 

first_word_end_index=0 
for char in S:
    if char==" ":
        break
    else:
        first_word_end_index=first_word_end_index+1 
        
        
first_word=S[0:first_word_end_index]
first_word_upper_case=first_word.upper()
output=first_word_upper_case+S[first_word_end_index:]
print(output)
    