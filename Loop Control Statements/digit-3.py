N=int(input())
left_spaces="  "*(N-1)

for i in range(2*N-1):
    if i==0 or i==N-1 or i==2*N-2:
        each_row="* "*N 
    else:
        each_row=left_spaces+"*"
    print(each_row)    