A=int(input())
is_morning=((A>=4)and(A<12))
is_afternoon=((A>=12)and(A<16))
is_evining=((A>=16)and(A<20))

if is_morning:
    print("Good Morning")
elif is_afternoon:
    print("Good Afternoon")
elif is_evining:
    print("Good Evening")
else:
    print("Good Night")