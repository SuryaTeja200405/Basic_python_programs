N=int(input())

for i in range(1,N+1):
    spaces="  "*(N-i)
    stars="* "*(2*i)
    print(spaces+stars+spaces)