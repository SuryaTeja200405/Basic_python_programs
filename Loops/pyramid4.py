N=int(input())

for i in range(1,N+1):
    spaces=("  ")*(N-i)
    symbols=("+ ")*(i-1)+("# ")
    each_row=spaces+symbols
    print(each_row)
for i in range(N-1,0,-1):
    spaces=("  ")*(N-i)
    symbols=("+ ")*(i-1)+("# ")
    each_row=spaces+symbols
    print(each_row)    