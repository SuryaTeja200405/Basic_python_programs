D=int(input())

bonus_score=50

first_40=40*2
next_20=20*4
next_60=60*6

if D<=40:
    score=D*2
elif D<=60:
    remaining_distance=D-40
    remaining_distance_score=remaining_distance*4
    score=first_40+remaining_distance_score
elif D<=120:
    remaining_distance=D-60
    remaining_distance_score=remaining_distance*6
    score=first_40+next_20+remaining_distance_score
else:
    remaining_distance=D-120
    remaining_distance_score=remaining_distance*8
    score=first_40+next_20+next_60+remaining_distance_score

score=score+bonus_score
print(score)
    