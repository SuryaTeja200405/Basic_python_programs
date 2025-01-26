N=int(input())

no_pairs=0 

for i in range(1,N+1):
    if N-i<N and i<N-i:
        no_pairs+=1 
print(no_pairs)    