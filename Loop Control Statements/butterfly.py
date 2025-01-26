N=int(input())

for i in range(1,N+1):
    hollow_spaces="  "*(2*(N-i))
    stars="* "*i+hollow_spaces+"* "*i 
    print(stars)
    
for i in range(N+1):
    hollow_spaces="  "*(2*i)
    stars="* "*(N-i)+hollow_spaces+"* "*(N-i)
    print(stars)    