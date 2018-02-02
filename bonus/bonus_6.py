weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
index = weight/(height*height)
print(index)
if index < 15:
    print("Very severe underweight")
elif index < 16:
    print("Severe underweight")
elif index < 18.5:
    print("Underweight")
elif index < 25:
    print("Normal")
elif index < 30:
    print("Overweight")
elif index < 35:
    print("Moderate obese")
elif index < 40:
    print("Severe obese")
else:
    print("Very severe obese")
