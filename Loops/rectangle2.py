M=int(input())
N=int(input())




for i in range(1,M+1):
    if (i==1 or i==M):
        print("* "*N)
    else:
        spaces=("0 "*(N-2))
        print("* "+ spaces +"*")