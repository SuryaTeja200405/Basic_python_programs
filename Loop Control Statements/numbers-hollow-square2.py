rows=int(input())

for row in range(1,rows+1):
    each_row=str(rows)+" "
    
    if row==1 or row==rows:
        for column in range(2,rows+1):
            each_row=each_row +str(rows-column+1)+" "
            
        print(each_row)
        
    else:
        hollow_spaces="  "*(rows-2)
        each_row=each_row+hollow_spaces+str(1)
        
        print(each_row)