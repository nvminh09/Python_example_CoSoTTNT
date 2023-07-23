# Class các loại xe

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        #return f"Sức chứa của xe {self.name} là {self.max_speed}, quãng đường đã chạy là {self.mileage}."

    def seating_capacity(self, capacity):
        return f"Xe {self.name}, tốc độ tối đa là {self.max_speed}, quãng đường {self.mileage}, sức chứa {capacity} hành khách."


class Bus(Vehicle): # Lớp Bus kế thừa Vehicle
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("bus Volvo", 180, 12)
print(School_bus.seating_capacity())