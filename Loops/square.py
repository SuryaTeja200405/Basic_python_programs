N=int(input())
for i in range(1,N+1):
    if( i==1 or i==N):
        print("* "*N)
    else:    
        hallow_zeros=("0 ")*(N-2)
        print("* "+ hallow_zeros + "*")