a=int(input())
b=int(input())
c=int(input())
d=((a-b)<25 and(b-c)<25 and(c-a)<25)
if d==True:
    print("Difference is less than 25")
else:
    print("Difference is not less than 25")