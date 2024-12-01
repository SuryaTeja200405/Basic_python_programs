a=input()
b=input()
c=a[0:3]
d=b[0:3]
e=((c=="DIS")or(d=="DIS"))
if e==True:
    print("Discount")
else:
    print("No Discount")