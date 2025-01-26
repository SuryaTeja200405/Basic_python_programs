N=int(input())

for i in range(1,N+1):
    num_n=""
    for j in range(1,i+1):
        num_n+=str(j)
    for k in range(i-1,0,-1):
        num_n+=str(k)
    print(num_n)    