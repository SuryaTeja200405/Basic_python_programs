N=int(input())

count=0

for i in range(1,N):
    for j in range(i+1,N+1):
        sum_squares=i**2+j**2 
        k=i**2+j**2 
        k=int(k**0.5)
        con_1=k*k==sum_squares 
        con_2=k<=N 
        con_3=i<j<k 
        if con_1 and con_2 and con_3:
            count+=1 
print(count)            