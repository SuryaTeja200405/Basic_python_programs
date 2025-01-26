N=input()

len_s=len(N)
shuffled_s=""

for i in range(len_s):
    index=int(input())
    shuffled_s+=N[index]
print(shuffled_s)    