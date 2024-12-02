CP=int(input())
SP=int(input())
if SP>CP:
    print("Profit")
elif SP<CP:
    print("Loss")
elif CP==SP:
    print("No Profit - No Loss")