N=int(input())
a=(N%2)!=0
b=(N%3)!=0
c=(N%5)!=0
d=(N%7)!=0
e=(a and b and c and d)
if e:
    print("True")
else:
    print("False")