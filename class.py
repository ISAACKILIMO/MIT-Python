# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:53:46 2024

@author: pc
"""

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Please provide a positive value."

    def withdrawal(self, amount):
        """Withdraws the specified amount from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def balance_inquiry(self):
        """Returns the current account balance."""
        return f"Current balance: ${self.balance}"

# Example usage:
account = BankAccount(100)  # Initialize with an initial balance of $100
print(account.deposit(50))  # Deposits $50
print(account.withdrawal(30))  # Withdraws $30
print(account.balance_inquiry())  # Checks the current balance
