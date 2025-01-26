S=int(input())
N=int(input())

for i in range(1,N+1):
    left_spaces=" "*(N-i)
    each_n=""
    
    for j in range(S,S+i):
        each_n+=str(j)+" "
        
    each_n=left_spaces+each_n 
    print(each_n)