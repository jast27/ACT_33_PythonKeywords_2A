import random
from datetime import datetime

def assert_positive(amount):
    assert amount > 0, "Amount must be positive."

class BankAccount:
    def __init__(self, owner, pin):
        self.owner = owner
        self.pin = pin
        self.balance = 0.0
        self.transactions = []
        self.account_number = random.randint(100000, 999999)
        self.record_transaction(f"Account opened for {self.owner}")

    def record_transaction(self, message):
        self.transactions.append((datetime.now(), message))

    def verify_pin(self):
        entered_pin = input("🔢 Enter your PIN: ")
        return entered_pin == self.pin

    def deposit(self, amount):
        if not self.verify_pin():  # Ask for PIN before proceeding with deposit
            print("Incorrect PIN. Transaction denied.")
            return
        assert_positive(amount)
        self.balance += amount
        self.record_transaction(f"Deposited: ₱{amount:.2f}")
        print(f"✅ Successfully deposited ₱{amount:.2f}.")

    def withdraw(self, amount):
        if not self.verify_pin():  # Ask for PIN before proceeding with withdrawal
            print("Incorrect PIN. Transaction denied.")
            return
        if amount > self.balance:
            print("Insufficient funds! Please check your balance and try again.")
            return False
        self.balance -= amount
        self.record_transaction(f"Withdrew: ₱{amount:.2f}")
        print(f"💰 You have withdrawn ₱{amount:.2f}.")
        return True

    def transaction_history(self):
        if not self.transactions:
            print("No transactions recorded.")
        else:
            print("\nTransaction History:")
            for t in sorted(self.transactions, key=lambda t: t[0]):
                yield t[0].strftime("%Y-%m-%d %H:%M:%S"), t[1]  # Using yield

account = None

def menu():
    global account
    while True:
        print("\nWelcome to EverTrust Bank!")
        print("1. Open a New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Account Balance")
        print("5. View Transaction History")
        print("6. Delete Account")
        print("7. Exit")
        
        try:
            choice = int(input("\nGood Day! Please Enter a number: "))
            
            if choice == 1:
                if account is not None:
                    print("You already have an account!")
                    continue
                owner = input("Enter your full name: ")
                pin = input("Set a 4-digit PIN: ")
                account = BankAccount(owner, pin)
                print(f"Congratulations, {owner}! Your new account has been created. Your account number is {account.account_number}.")
                
            elif choice == 2:
                if account is None:
                    print("Account not found. Please open an account first.")
                    continue
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
                
            elif choice == 3:
                if account is None:
                    print("Account not found. Please open an account first.")
                    continue
                amount = float(input("💸 Enter the amount to withdraw: "))
                account.withdraw(amount)
                
            elif choice == 4:
                if account is None:
                    print("Account not found. Please open an account first.")
                elif not account.verify_pin():
                    print("❌ Incorrect PIN. Access denied.")
                else:
                    print(f"💰 Your current balance is: ₱{account.balance:.2f}")
                
            elif choice == 5:
                if account is None:
                    print("Account not found. Please open an account first.")
                elif not account.verify_pin():
                    print("❌ Incorrect PIN. Access denied.")
                else:
                    # Using yield to show transactions
                    for transaction in account.transaction_history():
                        print(transaction[0], "-", transaction[1])
            
            elif choice == 6:
                if account is None:
                    print("No account to delete.")
                elif not account.verify_pin():
                    print("❌ Incorrect PIN. Access denied.")
                else:
                    account.record_transaction("Account deleted.")
                    account.transaction_history()
                    account = None
                    print("✅ Your account has been successfully deleted.")
                
            elif choice == 7:
                with open("exit_log.txt", "a") as file:
                    file.write(f"{datetime.now()} - User exited the banking system.\n")
                print("Thank you for trusting EverTrust!")
                print("Have a wonderful day ahead!")
                break
                
            else:
                print("⚠️ Invalid choice. Please enter a number between 1 and 7.")
                
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"⚠️ An error occurred: {e}")
            raise

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n⚠️ Program interrupted by user.")
    finally:
        print(":)")