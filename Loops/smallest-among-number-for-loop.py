N=int(input())
first_input=int(input())
smalest_num=first_input

for i in range(N-1):
    num=int(input())
    if num<smalest_num:
        smalest_num=num 
print(smalest_num)      