from base_ride import Ride


class PremiumRide(Ride):
    def __init__(self, distance_km, snack):
        super().__init__(distance_km)
        self.__complimentary_snack = snack
        self.__premium_base_rate = 15.00

    def calculate_fare(self):
        return self.__premium_base_rate + (self.distance_km * 3.00)

    def start_ride(self):
        print("Starting VIP ride. Enjoy your snacks!")

    def complete_ride(self):
        print("Completing VIP ride... Thank you for choosing our premium service!")
        print(f"Fare: Php{self.calculate_fare():.2f}")
        print(f"Complimentary Snack: {self.__complimentary_snack}")