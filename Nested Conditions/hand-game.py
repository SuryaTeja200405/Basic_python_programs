Abhi=input()
Anjali=input()

if Abhi==Anjali:
    print("Tie")
elif Abhi=="Rock" and Anjali=="Scissors":
    print("Abhinav Wins")
elif Abhi=="Scissors" and Anjali=="Paper":
    print("Abhinav Wins")
elif Abhi=="Paper" and Anjali=="Rock":
    print("Abhinav Wins")
elif Abhi=="Rock" and Anjali=="Paper":
    print("Anjali Wins")
elif Abhi=="Scissors" and Anjali=="Rock":
    print("Anjali Wins")