M=int(input())
N=int(input())
total=0

for i in range(M,N+1):
    digits_count=len(str(i))
    total+=digits_count
print(total)    