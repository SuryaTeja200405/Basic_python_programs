N=int(input())


for i in range(N):
    spaces=(" ")*i
    if i==0:
        plus=("+ ")*(N-i)
        row=spaces+plus
    else:
        star=("* ")*(N-i)
        row=spaces+star
    print(row)    