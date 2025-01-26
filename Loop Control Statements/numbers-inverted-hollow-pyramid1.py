S=int(input())
N=int(input())
r=""
k=S
for row in range(N):
    r=r+str(k)+" "
    k=k+1 
print(r)
z=k 
mid=N-3 
left=1 
dis=N-2 
for m in range(N-3):
    print(" "*left+str(z)+" "+"  "*mid+str(z+dis))
    mid=mid-1
    left=left+1 
    dis=dis-1
    z=z+(dis+2)
print((left)*" "+str(z)+" "+str(z+1))
print((left+1)*" "+str(z+2))