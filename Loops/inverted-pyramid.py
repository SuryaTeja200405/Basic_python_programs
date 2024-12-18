N=int(input())

for i in range(N):
    spaces=(" ")*i 
    stars=("*")*(2*(N-i)-1)
    print(spaces+stars)