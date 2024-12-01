N=input()
a=int(N)
b=(N[0]!='5')
c=(N[1]!='5')
d=(N[2]!='5')
e=(b or c or d)
f=(300 < a < 700)
g=(e and f)
if g==True:
    print("Valid Number")
else:
    print("Not a Valid Number")