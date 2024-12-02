N=int(input())
a=(N%11)
b=(a==0)or(a==1)
if b:
    print("Special Eleven")
else:
    print("Normal Number")