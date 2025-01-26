N=input()

count=0 

for i in N:
    if (int(i)%2)==0:
        count+=1 
if count>2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")