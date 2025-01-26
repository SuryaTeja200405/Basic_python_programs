N=int(input())

for i in range(1,N+1):
    stars_top="* "*i 
    print(stars_top)
    
for i in range(1,N):
    stars_bottom="* "*(N-i)
    print(stars_bottom)