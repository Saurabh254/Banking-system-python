from .utils import frontend, balance, userinput
from . import logging
user = {}

import json
try:
    with open("database.json", "r") as f:
        user = json.loads(f.read())
except Exception as E:
    logging.warning(f" : {E}")
class database:
    def __init__(self) -> None:
        try:
            user_choice, AcHolderName = frontend(userlist= user)
        except Exception as E:
            logging.warning(f" : {E}")

        try:
            userinput(user=user, user_input=user_choice, balance=balance, username=AcHolderName)
        except Exception as E:
            logging.warning(f" : {E}")    

        try:
            with open("database.json", "w") as f:
                f.write(json.dumps(user, indent=4))
        except Exception as E:
            logging.warning(f" : E")

if __name__ == "__main__":
    try:
        database()
    except Exception as E:
        logging.warning(f" : {E}")