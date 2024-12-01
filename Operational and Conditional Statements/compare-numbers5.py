a=input()
b=int(a[0])>4
c=int(a[1])>4
d=int(a[2])>4
e=int(a[0])==6
f=((b and c and d)or e)
print(f)