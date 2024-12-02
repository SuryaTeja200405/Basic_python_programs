S=input()
b=S[0:3]
c=(b=="NXT")
d=len(S)
e=S[3:]
a=int(e)
f=((a%2)==0)or((a%7)==0)
g= c and f
if g:
    print("Special String")
else:
    print("Not a Special String")