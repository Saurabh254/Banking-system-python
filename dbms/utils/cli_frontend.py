

def frontend():

    options = ["Check balance",
               "Withdrawl",
               "Deposit Amount",
               "Transaction details (upto 5 transaction)",
               "Manage Transaction History",
               "Change Pin"]

    print("Welcome to Saurabh's Bank: \n\n Select method:")
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
                print("Enter Correct input: ")
                continue

        if (1 <= choosen_option <= len(options)+1):
            return choosen_option
        else:
            print(f"Enter integer digits in between 1, {len(options)+1}")
            continue
