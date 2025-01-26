N=input()

count=0 
count_1=0 
for i in N:
    if i=="G":
        count+=1 
    elif i=="R":
        count_1+=1 

if count >count_1:
    print(count_1) 
else:
    print(count)