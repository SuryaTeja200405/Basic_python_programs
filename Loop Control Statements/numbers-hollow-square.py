rows=int(input())

for row in range(1,rows+1):
    each_row=""
    
    for column in range(1,rows+1):
        if row ==1 or row == rows:
            each_row = each_row+str(column)+" "
            
        else:
            if column==1 or column ==rows:
                each_row =each_row+str(column)+" "
            else:    
                each_row=each_row+"  "
            
    print(each_row)        