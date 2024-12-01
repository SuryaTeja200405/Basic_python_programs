M=int(input())
P=int(input())
a=((M>35)and(P>35))
b=(M+P)>=100
c=(a or b)
if c==True:
    print("Qualified")
else:
    print("Not Qualified")