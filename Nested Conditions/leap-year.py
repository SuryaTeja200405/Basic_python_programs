Y=int(input())
a=((Y%400)==0)
b=((Y%4)==0) and ((Y%100)!=0)
c= a or b
if c:
    print("True")
else:
    print("False")

