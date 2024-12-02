N=int(input())
a=str(N)
b=(int(a[0])+int(a[1]))==7
c=((a[0]=='7')or ((a[1])=='7'))
d=((N%7)==0)
e=( b or c or d)
if e:
    print("Special Number")
else:
    print("Normal Number")
