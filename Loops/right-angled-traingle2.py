N=int(input())
counter=1 

while counter<=N:
    if counter==N:
        row="+ "* counter
        print(row)
    else:
        row="* "* counter
        print(row)
    counter+=1    