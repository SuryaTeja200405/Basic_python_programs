N=int(input())


for i in range(1,N+1):
    spaces=(" ")*(N-i)
    stars=("*")*i 
    
    if i==N:
        print("#"*N)
    else:
        print(spaces+stars)