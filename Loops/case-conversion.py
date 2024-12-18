S=input()

length=len(S)

result_string=S[0]

for i in range(1,length):
    e_c=S[i]
    upper_case=e_c.upper()
    
    if e_c ==upper_case:
        result_string=result_string+" "+e_c 
    else:
        result_string=result_string+e_c 
        
print(result_string)        