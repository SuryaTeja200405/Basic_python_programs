N=input()
length=len(N)
sum_of_n=0


for i in N:
    k_th=int(i)**length
    sum_of_n+=k_th
print(sum_of_n)    
