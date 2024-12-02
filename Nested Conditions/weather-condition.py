T=float(input())

freezing_weather=(T<0)
very_cold_weather=(0<=T<10)
cold_weather=(10<=T<20)
normal=(20<=T<30)
hot=(30<=T<40)
very_hot=(T>=40)

if freezing_weather:
    print("Freezing weather")
elif very_cold_weather:
    print("Very Cold weather")
elif cold_weather:
    print("Cold weather")
elif normal:
    print("Normal")
elif hot:
    print("Hot")
elif very_hot:
    print("Very Hot")