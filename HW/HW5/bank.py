class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✓ ${amount:,} has been deposited. Balance: ${self.balance:,}")
            return True
        else:
            print("✗ Deposit amount must be greater than 0.")
            return False
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"✓ ${amount:,} has been withdrawn. Balance: ${self.balance:,}")
                return True
            else:
                print("✗ Insufficient balance.")
                return False
        else:
            print("✗ Withdrawal amount must be greater than 0.")
            return False
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: ${self.balance:,}"


class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001
    
    def create_account(self, name, initial_balance=0):
        account_number = str(self.next_account_number)
        self.next_account_number += 1
        account = BankAccount(name, account_number, initial_balance)
        self.accounts[account_number] = account
        print(f"✓ Account created! Account Number: {account_number}")
        return account_number
    
    def find_account(self, account_number):
        return self.accounts.get(account_number)
    
    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        
        if not from_account:
            print("✗ Source account not found.")
            return False
        
        if not to_account:
            print("✗ Destination account not found.")
            return False
        
        if amount <= 0:
            print("✗ Transfer amount must be greater than 0.")
            return False
        
        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            print(f"✓ ${amount:,} has been transferred.")
            print(f"  {from_account.name}'s balance: ${from_account.balance:,}")
            print(f"  {to_account.name}'s balance: ${to_account.balance:,}")
            return True
        else:
            print("✗ Insufficient balance.")
            return False
    
    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts registered.")
            return
        
        print("\n=== All Customer List ===")
        for account in self.accounts.values():
            print(account)
        print()


bank = Bank()

# Create test accounts
bank.create_account("John Doe", 100000)
bank.create_account("Jane Smith", 50000)
bank.create_account("Bob Johnson", 200000)

while True:
    print("\n=== Bank Simulation ===")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("6. Customer List")
    print("0. Exit")
    
    choice = input("\nSelect menu: ")
    
    if choice == "1":
        name = input("Enter name: ")
        initial = input("Initial deposit (enter 0 for $0): ")
        try:
            initial_balance = int(initial)
        except:
            initial_balance = 0
        bank.create_account(name, initial_balance)
    
    elif choice == "2":
        account_number = input("Enter account number: ")
        account = bank.find_account(account_number)
        if account:
            amount = int(input("Enter deposit amount: "))
            account.deposit(amount)
        else:
            print("✗ Account not found.")
    
    elif choice == "3":
        account_number = input("Enter account number: ")
        account = bank.find_account(account_number)
        if account:
            amount = int(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        else:
            print("✗ Account not found.")
    
    elif choice == "4":
        from_acc = input("Enter source account number: ")
        to_acc = input("Enter destination account number: ")
        amount = int(input("Enter transfer amount: "))
        bank.transfer(from_acc, to_acc, amount)
    
    elif choice == "5":
        account_number = input("Enter account number: ")
        account = bank.find_account(account_number)
        if account:
            print(f"\n{account.name}'s balance: ${account.get_balance():,}")
        else:
            print("✗ Account not found.")
    
    elif choice == "6":
        bank.show_all_accounts()
    
    elif choice == "0":
        print("Exiting program.")
        break
    
    else:
        print("✗ Invalid selection.")
