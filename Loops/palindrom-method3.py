S=input()
S=S.lower()
S=S.replace(" ","")
S=S.replace("'","")
result=""


for i in S:
    result=i+result
if result==S:
    print("True")
else:
    print("False")
    
    