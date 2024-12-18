N=int(input())


for i in range(1,N+1):
    before_spaces=2*(N-i)
    after_spaces=2*(i-2)
    if i==1:
        row=" "*before_spaces+str(i)
    else:
        row=" "*before_spaces+(str(i)+" ")+" "*after_spaces+str(i)
    print(row)    
    
for i in range(N-1,0,-1):
    before_spaces=2*(N-i)
    after_spaces=2*(i-2)
    if i==1:
        row=" "*before_spaces+str(i)
    else:
        row=" "*before_spaces+(str(i)+" ")+" "*after_spaces+str(i)
    print(row)    
    