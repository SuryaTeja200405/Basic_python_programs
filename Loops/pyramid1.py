N=int(input())

for i in range(N):
    spaces=("  ")*(N-i-1)
    num=(str(i+1)+" ")*((2*i)+1)
    
    
    print(spaces+num)