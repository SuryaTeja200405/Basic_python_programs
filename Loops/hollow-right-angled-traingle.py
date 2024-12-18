N=int(input())

for i in range(1,N+1):
    if i==1:
        print("*")
    elif i==N:
        print("* "*N)
    else:
        spaces=" "*(2*(i-2))
        print("* "+spaces+"* ")