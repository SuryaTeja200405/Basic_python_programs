N=int(input())
num=1
for i in range(1,N+1):
    each_n=""
    for j in range(N):
        each_n=each_n+str(num)+" "
        num+=1
    print(each_n)