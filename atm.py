import json
import os
from datetime import datetime

class User:
    def __init__(self, user_id, pin, balance=0):
        """
        Initialize a User object with user ID, PIN, and balance.

        Args:
            user_id (str): The user's unique identifier.
            pin (str): The user's personal identification number.
            balance (float, optional): The initial balance of the user. Defaults to 0.
        """
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        """
        Deposit money into the user's account.

        Args:
            amount (float): The amount to be deposited.
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append((datetime.now(), "Deposit", amount))
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        """
        Withdraw money from the user's account.

        Args:
            amount (float): The amount to be withdrawn.
        """
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append((datetime.now(), "Withdrawal", -amount))
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount for withdrawal.")

    def transfer(self, amount, recipient):
        """
        Transfer money to another user's account.

        Args:
            amount (float): The amount to be transferred.
            recipient (User): The recipient user object.
        """
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.transaction_history.append((datetime.now(), f"Transfer to {recipient.user_id}", -amount))
                recipient.transaction_history.append((datetime.now(), f"Transfer from {self.user_id}", amount))
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount for transfer.")

    def display_transaction_history(self):
        """Display the transaction history of the user."""
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction[0].strftime("%Y-%m-%d %H:%M:%S"), "-", transaction[1], "-", "$ {:,.2f}".format(transaction[2]))


class ATM:
    def __init__(self):
        """Initialize the ATM object."""
        self.users = {}
        self.load_user_data()

    def load_user_data(self):
        """Load user data from the JSON file."""
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                data = json.load(file)
                for user_id, user_data in data.items():
                    self.users[user_id] = User(user_id, user_data["pin"], user_data["balance"])

    def save_user_data(self):
        """Save user data to the JSON file."""
        data = {user.user_id: {"pin": user.pin, "balance": user.balance} for user in self.users.values()}
        with open("users.json", "w") as file:
            json.dump(data, file, indent=4)

    def authenticate_user(self, user_id, pin):
        """
        Authenticate a user based on user ID and PIN.

        Args:
            user_id (str): The user's unique identifier.
            pin (str): The user's personal identification number.

        Returns:
            User or None: The authenticated user object if successful, None otherwise.
        """
        user = self.users.get(user_id)
        if user and user.pin == pin:
            return user
        else:
            return None

    def create_account(self, user_id, pin):
        """
        Create a new user account.

        Args:
            user_id (str): The desired user ID for the new account.
            pin (str): The desired PIN for the new account.
        """
        if user_id not in self.users:
            self.users[user_id] = User(user_id, pin)
            self.save_user_data()
            print("Account created successfully.")
        else:
            print("User ID already exists. Please choose a different one.")

def main():
    atm = ATM()

    print("Welcome to the ATM system!")
    while True:
        print("\n1. Log In")
        print("2. Create Account")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            user = atm.authenticate_user(user_id, pin)
            if user:
                print("Authentication successful.")
                while True:
                    print("\n1. Transaction History")
                    print("2. Withdraw")
                    print("3. Deposit")
                    print("4. Transfer")
                    print("5. Check Balance")
                    print("6. Change PIN")
                    print("7. Log Out")

                    option = input("Enter your choice: ")

                    if option == "1":
                        user.display_transaction_history()
                    elif option == "2":
                        try:
                            amount = float(input("Enter the amount to withdraw: $"))
                            user.withdraw(amount)
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    elif option == "3":
                        try:
                            amount = float(input("Enter the amount to deposit: $"))
                            user.deposit(amount)
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    elif option == "4":
                        recipient_id = input("Enter the recipient's user ID: ")
                        recipient = atm.users.get(recipient_id)
                        if recipient:
                            try:
                                amount = float(input("Enter the amount to transfer: $"))
                                user.transfer(amount, recipient)
                                print("Money of amount: $ ",amount, "transfered successfully.")

                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                        else:
                            print("Recipient not found.")
                    elif option == "5":
                        print("Your current balance is: $ {:,.2f}".format(user.balance))
                    elif option == "6":
                        new_pin = input("Enter your new PIN: ")
                        user.pin = new_pin
                        atm.save_user_data()
                        print("PIN changed successfully.")
                    elif option == "7":
                        print("Logging out.")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Authentication failed. Invalid user ID or PIN.")
        elif choice == "2":
            user_id = input("Enter your desired user ID: ")
            pin = input("Enter your desired PIN: ")
            atm.create_account(user_id, pin)
        elif choice == "3":
            print("Thank you for using the ATM system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
