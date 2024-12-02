N=int(input())
a=(N**2)
b=str(a)
c=len(b)
d=b[c-1]
e=str(N)
f=len(e)
g=e[f-1]
h=(d==g)
if h:
    print("Equal")
else:
    print("Not Equal")