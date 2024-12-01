m=int(input())
p=int(input())
c=int(input())
a=m+p+c
b=m>=70
d=p>=60
e=c>=60
f=(b and d and e)
g=a>=180
h=(f or g)
print(h)
