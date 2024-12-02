A=int(input())
B=int(input())
c=((A%3)==0)and((B%3)==0)
d=((A%12)==0)or((B%12)==0)
e= c and d 
if e:
    print("Pair")
else:
    print("Not a Pair")