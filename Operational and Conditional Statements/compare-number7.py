a=input()
b=int(a[0])
c=int(a[1])
d=int(a[2])
equals_1=((b==1) or (c==1)or (d==1))
sum_of_digits=b+c+d
sum_of_digits_greater=(sum_of_digits<12)
equals_5=(d==5)
result=(equals_1 and sum_of_digits_greater and equals_5)
print(result)