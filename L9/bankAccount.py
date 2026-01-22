class InvalidAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self._balance = 0.0

        if initial_balance != 0:
            self.deposit(initial_balance)

    def deposit(self, amount):
        amount = self._validate_amount(amount)
        self._balance += amount


    def withdraw(self, amount):
        amount = self._validate_amount(amount)
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Fond insuficient: sold={self._balance:.2f}, cerut={amount:.2f}"
            )
        self._balance -= amount

    def get_balance(self):
        return self._balance

    @staticmethod
    def _validate_amount(amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise InvalidAmountError("Suma trebuie să fie număr (int/float).")
        amount = float(amount)
        if amount <= 0:
            raise InvalidAmountError("Suma trebuie să fie > 0.")
        return amount

if __name__ == "__main__":
    acc = BankAccount(100)

    try:
        acc.deposit(50)
        print("Sold:", acc.get_balance())

        acc.withdraw(120)
        print("Sold:", acc.get_balance())

        acc.withdraw(1000)
    except (InvalidAmountError, InsufficientFundsError) as e:
        print("Eroare:", e)
