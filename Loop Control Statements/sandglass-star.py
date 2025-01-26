N=int(input())


for i in range(1,N+1):
    left_spaces=" "*(i-1)
    stars="* "*(N-i+1)
    print(left_spaces+stars)
    
for i in range(2,N+1):
    left_spaces=" "*(N-i)
    stars="* "*i
    print(left_spaces+stars)