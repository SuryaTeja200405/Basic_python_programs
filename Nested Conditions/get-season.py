month=int(input())

is_winter=(((month==11)or(month==12))or(month==1))
is_spring=((month==2)or (month==3))
is_summer=(((month==4)or(month==5))or(month==6))
is_rainy=((month==7)or(month==8))
is_autumn=((month==9)or(month==10))

if is_winter:
    print("Winter")
elif is_spring:
    print("Spring")
elif is_summer:
    print("Summer")
elif is_rainy:
    print("Rainy")
elif is_autumn:
    print("Autumn")
    
