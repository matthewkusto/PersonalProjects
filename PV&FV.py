def pv_calc():
    print("-" * 14)
    fv = float(input("Enter FV: "))
    r = float(input("Enter Interest Rate (0.0): "))
    n = int(input("Enter Number of Years: "))
    print("====Present Value Chart====")
    while n > 0:
        for i in range(0, n + 1):
            pv = fv / (1 + r) ** n
            print(f"{i}: ${round(pv, 2):,}")
            n -= 1
    print("=" * 28)


def fv_calc():
    print("-" * 14)
    pv = float(input("Enter PV: "))
    r = float(input("Enter Interest Rate (0.0): "))
    n = int(input("Enter Number of Years: "))
    print("====Future Value Chart====")
    while n > 0:
        for i in range(0, n + 1):
            fv = pv * (1 + r) ** n
            print(f"{n}: ${round(fv, 2):,}")
            n -= 1
    print("=" * 28)


def quit_program():
    print("-" * 14)
    print("Good Bye")


choice = None
while choice != "Q":
    print("====Main-Menu====")
    print("A. Present Value")
    print("B. Future Value")
    print("Q. Quit")
    choice = input("Select Option: ").upper()
    if choice == "A":
        pv_calc()
    elif choice == "B":
        fv_calc()
    elif choice == "Q":
        quit_program()
        break
    else:
        print("Invaild Choice")
