# Banking System Program

## Overview

This Python program implements a simple banking system where users can open a bank account, deposit money, withdraw money, view account balances, see transaction histories, and delete their account. The system is designed to be user-friendly, with PIN verification required for sensitive actions like deposits, withdrawals, and account deletion. Transaction history is recorded and can be viewed anytime.

### Features:
- **Account Creation**: Allows users to create a new bank account with a unique account number.
- **Deposit**: Users can deposit money into their account after PIN verification.
- **Withdraw**: Users can withdraw money from their account after PIN verification.
- **View Balance**: Users can check their current balance.
- **Transaction History**: Users can view their transaction history, which is sorted by timestamp.
- **Account Deletion**: Users can delete their account, with transaction history recorded.
- **Exit**: Users can exit the program securely, and the exit will be logged.

---

## Python Keywords Used

This program uses the following Python keywords in various places throughout the code:

1. **`import`**: Used to import required modules like `random` and `datetime`.
2. **`from`**: Used for importing specific functions or modules from libraries (e.g., `from datetime import datetime`).
3. **`def`**: Used to define functions, such as `assert_positive`, `deposit`, `withdraw`, `menu`, etc.
4. **`assert`**: Used to ensure that the amount being deposited is positive (`assert_positive` function).
5. **`class`**: Defines the `BankAccount` class which handles all the functionality related to the bank account.
6. **`continue`**: Skips to the next iteration of the loop in the menu if an invalid action is detected.
7. **`if`**: Used for conditional checks, such as verifying if the account exists or if the PIN is correct.
8. **`else`**: Used for handling the alternate case when a condition in an `if` statement fails.
9. **`elif`**: Used to check for other possible choices or conditions in the `if` statement.
10. **`except`**: Used for exception handling, such as catching `ValueError` for invalid input and other general exceptions.
11. **`False`**: Used to indicate when a condition or value is logically false, such as insufficient funds in withdrawal.
12. **`finally`**: Ensures that the program termination message is printed even after handling exceptions.
13. **`for`**: Used for iterating over transactions when displaying the transaction history.
14. **`global`**: Used to reference the global `account` variable inside functions.
15. **`in`**: Used in membership tests (e.g., checking for membership in a list of transactions).
16. **`is`**: Used to check if a variable (`account`) is `None`.
17. **`None`**: Represents the absence of a value, used for when the `account` is not initialized or deleted.
18. **`not`**: Negates conditions (e.g., `if not account` checks if the account is None).
19. **`or`**: Used for logical operations but was not explicitly necessary in this implementation.
20. **`pass`**: A placeholder used in empty blocks, though not explicitly needed in the current implementation.
21. **`raise`**: Used to raise exceptions in case of errors, such as when the user makes an invalid choice.
22. **`return`**: Used to return results from functions, e.g., returning results from the `withdraw` function.
23. **`True`**: Represents a logical truth, used for conditions.
24. **`try`**: Used to wrap code that may throw an exception (e.g., input parsing in the menu).
25. **`while`**: Used for a loop that continuously presents the menu to the user until they choose to exit.
26. **`with`**: Used to handle file operations safely (e.g., logging when the user exits).
27. **`yield`**: Used to yield transaction history one at a time, allowing the `transaction_history` function to generate results lazily.

---

## Installation

1. Clone or download the repository to your local machine.
2. Ensure Python 3.x is installed.
3. Run the program with the following command:

   ```bash
   python bank_system.py
