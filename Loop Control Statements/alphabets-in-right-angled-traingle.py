string_a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N=int(input())
for i in range(N):
    spaces=""
    
    for col in range(N-i):
        spaces=spaces+string_a[col]+" "
    print(spaces)    
        
    