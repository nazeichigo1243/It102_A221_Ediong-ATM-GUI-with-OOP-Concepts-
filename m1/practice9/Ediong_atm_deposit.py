from datetime import datetime

def deposit_money(account, amount):
    # TODO 3: Check whether the amount is valid.
    # If the amount is zero or negative, return False.
    if amount <= 0:
        return False

    # TODO 4: Ask the Account object to perform the deposit.
    # Store the returned result.
    success = account.deposit(amount)

    # TODO 5: If the deposit was successful, create a timestamp.
    if success:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # TODO 6: Open transactions.txt using append mode.
        with open("transactions.txt", "a") as file:

            # TODO 7: Write the timestamp.
            file.write(
                f"Timestamp: {timestamp}\n"
            )

            # TODO 8: Write the account name.
            file.write(
                f"Account: {account.account_name}\n"
            )

            # TODO 9: Write:
            # Transaction: Deposit
            file.write(
                "Transaction: Deposit\n"
            )

            # TODO 10: Write the transaction amount.
            # Format the amount to two decimal places.
            file.write(
                f"Amount: ₱{amount:.2f}\n\n"
            )

        # TODO 11: Return True when the transaction is successful.
        return True

    # TODO 12: Return False when the transaction is unsuccessful.
    return False

""" 
######### Learning Signature ######### 
Programmed by: Kevin Paolo Ediong
Date Submitted: September 4, 2026
"""    