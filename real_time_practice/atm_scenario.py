"""
Atm banking Scenario:
1. Enter pin which allows till 3 attempts
2.credit, debit operations has to be managed  along with balance
3. above should be done using OOPS Concept
"""


class Insufficient_exception(Exception):
    pass


class Bank:
    def __init__(self, balance):
        self.balance = balance

    def login(self, pin):
        if pin == "1234":
            return True
        elif len(pin) > 4:
            print(f"Pin should contain 4 digits")
        else:
            print(f"Incorrect pin")
            return False

    def credit(self, amt):
        self.balance += amt  # self.balance = self.balance + amt

    def debit(self, amt):
        if self.balance >= amt:
            self.balance -= amt
        else:
            raise Insufficient_exception("Amount exceeded balance : Insufficient Balance")


object = Bank(5000)
operation = False
for i in range(1, 4):
    user_pin = input("Enter Your Pin:")
    if object.login(user_pin):
        operation = True
        break
if operation:
    while True:
        select_option = input("""
                        Press c for credit
                        Press d for debit
                        Press b for balance
                        Press e for exit : """)
        if select_option == "c" or select_option == "C":
            object.credit(int(input("Enter amount :")))
            print(f"Your credit transaction is success & Your balance is : {object.balance}")

        if select_option == "d" or select_option == "D":
            object.debit(int(input("Enter amount :")))
            print(f"Transaction is successfull")

        if select_option == "b" or select_option == "B":
            print(f"Current balance is : {object.balance}")

        if select_option == "e" or select_option == "E":
            exit(0)
else:
    print(f"Your have used 3 attempts. Note: Please visit branch for more info...")
