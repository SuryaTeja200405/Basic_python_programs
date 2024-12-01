a=int(input())
b=int(input())
c=int(input())
d=(9<a<21)
e=(9<b<21)
f=(9<c<21)
g=(d or e or f)
if g==True:
    print("True")
else:
    print("False")