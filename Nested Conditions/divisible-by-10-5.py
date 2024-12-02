N= int(input())
a=((N%10)==0)
b=((N%5)==0)
if a:
    print("Divisible by 10")
elif b:
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")