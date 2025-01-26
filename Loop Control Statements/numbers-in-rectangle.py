M=int(input())
N=int(input())


for i in range(1,M+1):
    each_n=""
    for j in range(7,7+N):
        each_n+=str(j)+" "
    print(each_n)    