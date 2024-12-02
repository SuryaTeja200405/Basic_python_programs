N=int(input())


no_years=(N//365)
A=N%365
no_weeks=A//7
no_days=A%7


print(str(no_years) +" years " + str(no_weeks) +" weeks "+  str(no_days) +" days")
