N=int(input())
print("* "*(2*N-1))
for i in range(1,N+1):
    left_spaces=(" ")*i 
    middle_spaces=(" ")*(2*(i-1))
    stars=("* ")*(N-i)
    
    print(left_spaces+stars+middle_spaces+stars)