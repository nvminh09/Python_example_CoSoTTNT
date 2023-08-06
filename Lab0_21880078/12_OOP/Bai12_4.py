# Định nghĩa lớp School_bus là một phương thức của lớp Vehicle

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("Volvo", 20, 50)

print(isinstance(School_bus, Vehicle))