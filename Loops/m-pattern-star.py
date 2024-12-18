N=int(input())

for i in range(1,N+1):
    stars=i 
    spaces=4*(N-i)
    row=("* ")*stars+(" ")*spaces+("* ")*stars
    print(row)