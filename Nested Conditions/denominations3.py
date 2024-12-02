A=int(input())


no_100s=(A//100)
b=A-(no_100s*100)
no_50s=(b//50)
c=b-(no_50s*50)
no_20s=(c//20)
d=c-(no_20s*20)
no_10s=(d//10)


print("100 Notes: "+str(no_100s))
print("50 Notes: "+str(no_50s))
print("20 Notes: "+str(no_20s))
print("10 Notes: "+str(no_10s))
