S=int(input())
N=int(input())
k=0
for num in range(1,N+1):
    k=num+k 
s=k+S-1   

for i in range(1,N+1):
    each_n=""
    for j in range(0,i):
        each_n=each_n+str(s)+" "
        s-=1 
    print(each_n)