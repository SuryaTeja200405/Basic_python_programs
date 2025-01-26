N=int(input())


for i in range(1,N+1):
    each_n=""
    for j in range(1,i+1):
        each_n+=str(j)+" "
    print(each_n)    