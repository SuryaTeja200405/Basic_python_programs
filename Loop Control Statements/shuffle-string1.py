S1=input()
S2=input()

result=""
len_s=len(S1)
for i in range(0,len_s):
    if i%2==0:
        result+=S1[i]
    else:
        result+=S2[i]
print(result)        
