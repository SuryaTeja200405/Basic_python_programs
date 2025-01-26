string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N=int(input())

for i in range(1,N+1):
    spaces=""
    left_spaces="  "*(N-i)
    for col in range(i):
        left_spaces=left_spaces+string[col]+" "
    print(left_spaces)