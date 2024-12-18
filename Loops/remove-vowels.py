S=input()

vowels="AEIOUaeiou"

result=""

for i in S:
    if i not in vowels:
        result+=i 
    
print(result)    