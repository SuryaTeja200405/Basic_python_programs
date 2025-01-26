M=int(input())
N=int(input())
row=""

for i in range(1,N+1):
    row=row+(str(i)+" ")
    
for i in range(M):
    print(row)