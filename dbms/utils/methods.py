def userinput(user: dict, user_input: int, balance, username: str):
    if user_input != None:
                if user_input == 1:
                    print(balance(user_dict=user, user_name=username))

                elif user_input == 2:
                    user_bal = balance(user_dict=user, user_name=username)
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
                                    user_name=username, debit_amount=withdrawlAmount)
                            print(
                                f"Transaction Successfully! Your Remaining balance is { balance(user_dict=user, user_name=username)}/~ INR")
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
                                    user_name=username, deposit=depositAmount)
                            print(
                                f"Transaction Successfully! Your Current balance is { balance(user_dict=user, user_name=username)}/~ INR")
                            break

                elif user_input == 4:
                    transaction_list = user[username]["Last_Transactions"]
                    for transactions in transaction_list:
                        print(transactions)
                elif user_input == 5:
                    user[username]["Last_Transactions"] = []
                    print("History Cleared Successfully!")
                elif user_input == 6:
                    while True:
                        old_pin = input("Enter Your old Pin: ")
                        if old_pin.isdigit() and len(old_pin) == 4:
                            old_pin = int(old_pin)
                            pass
                        else:
                            print("Enter numeric Pin of 4 digits")
                            continue
                        if old_pin == user[username]["Pin"]:
                            break
                        else:
                            print("Enter correct pin")
                            continue
                    while True:
                        new_pin = input("Enter Your new pin: ")
                        if new_pin.isdigit() and len(new_pin) == 4:
                            user[username]["Pin"] = "{:04}".format(new_pin)

                            break
                        else:
                            print("Enter numeric Pin")
                            continue
                    print(user[username]["Pin"])