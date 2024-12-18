M=int(input())
N=int(input())
total=N-M
result=""

for i in range(total+1):
    number=N-i
    if(number%2)!=0:
        result=result+str(number)+(" ")
print(result)