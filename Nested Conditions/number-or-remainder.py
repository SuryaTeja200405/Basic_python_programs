N=int(input())
a=((N%5)==0)and((N%7)==0)
b=N<7
c=a or b 
if c:
    print(N)
else:
    print(N%5)
    print(N%7)