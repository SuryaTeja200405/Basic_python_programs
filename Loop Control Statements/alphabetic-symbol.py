N=int(input())
string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(1,N+1):
    each_n=""
    for j in range(i):
        each_n=each_n+string[j]+" "
    print(each_n[:-1])    
