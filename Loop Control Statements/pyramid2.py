N=int(input())

for i in range(0,N):
    dots=". "*(N-(i+1))
    zeros="0 "*(2*i+1)
    pattern=dots+zeros+dots 
    print(pattern)
    