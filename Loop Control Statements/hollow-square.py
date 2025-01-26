N=int(input())

for i in range(1,N+3):
    if i==1 or i==(N+2):
        hyphens=("- ")*N 
        row="+ "+hyphens+"+"
    else:
        spaces=("  ")*N 
        row="| "+spaces+"|"
    
    print(row)    