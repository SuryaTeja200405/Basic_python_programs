A=input()
M=input()
B=len(A)
A=A[:(B-1)]
C=int(A)

if C>=75:
    print("Allowed to write exam")
elif C<75 and M=="Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")