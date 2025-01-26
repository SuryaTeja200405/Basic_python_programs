N=int(input())

for i in range(2*N-1):
    spaces="  "*(N-1)
    if i==0 or i==N-1 or i==2*N-2:
        star="* "*N 
    elif i<N:
        star="*"
    else:
        star=spaces+"*"
    print(star)    