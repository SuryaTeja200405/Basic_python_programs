N=int(input())

for i in range(1,N+1):
    
    spaces1=4*(N-i)
    spaces2=2*(i-2)
    
    if i==1:
        row="* "*i+" "*spaces1+"* "*i
    elif i==N:
        stars=2*N 
        row="* "*stars
    else:
        row="* "+" "*spaces2+"* "+" "*spaces1+"* "+" "*spaces2+"* "
    print(row)    