try:
    weight = int(input("Enter your weight in kg: "))
    height = int(input("Enter your height in cm: "))
    bmi = round(weight / ((height / 100) ** 2), 1)
    print("Your BMI is:", bmi)
except ValueError:
    print("Invalid input. Please enter numeric values for weight and height.")
except ZeroDivisionError:
    print("Height cannot be zero. Please enter a valid height.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")