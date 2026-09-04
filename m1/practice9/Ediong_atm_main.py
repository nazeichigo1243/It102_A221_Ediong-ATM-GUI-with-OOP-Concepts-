import streamlit as st

# TODO 1: Import the Account class.
from Ediong_atm_account import Account

# TODO 2: Import the balance module.
import Ediong_atm_balance

# TODO 3: Import the deposit module.
import Ediong_atm_deposit

# TODO 4: Import the withdraw module.
import Ediong_atm_withdraw

# TODO 5: Import the history module.
import Ediong_atm_history

# TODO 6: Import the analysis module.
import Ediong_atm_analysis

# TODO 7: Create the Account object.
# Account: Juan Dela Cruz
# Starting balance: ₱10,000.00
account = Account("Juan Dela Cruz", 10000.00)

# TODO 8: Configure the Streamlit page.
st.set_page_config(
    page_title="Python ATM",
    page_icon="🏧",
    layout="wide"
)

# TODO 9: Display the main ATM title.
st.title("PYTHON ATM")

# TODO 10: Display a welcome message using the account name.
st.write(f"Welcome, **{account.account_name}**!")

# TODO 11: Add a divider.
st.divider()

# TODO 12: Create the sidebar title.
st.sidebar.title("ATM Menu")

# TODO 13: Create a sidebar radio menu.
menu = st.sidebar.radio(
    "Select an operation",
    ["Check Balance", "Deposit", "Withdraw", "View History", "Analyze Transactions"]
)

# ================================
# CHECK BALANCE
# ================================
if menu == "Check Balance":
    st.subheader("Check Balance")
    balance = Ediong_atm_balance.check_balance(account)
    st.metric("Current Balance", f"₱{balance:,.2f}")

# ================================
# DEPOSIT
# ================================
elif menu == "Deposit":
    st.subheader("Deposit Money")
    amount = st.number_input(
        "Enter deposit amount:",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Deposit Money"):
        if amount <= 0:
            st.error("Invalid deposit amount.")
        else:
            success = Ediong_atm_deposit.deposit_money(account, amount)
            if success:
                st.success("Deposit successful!")
                st.metric("Updated Balance", f"₱{account.check_balance():,.2f}")
            else:
                st.error("Deposit failed.")

# ================================
# WITHDRAW
# ================================
elif menu == "Withdraw":
    st.subheader("Withdraw Money")
    amount = st.number_input(
        "Enter withdrawal amount:",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Withdraw Money"):
        if amount <= 0:
            st.error("Invalid withdrawal amount.")
        else:
            success = Ediong_atm_withdraw.withdraw_money(account, amount)
            if success:
                st.success("Withdrawal successful!")
                st.metric("Updated Balance", f"₱{account.check_balance():,.2f}")
            else:
                st.error("Insufficient balance.")

# ================================
# VIEW HISTORY
# ================================
elif menu == "View History":
    st.subheader("Transaction History")
    lines = Ediong_atm_history.view_history()

    if lines:
        st.text("".join(lines))
    else:
        st.info("No transactions found yet.")

# ================================
# ANALYZE TRANSACTIONS
# ================================
elif menu == "Analyze Transactions":
    st.subheader("Transaction Analysis")
    results = Ediong_atm_analysis.analyze_transactions()

    if results["total_transactions"] == 0:
        st.info("No transactions to analyze yet.")
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Transactions", results["total_transactions"])
        col1.metric("Deposits", results["deposits"])
        col1.metric("Withdrawals", results["withdrawals"])

        col2.metric("Total Deposited", f"₱{results['total_deposited']:,.2f}")
        col2.metric("Total Withdrawn", f"₱{results['total_withdrawn']:,.2f}")
        col2.metric("Average Transaction", f"₱{results['average_transaction']:,.2f}")

        col3.metric("Latest Transaction", results["latest_transaction"])
        col3.metric("Latest Timestamp", results["latest_timestamp"])
        col3.metric("Largest Transaction", f"₱{results['largest_transaction']:,.2f}")

"""
########## Learning Signature ##########
Programmed by: Kevin Paolo Ediong
Date Submitted: September 4, 2026
"""