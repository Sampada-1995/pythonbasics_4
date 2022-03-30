import math


def fd_calculator():
    principle = int(input("Enter the Principle value: "))
    rate = float(input("Enter the rate of interest per annum: "))
    tenure = int(input("Enter the tenure in years: "))

    invested_amount = principle
    estimated_return = ((principle * rate * tenure) / 100)
    total_value = invested_amount + estimated_return

    print(f"Invested Amount :", invested_amount)
    print(f"Estimated Return : ", estimated_return)
    print(f"Total Value :", total_value)


def rd_calculator():
    monthly = int(input("Enter the Monthly Contribution value: "))
    rd_market_rate = float(input("Enter the rate of interest per annum: "))
    rd_tenure = int(input("Enter the tenure in months: "))
    quaters = rd_tenure / 3

    rd_invested_amount = monthly * rd_tenure
    rd_rate = rd_market_rate / 400

    rd_total_value = (monthly * ((1 + rd_rate) ** (quaters - 1))) / (1 - ((1 + rd_rate) ** (-1 / 3)))

    print(f"RD rate: ", rd_rate)
    print(f"Invested Amount :", rd_invested_amount)
    #print(f"Estimated Return : ", interest_amount)
    print(f"Total Value :", rd_total_value)


def calculator_selected():
    cal = input("Enter Your Choice RD / FD: ")
    print(cal)
    if cal == "RD" or "rd":
        rd_calculator()
    elif cal == "FD" or "fd":
        fd_calculator()
    else:
        print("Enter correct input type RD / FD")


calculator_selected()
