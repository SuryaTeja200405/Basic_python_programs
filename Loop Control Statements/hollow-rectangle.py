M=int(input())
N=int(input())


for i in range(M+2):
    if i==0 or i==M+1:
        print("+"+"-"*N+"+")
    else:
        print("|"+" "*N+"|")

