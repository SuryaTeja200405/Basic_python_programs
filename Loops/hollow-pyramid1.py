N=int(input())

for i in range(1,N+1):
    if i ==1:
        row=str(i)
    else:
        spaces=" "*((2*i)-3)
        row=str(i)+spaces+str(i)
    print(row)
    
for i in range(1,N):
    num=N-i
    if i==(N-1):
        row =str(1)
    else:
        spaces=" "*(2*(N-i)-3)
        row=str(num)+spaces+str(num)
    print(row)    