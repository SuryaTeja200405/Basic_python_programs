String=input()

for i in String:
    if i.upper()==i:
        if not i.isdigit():
            print(i)
            break