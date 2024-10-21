class BankAccount:
    def __init__(self, balance) -> None:
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance after deposit: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"New balance after withdrawal: {self.balance}")
        else:
            print("Not enough money")

bank = BankAccount(500)

deposit_amount = float(input("Enter amount to deposit: "))
bank.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
bank.withdraw(withdraw_amount)

print(f'Final balance: {bank.balance}')
