N=int(input())

for i in range(1,N+1):
    num=(N+1)-i
    spaces=("  ")*(i-1)
    number=(str(num)+" ")*num
    print(spaces+number)