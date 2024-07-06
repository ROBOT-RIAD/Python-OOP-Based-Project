class Account:
    account_number_counter = 1000
    loan_feature_enabled = True

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = Account.account_number_counter
        self.transaction_history = []
        self.loan_count = 0
        Account.account_number_counter += 1

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}. New balance: {self.balance}")
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        elif amount > 0:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}. New balance: {self.balance}")
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, loan_amount):
        if Account.loan_feature_enabled:
            if self.loan_count < 2:
                if loan_amount <= 0:
                    print("Loan amount must be positive.")
                elif self.balance >= loan_amount:
                    self.balance -= loan_amount
                    self.loan_count += 1
                    self.transaction_history.append(f"Loan taken: {loan_amount}. New balance: {self.balance}")
                    print(f"Loan taken: {loan_amount}. New balance: {self.balance}")
                else:
                    print("Insufficient funds to take the loan.")
            else:
                print("Loan limit exceeded. You can only take a loan at most two times.")
        else:
            print("Loan feature is currently disabled.")

    @classmethod
    def toggle_loan_feature(cls, enable):
        cls.loan_feature_enabled = enable
        status = "enabled" if enable else "disabled"
        print(f"Loan feature is now {status}.")


class Admin:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        name = input("Enter user's name: ")
        email = input("Enter user's email: ")
        address = input("Enter user's address: ")
        account_type = input("Enter account type (Savings/Current): ")

        if account_type.lower() not in ["savings", "current"]:
            print("Invalid account type! Please enter either 'Savings' or 'Current'.")
            return None

        new_account = Account(name, email, address, account_type.capitalize())
        self.accounts.append(new_account)
        print("Account created successfully!")
        return new_account

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} deleted successfully.")
                return
        print(f"Account with number {account_number} not found.")

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            print("List of all accounts:")
            for account in self.accounts:
                account.display_account_info()
                print("------------------------")

    def delete_user_account(self):
        account_number = int(input("Enter account number to delete: "))
        self.delete_account(account_number)

    def total_loan_amount(self):
        total_loan = sum(account.balance for account in self.accounts if account.loan_count > 0)
        print(f"Total loan amount in the bank: {total_loan}")

    def total_balance(self):
        total = sum(account.balance for account in self.accounts)
        print(f"Total available balance in the bank: {total}")

    def toggle_loan_feature(self):
        enable = input("Do you want to enable (yes) or disable (no) the loan feature? ").lower()
        if enable == "yes":
            Account.toggle_loan_feature(True)
        elif enable == "no":
            Account.toggle_loan_feature(False)
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


class User:
    def __init__(self, name):
        self.name = name

    def deposit(self, account, amount):
        account.deposit(amount)

    def withdraw(self, account, amount):
        account.withdraw(amount)

    def check_balance(self, account):
        account.check_balance()

    def display_transaction_history(self, account):
        account.display_transaction_history()

    def take_loan(self, account, loan_amount):
        account.take_loan(loan_amount)


# Main program
if __name__ == "__main__":
    admin = Admin()
    user = User("John Doe")

    while True:
        print("\n===== Welcome to the Bank Management System =====")
        print("1. Admin Login")
        print("2. User Operations")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n===== Admin Login =====")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. Display All Accounts")
            print("4. Toggle Loan Feature")
            print("5. Total Loan Amount")
            print("6. Total Balance")
            print("7. Back to Main Menu")
            admin_choice = input("Enter your choice: ")

            if admin_choice == "1":
                admin.create_account()
            elif admin_choice == "2":
                admin.delete_user_account()
            elif admin_choice == "3":
                admin.display_all_accounts()
            elif admin_choice == "4":
                admin.toggle_loan_feature()
            elif admin_choice == "5":
                admin.total_loan_amount()
            elif admin_choice == "6":
                admin.total_balance()
            elif admin_choice == "7":
                continue
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            print("\n===== User Operations =====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Display Transaction History")
            print("5. Take Loan")
            print("6. Back to Main Menu")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                account_number = int(input("Enter your account number: "))
                account = next((acc for acc in admin.accounts if acc.account_number == account_number), None)
                if account:
                    amount = float(input("Enter deposit amount: "))
                    user.deposit(account, amount)
                else:
                    print(f"Account with number {account_number} not found.")
            elif user_choice == "2":
                account_number = int(input("Enter your account number: "))
                account = next((acc for acc in admin.accounts if acc.account_number == account_number), None)
                if account:
                    amount = float(input("Enter withdrawal amount: "))
                    user.withdraw(account, amount)
                else:
                    print(f"Account with number {account_number} not found.")
            elif user_choice == "3":
                account_number = int(input("Enter your account number: "))
                account = next((acc for acc in admin.accounts if acc.account_number == account_number), None)
                if account:
                    user.check_balance(account)
                else:
                    print(f"Account with number {account_number} not found.")
            elif user_choice == "4":
                account_number = int(input("Enter your account number: "))
                account = next((acc for acc in admin.accounts if acc.account_number == account_number), None)
                if account:
                    user.display_transaction_history(account)
                else:
                    print(f"Account with number {account_number} not found.")
            elif user_choice == "5":
                account_number = int(input("Enter your account number: "))
                account = next((acc for acc in admin.accounts if acc.account_number == account_number), None)
                if account:
                    amount = float(input("Enter loan amount: "))
                    user.take_loan(account, amount)
                else:
                    print(f"Account with number {account_number} not found.")
            elif user_choice == "6":
                continue
            else:
                print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exiting the Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
