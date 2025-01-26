N=int(input())

for i in range(1,2*N+2):
    spaces="  "*(N-2)
    if i==1 or i==N+1 or i==(2*N+1):
        print("* "*N)
    else:
        print("* "+spaces+"* ")
    