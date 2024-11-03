height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))


BMI = weight / (height ** 2)


if BMI < 18.5:
    category = "Underweight"
elif 18.5 <= BMI< 24.9:
    category = "Normal weight"
elif 25 <= BMI < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

# Display the result
print(f"Your BMI is {BMI:.2f}, which falls under the category: {category}")
