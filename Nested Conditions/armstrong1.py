N=int(input())
a=str(N)
b=int(a[0])
c=int(a[1])
d=int(a[2])
e=int(a[3])
f=((b**4)+(c**4)+(d**4)+(e**4))
g=(f==N)
if g:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")