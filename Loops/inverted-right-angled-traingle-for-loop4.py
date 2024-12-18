N=int(input())

for i in range(N+1):
    spaces=("  ")*i
    stars=("* ")*(N-i)
    print(spaces+stars)