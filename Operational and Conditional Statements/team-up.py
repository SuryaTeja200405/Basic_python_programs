a=int(input())
b=int(input())
c=((a>300)or(b>300))and((a+b)<500)
if c==True:
    print("Can team up")
else:
    print("Cannot team up")