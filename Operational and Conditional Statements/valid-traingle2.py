a=int(input())
b=int(input())
c=int(input())
d=((a+b)>c and (b+c)>a and (a+c)>b)
if d==True:
    print("It's a Triangle")
else:
    print("It's not a Triangle")