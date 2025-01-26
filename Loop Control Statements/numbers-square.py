N=int(input())

for i in range(1,N+1):
    each_n=""
    for j in range(N,0,-1):
        each_n+=str(j)+" "
    print(each_n)    