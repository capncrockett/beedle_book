# pay_rate_calc.py
#   Program to calculate an employees pay rate, including overtime.

def main():
    hours = eval(input("Enter employee total hours: "))
    pay_rate = eval(input("Enter employee pay rate: "))

    if hours <= 40:
        pay = pay_rate * hours
        print(f"Total pay = ${pay:0.2f}")
    else:
        base_pay = 40 * pay_rate
        overtime = (hours - 40) * (pay_rate * 1.5)
        print(f"Base pay = ${base_pay:0.02f}\n"
              f"Overtime = ${overtime:0.02f}\n"
              f"Total pay = ${base_pay + overtime:0.02f}")


main()
