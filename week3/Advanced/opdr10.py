weight = float(input("Enter your weight(kg): "))
length = float(input("Enter your length(cm): "))

BMI = weight / (length ** 2)

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI <= 25:
    print("Healthy")
if BMI > 25:
    print("Overweight")