class PassengerAccount:
    def __init__(self, name):
        self.name = name
        self.__wallet_balance = 0.0

    def top_up_wallet(self, amount):
        self.__wallet_balance += amount
        if self.__wallet_balance < 0:
            self.__wallet_balance = 0.0
            raise ValueError("Top-up amount cannot be negative.")

    def pay_for_ride(self, fare_amount):
        if self.__wallet_balance < fare_amount:
            raise ValueError("Insufficient funds! Please top up.")
        self.__wallet_balance -= fare_amount
        print(f"Remaining balance: {self.__wallet_balance}")