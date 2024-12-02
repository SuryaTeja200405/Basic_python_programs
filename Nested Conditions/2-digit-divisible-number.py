N=int(input())
a=str(N)
b=int(a[0])
c=int(a[1])
d=(N%b)==0
e=(N%c)==0
f= d and e
if f:
    print(N*2)
else:
    print(N)
    