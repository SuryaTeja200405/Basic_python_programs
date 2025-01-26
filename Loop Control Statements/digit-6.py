N=int(input())

for i in range(1,2*N):
    spaces="  "*(N-2)
    if i==1 or i==N or i== (2*N-1):
        print("* "*N)
    elif 1<i<N:
        print("* ")
    elif i>N:
        print("* "+spaces+"* ")