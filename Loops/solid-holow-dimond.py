N=int(input())

for i in range(1,N+1):
    spaces=" "*(N-i)
    stars="* "*i 
    print(spaces+stars)
for row in range(1,N-1):
    left_count= row
    spaces=" "*left_count
    hollow_spaces_count= N-row-2
    hollow_spaces="  "* hollow_spaces_count
    row= spaces+"* "+hollow_spaces+"*"
    print(row)
print(" "*(N-1)+"*")    