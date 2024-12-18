M=int(input())
N=int(input())

for i in range(1,M+1):
    if (i==1 or i==M):
        print("* "*N)
    else:
        spaces="  "*(N-2)
        print("* "+spaces+"*")