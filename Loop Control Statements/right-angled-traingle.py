N=int(input())
stars=1
for i in range(1,N+1):
    row=("* ")*(stars)
    stars+=2
    print(row)