N=int(input())

for i in range(1,N+1):
    left_spaces=" "*(N-i)
    if i==1:
        row="1 "
        print(left_spaces+row)
    else:
        hollow_spaces="  "*(i-2)
        row="1 "+hollow_spaces+str(i)+" "
        print(left_spaces+row)
for j in range(1,N):
    left_spaces=" "*j 
    if j==N-1 :
        row="1"
        print(left_spaces+row)
    else:
        hollow_spaces="  "*(N-j-2)
        row="1 "+hollow_spaces+str(N-j)+""
        print(left_spaces+row)