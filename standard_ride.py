from base_ride import RIDE

class StandardRide(RIDE):
    def __init__(self, distance_km):
        super().__init__(distance_km)
        self.__base_rate = 5.00

    def calculate_fair(self):
        return self.__base_rate + (self.distance_km * 1.50)

    def start_ride(self):
        print(f"Starting Standard Ride for {self.distance_km} km.")

    def complete_ride(self):
        self.is_completed = True
        print ("=== STANDARD RECEIPT ===")
        print(f"Distance: {self.distance_km} km.")
        print(f"Fare: Php{self.calculate_fair() :.2f}")