S=input()

first_word=S 
word=""

for i in range(len(S)):
    char= S[i]
    word+=char
    
    if char==" " or i == len(S)-1:
        if word.lower()<first_word.lower():
            first_word=word
        word=""
        
print(first_word)        
    