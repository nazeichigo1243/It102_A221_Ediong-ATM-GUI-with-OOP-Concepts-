def analyze_transactions():
    try:
        with open("transactions.txt", "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        return {
            "total_transactions": 0,
            "deposits": 0,
            "withdrawals": 0,
            "total_deposited": 0,
            "total_withdrawn": 0,
            "average_transaction": 0,
            "latest_transaction": "None",
            "latest_timestamp": "None",
            "largest_transaction": 0
        }

    transactions = []

    current = {}

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("Timestamp:"):
            current["timestamp"] = (
                line.replace("Timestamp:", "").strip()
            )

        elif line.startswith("Account:"):
            current["account"] = (
                line.replace("Account:", "").strip()
            )

        elif line.startswith("Transaction:"):
            current["type"] = (
                line.replace("Transaction:", "").strip()
            )

        elif line.startswith("Amount:"):
            amount_str = (
                line.replace("Amount:", "").strip().replace("₱", "")
            )
            current["amount"] = float(amount_str)

            transactions.append(current)
            current = {}

    total_transactions = len(transactions)

    deposits = sum(1 for t in transactions if t["type"] == "Deposit")

    withdrawals = sum(1 for t in transactions if t["type"] == "Withdraw")

    total_deposited = sum(
        t["amount"] for t in transactions if t["type"] == "Deposit"
    )

    total_withdrawn = sum(
        t["amount"] for t in transactions if t["type"] == "Withdraw"
    )

    largest_transaction = (
        max(t["amount"] for t in transactions) if transactions else 0
    )

    latest_transaction = (
        transactions[-1]["type"] if transactions else "None"
    )

    latest_timestamp = (
        transactions[-1]["timestamp"] if transactions else "None"
    )

    average_transaction = (
        (total_deposited + total_withdrawn) / total_transactions
        if total_transactions > 0 else 0
    )

    return {
        "total_transactions": total_transactions,
        "deposits": deposits,
        "withdrawals": withdrawals,
        "total_deposited": total_deposited,
        "total_withdrawn": total_withdrawn,
        "average_transaction": average_transaction,
        "latest_transaction": latest_transaction,
        "latest_timestamp": latest_timestamp,
        "largest_transaction": largest_transaction
    }

""" 
######### Learning Signature ######### 
Programmed by: Kevin Paolo Ediong
Date Submitted: September 4, 2026
"""