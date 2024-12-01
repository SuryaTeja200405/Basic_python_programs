a=int(input())
b=int(input())
c=a+b
d=(a-b)==6 
e=(b-a)==6 
f=((a==6)or(b==6))
g=(c==6)
h=(d or e)
i=(f or g or h)
if i==True:
    print("Lucky")
else:
    print("Not Lucky")