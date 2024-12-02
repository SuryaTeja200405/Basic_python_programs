D=int(input())

first_50_score=50*3
if D<=50:
    A=(D*3)
    print(A)
elif D>50:
    B=(first_50_score+((D-50)*5))
    print(B)
    