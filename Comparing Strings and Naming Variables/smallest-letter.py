S=input()
smallest_char=S[0]
for i in range(1,len(S)):
    if ord(S[i])<ord(smallest_char):
        smallest_char=S[i]
        
print(smallest_char)    
        
    