N=int(input())
K=int(input())


for i in range(N):
    if N%(N-i)==0:
        largest_factor=N-i
        K=K-1 
    if K==0:
        break
print(largest_factor)    