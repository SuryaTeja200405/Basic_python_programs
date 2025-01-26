M=int(input())
N=int(input())
each_n=""

for i in range(M,N+1):
    if i>1:
        factors=0 
    else:
       factors=1
    
    for j in range(2,i):
        if (i%j==0):
            factors+=1
    if factors==0:
        each_n=each_n+str(i)+" "
        
if len(each_n)>0:
    print(each_n)
else:
    print("No Prime Numbers Found")
