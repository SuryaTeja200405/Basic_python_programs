N=int(input())


for i in range(1,N+1):
    spaces1=4*(N-i)
    spaces2=2*(i-2)
    if i==1:
        row="* "*1+" "*spaces1+"* "*1
    else:
        row="* "*1+" "*spaces2+"* "*1+" "*spaces1+"* "*1+" "*spaces2+"* "*1
    print(row)    
    
for i in range(1,N+1):
    spaces3=4*(N-1)
    spaces4=2*(N-i-1)
    spaces5=4*(i-1)
    
    if i==N:
        row="* "*1+" "*spaces3+"* "*1
    else:
        row="* "*1+" "*spaces4+"* "*1+" "*spaces5+"* "*1+" "*spaces4+"* "*1
    print(row)    