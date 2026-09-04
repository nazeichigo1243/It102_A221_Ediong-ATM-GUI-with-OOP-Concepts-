from datetime import datetime

def withdraw_money(account, amount):
    if amount <= 0:
        return False

    success = account.withdraw(amount)

    if success:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("transactions.txt", "a") as file:

            file.write(
                f"Timestamp: {timestamp}\n"
            )

            file.write(
                f"Account: {account.account_name}\n"
            )

            # Transaction: Withdraw
            file.write(
                "Transaction: Withdraw\n"
            )

            file.write(
                f"Amount: ₱{amount:.2f}\n\n"
            )

        return True

    return False

""" 
######### Learning Signature ######### 
Programmed by: Kevin Paolo Ediong
Date Submitted: September 4, 2026
"""  