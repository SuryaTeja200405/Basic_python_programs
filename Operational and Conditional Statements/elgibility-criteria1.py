M=int(input())
P=int(input())
C=int(input())
a=(M+P)>=100
b=(P+C)>=100
c=(M+C)>=100
d=(M+P+C)>=180
e=((a or b or c)and d)
print(e)