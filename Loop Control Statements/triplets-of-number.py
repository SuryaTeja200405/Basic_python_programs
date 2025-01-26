N=int(input())

no_pairs=0 

for i in range(1,N):
    for j in range(i+1,N):
        if N-(i+j)<N and i<j< N-(i+j):
            no_pairs=no_pairs+1
print(no_pairs)        
    