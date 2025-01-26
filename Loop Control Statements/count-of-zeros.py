N=input()

count=0

for i in N:
    if i=="0":
        count+=1 
if count>3:
    print("Count of zeroes is greater than three")
else:
    print("Count of zeroes is not greater than three")