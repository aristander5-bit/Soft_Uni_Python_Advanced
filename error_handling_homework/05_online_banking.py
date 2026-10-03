class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

pin_code, balance_str, age_str = input().split(", ")
balance = float(balance_str)
age = int(age_str)

line = input()

while line != "End":
    parts = line.split("#")
    command = parts[0]

    if command == "Send Money":
        money = float(parts[1])
        provided_pin = parts[2]

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if provided_pin != pin_code:
            raise PINCodeError("Invalid PIN code")

        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif command == "Receive Money":
        money = float(parts[1])

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        added_money = money / 2
        balance += added_money
        print(f"{added_money:.2f} money went straight into the bank account")

    line = input()
