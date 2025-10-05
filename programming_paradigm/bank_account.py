class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Add the specified amount to account_balance"""
        self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Deduct the amount from account_balance if funds are sufficient
        Returns True if successful, False otherwise
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """Print the current balance in a user-friendly format"""
        print(f"Current Balance: ${self.account_balance:.2f}")