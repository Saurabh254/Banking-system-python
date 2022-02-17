from hashlib import new
from .utils import frontend, balance


user = {
    "Saurabh": {"Pin": 1234,
                "Name": "Saurabh",
                "Age": 18,
                "balance": 100000,
                "dob": "19-03-2003",
                "Last_Transactions": ["19-03-2003 Account Insurance", "24-03-2004 Withdrawl 5000 at SBI Burhar", "05-07-2008 Deposited 10000 /~ INR"]
                },


}


class database:
    def __init__(self) -> None:
        user_input = frontend()

        if user_input != None:
            if user_input == 1:
                print(balance(user_dict=user, user_name="Saurabh"))

            elif user_input == 2:
                user_bal = balance(user_dict=user, user_name="Saurabh")
                while True:
                    withdrawlAmount = input(
                        f"Enter withdrawl amount(Remaining Balance: {user_bal}): ")
                    if withdrawlAmount.isdigit():
                        withdrawlAmount = int(withdrawlAmount)
                    else:
                        print("Enter integer digits")
                        continue

                    if 0 < withdrawlAmount > user_bal:
                        print("Entered amount isn't available in you AC, Try Again! ")
                        pass

                    elif withdrawlAmount < 0:
                        print("Enter a Positive Amount!")
                        pass

                    else:
                        balance(user_dict=user, user_choice=user_input,
                                user_name="Saurabh", debit_amount=withdrawlAmount)
                        print(
                            f"Transaction Successfully! Your Remaining balance is { balance(user_dict=user, user_name='Saurabh')}/~ INR")
                        break
            elif user_input == 3:
                while True:
                    depositAmount = input(
                        "Enter the amount you wanna deposit: ")
                    if depositAmount.isdigit():
                        depositAmount = int(depositAmount)
                    else:
                        print("Enter integer digits")
                        continue
                    if depositAmount < 0:
                        print("Enter a Positive Amount!")
                        pass

                    else:
                        print(depositAmount)
                        balance(user_dict=user, user_choice=user_input,
                                user_name="Saurabh", deposit=depositAmount)
                        print(
                            f"Transaction Successfully! Your Current balance is { balance(user_dict=user, user_name='Saurabh')}/~ INR")
                        break

            elif user_input == 4:
                transaction_list = user["Saurabh"]["Last_Transactions"]
                for transactions in transaction_list:
                    print(transactions)
            elif user_input == 5:
                user["Saurabh"]["Last_Transactions"] = []
                print("History Cleared Successfully!")
            elif user_input == 6:
                while True:
                    old_pin = input("Enter Your old Pin: ")
                    if old_pin.isdigit() and len(old_pin) ==4:
                        old_pin = int(old_pin)
                        pass
                    else:
                        print("Enter numeric Pin of 4 digits")
                        continue
                    if old_pin == user["Saurabh"]["Pin"]:
                        break
                    else:
                        print("Enter correct pin")
                        continue
                while True:
                    new_pin = input("Enter Your new pin: ")
                    if new_pin.isdigit() and len(new_pin) == 4:
                        user["Saurabh"]["Pin"] = "{:04}".format(new_pin)

                        break
                    else:
                        print("Enter numeric Pin")
                        continue
                print(user["Saurabh"]["Pin"])


if __name__ == "__main__":
    database()
