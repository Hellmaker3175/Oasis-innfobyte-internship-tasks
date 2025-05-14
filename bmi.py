weight=float(input("Enter your weight in kilograms: "))
height=float(input("Enter your height in meters: "))
BMI=weight/height**2
if BMI<18.5:
    print("The person is Underweight")
elif BMI>18.5 and BMI<24.9:
    print("the person is having a Normal Weight.")
elif BMI>25.0 and BMI<29.9:
    print("The person is Overweight.")
elif BMI>30.0 and BMI<34.9:
    print("The person is Obese at stage I.")
elif BMI>35.0 and BMI<39.9:
    print("The person is Obese at stage II.")
elif BMI>40:
    print("The person is Obese at stage III")
               
else:
    print("The provided data is not sufficient or incorrect.")