# bmi_calc.py
#   Program calculates a person BMI.

def main():
    weight = eval(input("Please enter weight (in pounds): "))
    height = eval(input("Please enter height (in inches): "))
    bmi = weight * 720 / height ** 2

    if bmi < 19:
        print(f"BMI is below healthy range at {bmi:2.01f}")
    elif 19 <= bmi <= 25:
        print(f"BMI is a healthy range at {bmi:2.01f}")
    else:
        print(f"BMI is above healthy range at {bmi:2.01f}")


main()
