S=int(input())
N=int(input())

s=S
for i in range(1,N+1):
    each_n=""
    for j in range(1,i+1):
        each_n=each_n+str(s)+" "
        s+=1 
    print(each_n)    