A=int(input())
B=int(input())
C=int(input())
is_first_greatest=(A>B)and(A>C)
if is_first_greatest:
    print(A)
else:
    is_second_greatest=(B>C)
    if is_second_greatest:
        print(B)
    else:
        print(C)
    