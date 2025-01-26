N=int(input())

for i in range(1,N+1):
    hollow_spaces="  "*(N-2)
    if i==1 or i==N:
        stars="* "*N 
    else:
        stars="* "+hollow_spaces+"* "
    print(stars)    
    
for i in range(2,N+1):
    hollow_spaces="  "*(N-1)
    if i==N:
        stars="* "*N 
    else:
        stars=hollow_spaces+"* "
    print(stars)