a=int(input())
b=int(input())
c=(40<a<140)
d=(40<b<140)
e=(c or d)
if e==True:
    print("Between 40 and 140: Yes")
else:
    print("Between 40 and 140: No")