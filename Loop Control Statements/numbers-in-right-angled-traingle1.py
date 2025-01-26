N=int(input())

for row in range(1,N+1):
    each_n=""
    for col in range(1,row+1):
        each_n=each_n+str(col)+" "
    for col in range(1,row):
        each_n=each_n+str(col)+" "
    print(each_n)    