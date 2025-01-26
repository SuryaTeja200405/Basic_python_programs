string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N=int(input())
for i in range(N):
    each_row=""
    for col in range(N):
        each_row=each_row+string[col]+" " 
    print(each_row)    
    
    