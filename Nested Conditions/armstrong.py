N=int(input())
a=str(N)
b=(int(a[0])**3)
c=(int(a[1])**3)
d=(int(a[2])**3)
e=((b+c+d)==N)
if e:
    print("True")
else:
    print("False")