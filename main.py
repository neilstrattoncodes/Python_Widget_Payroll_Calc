
#constant variables:


PAY_RATE = 17.50
COMMISSION = .35
GROSS_PAY_TAX = .21
CPP_RATE = .0495
EI_RATE = .16
UNION_DUES = 15
WIDGET = .35
EI = .016

while True:
    print(f"EMPLOYEE PAYROLL CALCULATOR")
    print(f"-" * 44)
    emp_name = str(input(f"Please enter your name: "))
    hours_worked = float(input(f"Enter amount of hours worked: "))
    print()
    wid_monday = int(input(f"Enter amount of Widgets for Monday: "))
    wid_tuesday = int(input(f"Enter amount of Widgets for Tuesday: "))
    wid_wednesday = int(input(f"Enter amount of Widgets for Wednesday: "))
    wid_thursday = int(input(f"Enter amount of Widgets for Thursday: "))
    wid_friday = int(input(f"Enter amount of Widgets for Friday: "))

#total number of widgets

    total_widgets = wid_monday + wid_tuesday + wid_wednesday + wid_thursday + wid_friday

#Regular pay

    regular_pay = PAY_RATE * hours_worked

#Commission pay

    commission_pay = total_widgets * WIDGET

#Gross pay

    gross_pay = regular_pay + commission_pay

#Gross pay plus tax

    gross_pay_tax_rate = gross_pay * GROSS_PAY_TAX

# CPP pay cost

    cpp_pay_rate = gross_pay * CPP_RATE

# EI deductions

    ei_deductions = gross_pay * EI

# Union dues deductions

    union_deductions = UNION_DUES

#Total deductions

    totaldeductions = gross_pay_tax_rate + ei_deductions + cpp_pay_rate + UNION_DUES

#Total net pay

    net_pay = gross_pay - totaldeductions


    print(f"-"*44)
    print("WORK INFO")
    print(f"Employee name:                      {emp_name:>3}")
    print(f"Hours worked:                  \t\t{hours_worked:<5.2f}")
    print(f"Widgets made (per week)       \t\t${total_widgets:<5.2f}")
    print()
    print(f"PAY INFO")
    print(f"Regular pay is:               \t\t${regular_pay:<5.2f}")
    print(f"Total Commission is:          \t\t${commission_pay:<5.2f}")
    print(f"your Gross pay is:            \t\t${gross_pay:<5.2f}")
    print()
    print("DEDUCTIONS")
    print(f"your income tax deduction is: \t\t${gross_pay_tax_rate:<5.2f}")
    print(f"your CPP deduction is:        \t\t${cpp_pay_rate:<5.2f}")
    print(f"your EI deduction is:         \t\t${ei_deductions:<5.2f}")
    print(f"your union dues are:          \t\t${union_deductions:<5.2f}")
    print(f"your total deductions are:    \t\t${totaldeductions:<5.2f}")
    print(f"-"*44)
    print(f"your total net pay is:        \t\t${net_pay:<5.2f}")
    print()
    choice = input(f"do you want to enter new values? y or n: ")
    if choice.lower() == "y":
        continue

    elif choice.lower() == "n":
        print("Bye!")
        break