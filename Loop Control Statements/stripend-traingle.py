M=int(input())
N=int(input())
pattern=""
for i in range(1,M+1):
    row=""
    if i%2==0:
        row="- "*N 
    else:
        row+="+ "*N
    pattern+=row+ "\n"
print(pattern)
        