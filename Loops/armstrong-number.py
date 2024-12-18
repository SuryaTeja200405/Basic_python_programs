N=input()
length=len(N)

sum_of_n=0

for i in N:
    arm=int(i)**length
    sum_of_n+=arm 
if sum_of_n==int(N):
     print("Armstrong Number")
else:
    print("Not an Armstrong Number")
    