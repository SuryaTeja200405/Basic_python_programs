rows=int(input())
columns=int(input())

spaces=2*columns-3
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

current_index=0 
for row in range(rows):
    each_row=""
    
    for column in range(columns):
        if row==0 or row ==rows-1:
            each_row=each_row+alpha[current_index]+" "
            
        elif column==0:
            each_row=each_row+alpha[current_index]+" "*spaces+alpha[columns+current_index-1]
        current_index=current_index+1 
    print(each_row)    