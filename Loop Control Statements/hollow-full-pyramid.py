n=int(input())

for i in range(1,n+1):
    left_spaces=" "*(n-i)
    if (i>2 )and (i<n):
        hollow_space="  "*(i-2)
        stars="* "+hollow_space+"* "
        print(left_spaces+stars)
    else:
        stars="* "*i
        print(left_spaces+stars)