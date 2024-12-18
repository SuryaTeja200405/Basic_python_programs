N=int(input())

for i in range(1,N+1):
    f_p_spaces=(" ")*(N-i)
    f_p_stars=("* ")*i 
    f_p=f_p_spaces+f_p_stars
    
    space_between_stars=(" ")*(N-i)
    
    s_p_spaces=(" ")*(N-i)
    s_p_stars=("* ")*i 
    s_p=s_p_spaces+s_p_stars
    
    row=f_p+space_between_stars+s_p
    print(row)