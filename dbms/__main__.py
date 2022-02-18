from .utils import frontend, balance, userinput

user = {
    "Saurabh": {"Pin": 1234,
                "Name": "Saurabh",
                "Age": 18,
                "balance": 100000,
                "dob": "19-03-2003",
                "Last_Transactions": ["19-03-2003 Account Insurance", "24-03-2004 Withdrawl 5000 at SBI Burhar", "05-07-2008 Deposited 10000 /~ INR"]
                },
    "Rohan": {"Pin": 7657,
                "Name": "Rohan",
                "Age": 25,
                "balance": 5000,
                "dob": "19-03-2003",
                "Last_Transactions": ["19-03-2022 Account Opening", "24-03-2022 Withdrawl 5000 at SBI Amlai", "05-07-2022 Deposited 10 /~ INR"]
                },

}


class database:
    def __init__(self) -> None:
        
        user_choice, AcHolderName = frontend(user)

        userinput(user=user, user_input=user_choice, balance=balance, username=AcHolderName)

if __name__ == "__main__":
    database()
