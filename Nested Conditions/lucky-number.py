a=int(input())
b=(a%9)==0
c=str(a)
d=int(c[0])
e=int(c[1])
f=(d==9)or(e==9)
g= b or f 
if g:
    print("Lucky Number")
else:
    print("Unlucky Number")