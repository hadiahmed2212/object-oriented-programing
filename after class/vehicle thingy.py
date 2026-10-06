class vehicle:
    def __init__(self, brand, mx_sp):
        self.brand = brand
        self.mx_sp = mx_sp

    def show_details(self):
        print("brand of car:", self.brand)
        print("car max speed:", self.mx_sp, "km/h")
class car(vehicle):
    def __init__(self, model, seats, brand, mx_spe):
        self.model = model
        self.seats = seats
        super().__init__(brand, mx_spe)

   
    def show_details(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        super().show_details()

    def fuel_type(self, fuel):
        print("fuel type used", fuel)
my_car = car("land cruiser", 7, "toyota", 170)
my_car.show_details()
my_car.fuel_type("diesel")
print("is car subclass of vehicle?", issubclass(car, vehicle))
