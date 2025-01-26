N=input()
a="aeiouAEIOU"
c=""
for i in N:
    if i in a:
        continue 
    c+=i 
print(c)    