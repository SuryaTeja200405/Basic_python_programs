N=int(input())

for row in range(1,N+1):
    left_spaces=" "*(row-1)
    number=""
    i=N-(row-1)
    for j in range(1,i+1):
        number=number+(str(j)+" ")
    print(left_spaces+number)
        