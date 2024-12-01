a=int(input())
b=int(input())
c=((a<=1000)and(b<=1000))or(b>500)
if c==True:
    print("Pair")
else:
    print("Not a Pair")