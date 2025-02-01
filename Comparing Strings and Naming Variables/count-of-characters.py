S=input()
N=int(input())
count=0
for i in S:
    unicode_value=ord(i)
    if unicode_value==N:
        count+=1
print(count)        
        