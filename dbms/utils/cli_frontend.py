
def frontend(userlist: dict):

    options = ["Check balance",
               "Withdrawl",
               "Deposit Amount",
               "Transaction details (upto 5 transaction)",
               "Manage Transaction History",
               "Change Pin"]
    print("Welcome to Saurabh's Bank: \n")
    while True:
        account_holderName = input("Enter Account Holder's Name: ")
        if account_holderName in userlist:
            break
        elif account_holderName.lower() in ["exit", "close", "q"]:
            print("Program closed")
            exit()
        else:
            print(f"Mentioned user ({account_holderName}) not found")
            continue
    while True:
        userPin = input(f"Enter {account_holderName}'s Ac Pin: ")
        if userPin.isdigit() and len(userPin) == 4:
            if int(userPin) == userlist[account_holderName]["Pin"]:
               break
            else:
                print("Wrong Pin entered ")
                continue
        elif userPin.lower() in ["exit", "close", "q"]:
            exit()
        else:
            print("Enter 4 digit numeric Pin")
            continue

    for option, count in zip(options, list(range(1, len(options)+1))):
        print(f"{count}. {option}", end="  ")

    while True:
        choosen_option = input("\nEnter Your desire Option: ")

        if choosen_option.isdigit():
            choosen_option = int(choosen_option)
        else:
            if(choosen_option.lower() in ["close", "exit", "q", "cancel"]):
                break

            else:
                print("Enter Correct input ")
                continue

        if (1 <= choosen_option <= len(options)+1):
            return choosen_option, account_holderName
        else:
            print(f"Enter integer digits in between 1, {len(options)+1}")
            continue
