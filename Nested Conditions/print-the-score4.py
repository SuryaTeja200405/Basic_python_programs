D=int(input())

first_50=50*3
second_50=50*5
next_100=100*6
bonous_score=100

if D<=50:
    score=D*3
elif D<=100:
    remaining_score=D-50
    remainig_score_test=remaining_score*5
    score=first_50+remainig_score_test
elif  D<=200:
    remaining_score=D-100
    remainig_score_test=remaining_score*6
    score=first_50+second_50+remainig_score_test
elif     D>200:
    remaining_score=D-200
    remainig_score_test=remaining_score*10
    score=first_50+second_50+next_100+remainig_score_test


score=bonous_score+score
print(score)
