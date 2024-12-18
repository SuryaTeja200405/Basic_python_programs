A=int(input())
B=int(input())

count=0

for i in range(A,B+1):
    if(i**0.5).is_integer():
        count+=1 
print(count)        