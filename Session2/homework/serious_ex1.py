
weigh = int(input("put in your weight in kg: "))
height = int(input("put in your height in cm: "))

BMI = weigh/(height*height*0.0001)

if BMI < 16:
    print("you're serverly unerweight'")
elif BMI <18.5:
    print("you're Underweight")
elif BMI <25:
    print("congrat you're Normal")
elif BMI <30:
    print("ops you're Overweight")
else:
    print("ops you're Obese")
