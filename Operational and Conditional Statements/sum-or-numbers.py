a=int(input())
b=int(input())
c=a+b
d=(30<c<50)
e=((a<20)or(b<20))
e=(d or e)
if e==True:
    print(c)
else:
    print(a)
    print(b)