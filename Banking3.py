# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:08:30 2025

@author: abmah
"""

import argparse
import hashlib
import random
import os
import json
import csv
from datetime import datetime
from getpass import getpass
from colorama import Fore, Style, init

# Initialize colorama
init()

# File paths
ACCOUNTS_FILE = "accounts.json"
TRANSACTIONS_FILE = "transactions.csv"

# Helper Functions
def hash_password(password):
    """Hashing password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_input(prompt, expected_type):
    """Validating user input based on the expected type"""
    while True:
        try:
            value = expected_type(input(Fore.CYAN + prompt + Style.RESET_ALL))
            return value
        except ValueError:
            print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)

def load_accounts():
    """Load accounts from the JSON file"""
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_accounts(accounts):
    """Save accounts to the JSON file"""
    with open(ACCOUNTS_FILE, "w") as file:
        json.dump(accounts, file, indent=4)

def log_transaction(acc_no, trans_type, amount):
    """Log a transaction to the CSV file"""
    with open(TRANSACTIONS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if os.stat(TRANSACTIONS_FILE).st_size == 0:
            writer.writerow(["Account Number", "Transaction Type", "Amount", "Date"])
        writer.writerow([acc_no, trans_type, amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

# Core Banking Functions
def create_account():
    """Creates a new bank account"""
    print(Fore.YELLOW + "\n=== Create Account ===" + Style.RESET_ALL)
    name = input(Fore.CYAN + "Enter your name: " + Style.RESET_ALL)
    initial_deposit = validate_input("Enter your initial deposit: ", float)
    password = getpass(Fore.CYAN + "Enter your password: " + Style.RESET_ALL)

    acc_no = str(random.randint(100000, 999999))
    accounts = load_accounts()
    accounts[acc_no] = {
        "name": name,
        "password": hash_password(password),
        "balance": initial_deposit,
    }
    save_accounts(accounts)

    print(Fore.GREEN + f"\nAccount created successfully! Your Account number is {acc_no}." + Style.RESET_ALL)

def login():
    """Log in a user"""
    print(Fore.YELLOW + "\n=== Login ===" + Style.RESET_ALL)
    acc_no = input(Fore.CYAN + "Enter your account number: " + Style.RESET_ALL)
    password = getpass(Fore.CYAN + "Enter your password: " + Style.RESET_ALL)

    accounts = load_accounts()

    if acc_no in accounts and accounts[acc_no]["password"] == hash_password(password):
        print(Fore.GREEN + "\nLogin successful!" + Style.RESET_ALL)
        return acc_no
    else:
        print(Fore.RED + "\nInvalid account number or password." + Style.RESET_ALL)
        return None

def deposit(acc_no):
    """Depositing money into the user's account"""
    accounts = load_accounts()
    amount = validate_input("Enter amount to deposit: ", float)

    accounts[acc_no]["balance"] += amount
    save_accounts(accounts)
    log_transaction(acc_no, "Deposit", amount)

    print(Fore.GREEN + f"\nDeposit successful! New balance: {accounts[acc_no]['balance']}" + Style.RESET_ALL)

def withdraw(acc_no):
    """Withdraws money from the user's account"""
    accounts = load_accounts()
    amount = validate_input("Enter amount to withdraw: ", float)

    if accounts[acc_no]["balance"] >= amount:
        accounts[acc_no]["balance"] -= amount
        save_accounts(accounts)
        log_transaction(acc_no, "Withdraw", amount)

        print(Fore.GREEN + f"\nWithdrawal successful! New balance: {accounts[acc_no]['balance']}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nInsufficient balance." + Style.RESET_ALL)

def view_balance(acc_no):
    """Display the current balance of the user's account."""
    accounts = load_accounts()
    print(Fore.BLUE + f"\nCurrent balance: {accounts[acc_no]['balance']}" + Style.RESET_ALL)

def view_transactions(acc_no):
    """Display the transaction history for the user's account."""
    if not os.path.exists(TRANSACTIONS_FILE):
        print(Fore.RED + "\nNo transaction history found." + Style.RESET_ALL)
        return

    print(Fore.YELLOW + "\n=== Transaction History ===" + Style.RESET_ALL)
    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Account Number"] == acc_no:
                print(f"{row['Date']} - {row['Transaction Type']}: {row['Amount']}")

# Main Menu
def main_menu():
    parser = argparse.ArgumentParser(description="Banking System Application")
    parser.add_argument("--admin", action="store_true", help="Start the system in admin mode")
    args = parser.parse_args()

    logged_in_account = None

    while True:
        print(Fore.MAGENTA + "\n=== Welcome to the Banking System ===" + Style.RESET_ALL)

        if not logged_in_account:
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            selection = input(Fore.CYAN + "Enter your selection: " + Style.RESET_ALL)

            if selection == "1":
                create_account()
            elif selection == "2":
                logged_in_account = login()
            elif selection == "3":
                print(Fore.YELLOW + "Thank you for using the Banking System!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        else:
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. View Balance")
            print("4. View Transactions")
            print("5. Logout")
            selection = input(Fore.CYAN + "Enter your selection: " + Style.RESET_ALL)

            if selection == "1":
                deposit(logged_in_account)
            elif selection == "2":
                withdraw(logged_in_account)
            elif selection == "3":
                view_balance(logged_in_account)
            elif selection == "4":
                view_transactions(logged_in_account)
            elif selection == "5":
                print(Fore.YELLOW + "Logging out..." + Style.RESET_ALL)
                logged_in_account = None
            else:
                print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

# Run the Banking System
if __name__ == "__main__":
    main_menu()
