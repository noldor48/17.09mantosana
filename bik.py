class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} EUR nogulditi konta.")
        else:
            print("Noguldijuma summa jabut pozitivai")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Nepietiekami lidzekli iznemsanai.")
        elif amount <= 0:
            print("Iznemsanas summai jabut pozitivai.")
        else:
            self.__balance -= amount
            print(f"{amount} EUR iznemti no konta.")
account = BankAccount(100)
print("Pasreizejais atlikums: ", account.get_balance())
account.deposit(50)
print("Pasreizejais atlikums: ", account.get_balance())
account.withdraw(160)
print("Pasreizejais atlikums: ", account.get_balance())