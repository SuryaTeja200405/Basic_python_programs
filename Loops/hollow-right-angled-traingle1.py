N=int(input())
print("_"*(N+1))

for i in range(1,N+1):
    hallow_spaces=" "*(N-i)
    print("|"+hallow_spaces+"/")
    