M=int(input())
N=int(input())



K=(M*N)

for i in range(1,M+1):
    each_n=""
    for j in range(N):
        each_n=each_n+str(K)+" "
        K-=1 
    print(each_n)   