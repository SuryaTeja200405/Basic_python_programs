S=input()

first_word="z"
last_word="a"
word=""

for i in range(len(S)):
    char=S[i]
    if char != " ":
        word+=char
        
    if char==" " or i==len(S)-1:
        if word.lower()<first_word.lower():
            first_word=word
        if word.lower()>last_word.lower():
            last_word=word 
        word=""
        
first_and_last_word=first_word+" "+last_word
print(first_and_last_word)