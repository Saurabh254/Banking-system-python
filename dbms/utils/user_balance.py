def balance(user_dict, user_name, user_choice=1,deposit=0, debit_amount=0):
    if(user_choice) == 1:
        balance = user_dict[user_name]["balance"]
        return balance
    elif(user_choice) == 2:
        if debit_amount != 0:
            user_dict[user_name]["balance"] -= debit_amount
    elif(user_choice) == 3:
        if deposit != 0:
            user_dict[user_name]["balance"] += deposit