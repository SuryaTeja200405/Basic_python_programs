vowels_list=["A","E","I","O","U","a","i","e","o","u"]


String=input()
count=0
count_1=0
String=String.replace(" ","")
for i in String:
    if i in vowels_list:
        count+=1
    else:
        count_1+=1
       
print(count)
print(count_1) 

    