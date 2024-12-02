D=int(input())

bonus_score=30

first_20= 20*2
next_40=40*4

if D<=20:
    score=D*2
elif D<=60:
    remaining_score=(D-20)
    remaining_distance_score=remaining_score*4
    score=first_20+remaining_distance_score
else:
    remaining_score=(D-60)
    remaining_distance_score=remaining_score*6
    score=first_20+next_40+remaining_distance_score
    
score=  score+bonus_score 
print(score)
    
    