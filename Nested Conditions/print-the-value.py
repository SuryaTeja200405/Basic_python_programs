S=input()

A=len(S)
B=(A-1)
C=int(S[:B])
D=S[B]

if D=="T":
    print(C*10)
elif D=="H":
    print(C*100)
elif D=="K":
    print(C*1000)