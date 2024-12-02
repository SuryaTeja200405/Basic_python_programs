hall_ticket = input()
identification = input()

has_hall_ticket = (hall_ticket == "Y")
has_identification = (identification == "Y")

if has_hall_ticket:
    print("Allowed to Exam - Has Hall ticket")
elif has_identification:
    print("Allowed to Exam - Has Identification Card")