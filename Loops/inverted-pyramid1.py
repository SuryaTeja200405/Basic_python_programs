N=int(input())


for i in range(N+1):
    spaces=(" ")*i
    star=("* ")*(N-i)
    print(spaces+star)