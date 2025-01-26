N=int(input())

for i in range(1,N+1):
    spaces=(" ")*(N-i)
    stars="* "*i
    row=spaces+stars
    print(row)