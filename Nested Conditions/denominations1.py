A=int(input())

no_100s=(A//100)
b=A-(no_100s*100)
no_50s=(b//50)
c=b-(no_50s*50)
no_10s=(c//10)
d=c-(no_10s*10)
no_1s=(d//1)

print("100:"+str(no_100s))
print("50:"+str(no_50s))
print("10:"+str(no_10s))
print("1:"+str(no_1s))
